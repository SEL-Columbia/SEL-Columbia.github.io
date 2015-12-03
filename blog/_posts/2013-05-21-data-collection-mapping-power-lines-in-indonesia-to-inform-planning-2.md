---
id: 46
title: Mapping Power Lines in Indonesia to Inform Planning
author: Jonathan Carbajal
layout: post
guid: http://modilabs.org/?p=46
permalink: /data-collection-mapping-power-lines-in-indonesia-to-inform-planning-2/
post-author:
  - jonathan
categories:
  - Energy Planning
tags:
  - Android
  - Data Collection
  - Field Reports
  - Formhub
  - OSM
---
[<img src="http://modi.mech.columbia.edu/wp-content/uploads/2013/05/EdwinBoatMapping.jpg" alt="EdwinBoatMapping" width="1024" height="578" class="alignnone size-full wp-image-2277" />][1] We are on a boat. It&#8217;s a not-so-atypical workday as we check the number of satellites in the sky visible to our [Android GPS Status app][2] and look up to the surrounding scenery of Alor&#8217;s volcanic calderas surrounding us from the deck of a small fishing boat. <!--more-->It may seem like we are on an exotic vacation but our mission here is one that centers on energy access. Most importantly, we want to understand who has and who does not have electricity access in the Alor archipelago and in turn the entirety of 3 eastern provinces of Indonesia covering nearly 10M people.</p> 

Global energy access is an issue we think about a lot. In more industrialized nations, it&#8217;s often easy to take ubiquitous electricity access for granted but it&#8217;s essential for meeting basic lifeline needs and allows for other untold economic, health & development benefits. 

Energy access is especially sensitive in Indonesia because as of today, there are 78M people in Indonesia (about one-third of the nation), who do not have access to reliable electricity. The Indonesian National electricity company, [PLN][3], is quickly changing this by focusing on expanding generation capacity and improving access to electricity with a strong focus on renewables. PLN is doing an impressive job too&#8211;expanding the grid to 2M people every year. However, a major challenge for long-term electricity planning is collecting and managing information on the location of power lines and related equipment, since the majority of new connections are in remote areas and small islands outside the area covered by the Java-Bali system. Our group from Modi Labs is helping PLN manage this data with improved rapid data collection techniques because, to paraphrase Lord Kelvin, &#8220;if you can not measure it, you can not improve it.&#8221; 

<img class="alignleft" alt="Mapping an electricity pole during training" src="https://lh5.googleusercontent.com/-7jnPMc71nPM/UXcnEz2hDII/AAAAAAAABnM/AzkI3PRioFc/w297-h527-no/IMAG0185.jpg" width="166" height="295" /> 

Which brings us to back to the Android platform and why we spent a working day on a fishing boat in Alor. Alor is emblematic in Indonesia&#8217;s difficulty electrifying rural areas in that as a single PLN branch office it must manage 6 mini-grids with an effective service territory covering 21 separate islands and about 200km of backbone medium-voltage (MV) powerlines. Traveling from minigrid-to-minigrid and island-to-island is time-intensive and often demands a variety of transport modes such as boat, 4&#215;4 or regular vehicles, mopeds or foot travel. Given the difficulty to reach these systems, it becomes critical to take accurate notes and logs whether it&#8217;s for regular maintenance, emergency repair or general data collection for planning needs like in our case. 

Our recent mission to Indonesia in April focused on using Android devices and open-source software applications to map out PLN MV powerlines. Leveraging an Android phone’s multi-functionality allows one to move beyond recording simple latitude/longitude coordinates commonly taken by standalone GPS devices. The Android devices used offered some key enhancements for PLN: 

  1. Custom [formhub][4] surveys allowed for the collection of PLN-specific asset data in the either English or the national language Bahasa Indonesia
  2. [OSMtracker][5] captured geo-referenced traces of existing grid lines with no practical point limit commonly run into on Garmins
  3. After surveying, once we were back in the office, sharing the data was almost instant, through surveys automatically uploaded to formhub.org and .gpx tracks shared electronically or via a private server we had setup for PLN.<img class="alignright" style="font-size: 1rem; line-height: 1;" alt="Traveling along power lines" src="http://farm8.staticflickr.com/7423/8718874872_0f5684eb3d.jpg" width="300" height="400" />

Piecing this very localized and distributed information together quickly put together a comprehensive picture of the extent of current PLN coverage. More importantly though, this information informs mid and high levels of PLN exactly where the need is which in turn better informs more targeted planning. Such a system makes it easier to collaborate across separate sub-systems and islands since multiple staff can simultaneously record data of interest and then commit it to a PLN server each day. Using this data collection technique and Open Street Maps based management systems, PLN was able to map 700km of powerlines over the course of a week. And yes, some of this was even done by boat. 

Stay tuned for a follow-up post on the actual tools and systems used for managing, collaborating and consolidating maps of PLN&#8217;s network.

 [1]: http://modi.mech.columbia.edu/wp-content/uploads/2013/05/EdwinBoatMapping.jpg
 [2]: https://play.google.com/store/apps/details?id=com.eclipsim.gpsstatus2&hl=en
 [3]: http://en.wikipedia.org/wiki/Perusahaan_Listrik_Negara
 [4]: http://formhub.org
 [5]: https://play.google.com/store/apps/details?id=me.guillaumin.android.osmtracker&hl=en