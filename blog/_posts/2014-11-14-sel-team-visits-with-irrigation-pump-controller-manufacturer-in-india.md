---
id: 4184
title: SEL team visits with irrigation pump controller manufacturer in India
author: Candice Heberer
layout: post
guid: http://sel.columbia.edu/?p=4184
permalink: /sel-team-visits-with-irrigation-pump-controller-manufacturer-in-india/
categories:
  - News
  - Smart Solar Irrigation
tags:
  - Irrigation
  - Solar
---
While the first pump controller was on its way to Senegal, the site of our smart solar irrigation project, the SEL team traveled to Coimbatore, India to meet with the manufacturer, <a href="http://www.sakthistabilizer.in" title="Sakthi Electrical Control" target="_blank">Sakthi Electrical Control</a>. We were eager to test the 2nd generation pump controller as well as discuss our future partnership.



![sakthiOwner][1] 

<p class="wp-caption-text">
  The owner of Sakthi Electrical Control, S. Thilagar, in front of the 2nd gen controller
</p>



### Testing

In collaboration with their technical team, we tested the new unit under multiple inductive loads (1hp and 3hp motors). We were curious to see its performance being that this was our first opportunity to test the controller with anything other than a resistive load (e.g., light bulb). Overall, it was what we were hoping for: Whenever the voltage dropped below the 430V threshold, the VFD tripped, shutting off the motors. And when the voltage came back up to a level above 430V, the VFD came back on automatically, starting the motors using a soft start. Hopefully this will be the case when we install this in the field next month.



![jackTestingIndia][2] 



We also studied the issue of inrush current during startup, which has been a concern for us. Pumps and other inductive loads can pull current surges of 6x their nominal load for a couple of seconds at startup. This becomes a major design factor once we are looking at multiple loads and we want to make sure that our controller can handle these surges. Using an oscilloscope, we determined the demands of adding 1hp loads and observed the controller’s behavior under multiple scenarios. Perhaps the most interesting outcome was that when we applied an additional load to an already loaded system, the inrush current demand was about half the demand of the system being turned on in isolation.



![graph1][3] 

<p class="wp-caption-text">
  Turning on first 1hp pump requires 13.0 Amp inrush current.
</p>

![graph2][4] 

<p class="wp-caption-text">
  Turning on 1hp pump with 1hp load already on requires 6.4 Amp inrush current.
</p>

![graph3][5] 

<p class="wp-caption-text">
  Turning on 1hp pump with 4hp load already on requires 6.2 Amp inrush current.
</p>



As seen in the graphs, when the system had an existing inductive load (1hp or 4hp) and we added an additional 1hp load, the marginal inrush current was 6.2 – 6.4 A. However, when the same 1hp load is added in isolation, with nothing else on, the inrush current is 13 A. So as more loads come online, handling the inrush currents becomes increasing less of a problem. This should help ensure that our VFD, meters and other electronics components can support the frequent turning on and off of pumps as is the case in Senegal.



### Farm visit

![pumpMadurai][6] 



We were excited to have the opportunity to visit an existing 5hp pump controller, installed by Shakthi in 2012 outside of Madurai about 75km from Coimbatore. The unit is a great example, as it has been operational without any significant problems, and more importantly, the farmer has been happy with its performance.



### Possible vendors

![indiaManufacturing][7] 



We also visited a few Indian-based companies who manufacture components that could be integrated into our solution for Senegal, including affordable submersible pumps, batteryless solar trackers and smart meters.

### Next steps

We&#8217;re looking forward to testing the first controller in the field in Potou, Senegal, in December. Then, after incorporating our findings, work will begin on the 2nd and 3rd pilot installations, perhaps with a few new and improved components.

 [1]: /assets/uploads/blog/2014/11/sakthiOwner.jpg
 [2]: /assets/uploads/blog/2014/11/jackTestingIndia.jpg
 [3]: /assets/uploads/blog/2014/11/graph1.png
 [4]: /assets/uploads/blog/2014/11/graph2.png
 [5]: /assets/uploads/blog/2014/11/graph3.png
 [6]: /assets/uploads/blog/2014/11/pumpMadurai.jpg
 [7]: /assets/uploads/blog/2014/11/indiaManufacturing.jpg