---
published: true
author: "chris-tan"
title: The Remote Debugginator (2015)
---

The Remote Debugginator is a device created for the [Acacia Irrigation Project](http://acaciairrigation.org/) to enable remote access to a LAN network over 3g.

![The Remote Debugginator](/assets/uploads/blog/2016/remote-debugginator/projects_rd1.jpg)

We have three irrigation sites serving about 20 farmers' fields. Each of these sites has a Raspberry Pi collecting data on sunlight, temperature, power consumption, and pump usage.

While working on the the project we encountered a lot of difficulty debugging and collecting data from our irrigation sites remotely. 

![Site 3 - View from a tree](/assets/uploads/blog/2016/remote-debugginator/projects_rd9.jpg)

Collecting data takes a lot of effort. Typically we drive to our sites from Louga (where we are staying) which takes about 45 minutes each way. It's not an easy drive, especially after the rainy season in Senegal.

![Getting stuck in the sand](/assets/uploads/blog/2016/remote-debugginator/projects_rd8.jpg)

The road is extremely sandy and frequently littered with deep potholes where the asphalt has collapsed into the soil. 

This is where the Remote Debugginator becomes useful. All we need is to have a farmer turn the device on near the irrigation system and we're good to go.


## Parts list

![Alt text](/assets/uploads/blog/2016/remote-debugginator/projects_rd6.jpg)

- [Raspberry Pi Kit](http://www.amazon.com/Raspberry-Complete-Starter-Preloaded-Heatsink/dp/B00MV6TAJI/)
    - If you don't want to get a kit, make sure to buy a version 2, as it can [provide more power to USB devices](https://raspberrypi.stackexchange.com/questions/27708/is-setting-max-usb-current-1-to-give-more-power-to-usb-devices-a-bad-idea)
- [Case + Screen for RPi](http://www.amazon.com/Tontec%C2%AE-Raspberry-Display-Touchscreen-Transparent/dp/B00NANNJLQ/)
- [USB battery pack (10000 mAh)](http://www.amazon.com/Anker-10000mAh-Portable-External-Technology/dp/B009USAJCC/)
- 3g USB dongle
    - [Linux compatible dongles](http://elinux.org/RPi_VerifiedPeripherals#USB_3G_Dongles) 
    - Make sure to [check for cell provider support](http://www.worldtimezone.com/gsm.html)
- [Portable keyboard](http://www.amazon.com/Rii-mini-X1-Raspberry-KP-810-10LL/dp/B00I5SW8MC/)
- [Digital Ocean](https://www.digitalocean.com/) instance
- M2M Sim card. Here are some providers:
    - <http://www.podsystemm2m.com/>
    - <http://www.embeddedworks.net/m2m-data.html>
    - <http://neo.aeris.com/pricing/plans-pricing/>


## Raspberry Pi setup

The Pi was set up using the default [Raspbian distro](https://www.raspbian.org/).

Setting up screen:

- <http://s3.amazonaws.com/ttbox/35screen.zip>
- <http://s3.amazonaws.com/ttbox/35calibrate.zip>

Connecting to wifi via command line:

- <https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md>

Preventing Edimax wifi adapter from sleeping during shell sessions when idle:

- <https://www.raspberrypi.org/forums/viewtopic.php?t=61665>

Booting directly into shell:

- <http://stackoverflow.com/a/17830633>


## Booting up

<iframe width="100%" height="330" src="https://www.youtube.com/embed/kkuggWvZ5NY" frameborder="0" allowfullscreen></iframe>


After booting, the Pi will need to:

1. Connect to 3g
2. Set up the reverse tunnel
3. Re-connect automatically to 3g or tunnel

We run the 3g and tunnel shell scripts in separate **screen** windows. This makes it easier to debug should a problem occur.

Setting up scripts:

    sudo apt-get install screen

Add the following to **~/.screenrc**. This enables the remotely logged in user to access the screen session.

    defshell -bash
    multiuser on
    acladd pi

Add the following to **~/.bashrc**. This starts **run.sh** only when the Pi boots up and not when someone connects via SSH or screen. If anyone has a better way to do this I'm all ears.


{% highlight bash %}
if [ -n "$STY" ]; then
    # Screen session.
    echo 'screen session'
elif [ -n "$SSH_CLIENT" ] || [ -n "$SSH_TTY" ]; then
    # SSH Session
    # http://serverfault.com/a/506267
    echo 'ssh session'
else
    # Main session
    echo 'main session'
    ~/run.sh
fi
{% endhighlight %}


Create a file named **run.sh** in your home folder. This starts the 3g and reverse tunnel scripts in separate screen windows.

{% highlight bash %}
#!/bin/bash

# Tip: You can press "Ctrl + a" twice to switch between windows

# Starts a new detached screen session (-dm) named "pi" (-S) with the 
# window title "3g" (-t), and runs 3g script
screen -dmS pi -t 3g /home/pi/3g.sh

# Connects to existing session "pi" (-S) and runs command (-X). 
# When screen is run within screen, it creates a new window named "tunnel" (-t)
# in the current session 
screen -S pi -X screen -t tunnel /home/pi/tunnel.sh

# Attach to 3g window
screen -r pi -p 3g
{% endhighlight %}


## Setting up 3g

![Alt text](/assets/uploads/blog/2016/remote-debugginator/projects_rd3.jpg)

To connect to 3g, we'll need to [install Sakis3g](http://www.sakis3g.com/).  I've left out the steps because getting Sakis working really depends on your modem and cell provider. It's a good idea to try Sakis3g first in interactive mode.

After that, install [UMTSKeeper](http://mintakaconciencia.net/squares/umtskeeper/) to automatically reconnect in the event of a connection failure.


Create a file named **3g.sh** in your home folder. You'll need to modify the *sakisoperators* to fit your configuration.

{% highlight bash %}
#!/bin/bash

# Start UMTSKeeper & Sakis3g

echo 'starting umtskeeper'

# Using Orange Senegal defaults:
sudo /home/pi/umtskeeper/umtskeeper --sakisoperators "USBINTERFACE='3' OTHER='USBMODEM' USBMODEM='1199:68a3' APN='internet' APN_USER='internet' APN_PASS='0'" --sakisswitches "--sudo --console"
{% endhighlight %}


## Reverse tunnel setup (server)

First, you'll need to set up a linux server. I used a $5 / month instance at [Digital Ocean](https://www.digitalocean.com/).

On your server, add this to **/etc/ssh/sshd_config** so that the connection times out after 3 x 60 seconds of unresponsiveness.

    ClientAliveInterval 60

Next, generate an SSH key on the Pi by following the [guide here](https://help.github.com/articles/generating-ssh-keys/). Then copy the Pi's public key to **~/.ssh/authorized_keys** on the DigitalOcean server. This will let the Pi login to the server without a password.

## Reverse tunnel setup (Pi)

Back to the Pi. Add the follow to **~/.ssh/config** so that the client exits after error (usually it will hang) and disconnects after 3 x 60 seconds of unresponsiveness.

    ExitOnForwardFailure yes
    ServerAliveInterval 60

Test out the reverse tunnel by running this command on the Pi. You'll want to replace the IP address with the address of your own server.

    ssh -R 22222:localhost:22 ubuntu@159.203.95.60

If this works, you can log into your server (using a separate terminal) and connect to the Pi via this command:

    ssh -p 22222 pi@localhost
    
Next, we'll install **autossh** which enables automatic reconnection of ssh sessions:

    sudo apt-get install autossh

Create a file named **tunnel.sh** in your home folder. This script waits for the 3g interface to go live before starting the reverse tunnel. It'll also restart the tunnel in the case of an unclean disconnect.

{% highlight bash %}
#!/bin/bash

while true;
do
    echo 'waiting for ppp interface'
    # Check to see if ppp0 is the default gateway
    # http://stackoverflow.com/a/15973156/86568
    if [[ `ip -4 route list 0/0` == *'ppp0'* ]]; then
        echo 'starting reverse tunnel'
        autossh -R 22222:localhost:22 ubuntu@159.203.95.60
        echo 'tunnel connection error'
        sleep 60
    fi
    sleep 5
done
{% endhighlight %}

That's it! If everything works correctly, you should be automatically connecting to the reverse tunnel each time the Pi boots up.


Re-published from: <https://csytan.com>

## Useful links

- <https://unix.stackexchange.com/questions/46235/how-does-reverse-ssh-tunneling-work>
- <http://blogs.wcode.org/2015/04/howto-ssh-to-your-iot-device-when-its-behind-a-firewall-or-on-a-3g-dongle/>
