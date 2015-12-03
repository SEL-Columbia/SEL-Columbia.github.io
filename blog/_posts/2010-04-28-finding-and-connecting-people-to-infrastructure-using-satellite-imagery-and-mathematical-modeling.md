---
id: 705
title: Finding and Connecting People to Infrastructure using Satellite Imagery and Mathematical Modeling
author: Modi Research Group
excerpt: We are creating a streamlined infrastructure planning system to help local leaders, financiers and utility owners explore scenarios, communicate and negotiate visually.
layout: post
guid: http://modi.mech.columbia.edu/?p=705
permalink: /finding-and-connecting-people-to-infrastructure-using-satellite-imagery-and-mathematical-modeling/
image:
  - http://modi.mech.columbia.edu/wp-content/uploads/2010/04/infrastructure-types-with-border5.jpg
categories:
  - Energy Planning
  - GIS Remote Sensing
tags:
  - Data-Driven Planning
  - Energy Planning
  - Open Source Technology
---
Success in an infrastructure project depends as much on local support and participation as it does on coordination between politicians, financiers and utilities ([Tufte and Mefalopulos 2009][1]). We wanted to create a freely accessible tool for non-technical people to experience the infrastructure planning process and see the impact of different decisions on the community. By experimenting first-hand with web-based software, a user can understand on a map how changes in population, pricing and fiscal policy influence where infrastructure is built, who will get access and why different technologies such as off-grid solar, mini-grid diesel or bio-diesel and grid affect cost. 

Our lab combined technical expertise from remote sensing, operations research and electrical engineering into an easy-to-use system so that local leaders, politicians, financiers and utility owners can focus on communicating visually and negotiating between different electrification scenarios. 

  * Local leaders: Will the construction affect my community?
  * Politicians: How many businesses and households in my district will get access?
  * Financiers: What are the risk and return on investment?
  * Utility owners: Is it technically and financially feasible?

[<img class="alignnone size-large wp-image-792" title="From remote sensing to geospatial optimization" alt="From remote sensing to geospatial optimization" src="http://modi.mech.columbia.edu/wp-content/uploads/2013/06/triptych-revised-1023x333.png" width="553" height="180" />][2] 

**Where do people live?**  The remote sensing component finds where people live using image recognition on satellite imagery. 

[<img class="alignnone size-full wp-image-788" title="Result from scanning our building detector over farmland in Koraro, Ethiopia where red points mark computer guesses and white points mark human guesses" alt="Result from scanning our building detector over farmland in Koraro, Ethiopia where red points mark computer guesses and white points mark human guesses" src="http://modi.mech.columbia.edu/wp-content/uploads/2013/06/20100220-HowPythonIsGuidingInfrastructureConstructionInAfrica_img_49.jpg" width="646" height="618" />][3] 

Results from the remote sensing component provide a spatial census, enabling us to estimate population density and spread with reasonable accuracy. Different settlement patterns hint at different electrification strategies: sparsely distributed clusters as in Ghana or Mali are good candidates for off-grid technologies such as solar, while larger clusters as in Tanzania justify diesel mini-grids and densely packed Kenya find grid electrification to be cost-effective ([Zvoleff, Kocaman, Huh, Modi 2009][4]). [<img class="alignnone size-large wp-image-782" title="Settlement patterns differ greatly by location, resulting in different electrification strategies for off-grid solar systems, mini-grid diesel systems or grid distribution systems." alt="Settlement patterns differ greatly by location, resulting in different electrification strategies for off-grid solar systems, mini-grid diesel systems or grid distribution systems." src="http://modi.mech.columbia.edu/wp-content/uploads/2013/06/settlement-patterns-1024x768.png" width="614" height="461" />][5] 

The command-line software to perform remote sensing was completed in 2008. We are in the process of optimizing the software to run on [graphical processing units][6] (GPUs) to make the system accessible via web. 

**How can we provide access to electricity?**  The econometric and operations research component uses demographics and pricing models to project electricity demand, cost and placement (

[Parshall, Pillai, Mohan, Sanoh, Modi 2009][7]). Users can freely explore what-if scenarios by changing the many parameters and see on a map what technology makes sense for each community, where and how much it will cost. 

We have created a web-based prototype of the infrastructure planning component that is being used this semester by students of the [Master&#8217;s in Development Practice][8] program at Columbia University. We are currently improving the map-based user interface and you will be able to use it through your browser soon. [2013 update: [ Network Planner ][9] is live and functioning in browsers.] 

**The power of open source software**  Both systems are built entirely using open source components such as 

[Python][10], [GDAL][11], [GEOS][12], [Lush][13], [OpenLayers ][14]and [AMQP][15]. </p>

### References

Alex Zvoleff, Ayse Selin Kocaman, Tim Huh, Vijay Modi. (2009) &#8220;The impact of geography on energy infrastructure cost.&#8221; *Energy Policy*, 37, 4066-4078. [[link][4]] 

Lily Parshall, Dana Pillai, Shashank Mohan, Aly Sanoh, Vijay Modi (2009) &#8220;National electricity planning in settings with low pre-existing grid coverage: development of a spatial model and case study of Kenya.&#8221; *Energy Policy*, 37, 2395-2410. [[link][7]] 

Pedro Sanchez et al. (2007) &#8220;The African Millennium Villages.&#8221; *Proceedings of the National Academy of Sciences* 104 (43). [[link][16]] 

Thomas Tufte, Paolo Mefalopulos (2009) *Participatory communication &#8211; a practical guide.* World Bank Working Paper. [[link][1]] 

[<img class="alignnone size-medium wp-image-736" title="The cost of poor planning" alt="The cost of poor planning" src="http://modi.mech.columbia.edu/wp-content/uploads/2013/06/HowPythonIsGuidingInfrastructureConstructionInAfrica_img_49.png" width="300" height="207" />][17] 

### Talks

[How Python is guiding infrastructure construction in Africa][18] PyCon Atlanta February 20, 2010 [[video][19]] 

[The impact of geography on energy infrastructure cost][20] Millennium Villages Student Research Showcase February 18, 2009 [[video][21]] 

[Automatically finding houses in rural satellite images with multiband convolutional neural networks][22] Millennium Villages Student Research Showcase February 18, 2009 [[video][22]] 

[Finding and connecting people in Africa to infrastructure using remote sensing and geospatial optimization][23] O&#8217;Reilly Where 2.0 Conference March 31, 2010 

[<img class="alignnone size-full wp-image-810" title="Locations of the UN Millennium Villages" alt="Locations of the UN Millennium Villages" src="http://modi.mech.columbia.edu/wp-content/uploads/2013/06/UNMillenniumVillagesFromSusanKum-resized.png" width="717" height="554" />][24] 

### Credits

<table>
  <tr>
    <td>
      Principal Investigator
    </td>
    
    <td>
      Vijay Modi
    </td>
  </tr>
  
  <tr>
    <td>
      Project Manager
    </td>
    
    <td>
      J. Edwin Adkins
    </td>
  </tr>
  
  <tr>
    <td>
      Econometric Analysts
    </td>
    
    <td>
      Aly Sanoh, Sahil Shah
    </td>
  </tr>
  
  <tr>
    <td>
      Operations Research Analyst
    </td>
    
    <td>
      Ayse Selin Kocaman
    </td>
  </tr>
  
  <tr>
    <td>
      GIS Specialist
    </td>
    
    <td>
      Susan Kum, Shaky Sherpa
    </td>
  </tr>
  
  <tr>
    <td>
      Lead Software Engineer
    </td>
    
    <td>
      Roy Hyunjin Han
    </td>
  </tr>
  
  <tr>
    <td>
      Software Engineers
    </td>
    
    <td>
      Po-Han Freeza Huang, Andrew Doro
    </td>
  </tr>
  
  <tr>
    <td>
      Image Recognition Consultants
    </td>
    
    <td>
      Yann LeCun, Marc&#8217;Aurelio Ranzato, Peter N. Belhumeur
    </td>
  </tr>
  
  <tr>
    <td>
      Statistician
    </td>
    
    <td>
      Jiehua Chen
    </td>
  </tr>
  
  <tr>
    <td>
      Early Contributors
    </td>
    
    <td>
      Arnaud Algrin, Lily Parshall, Dana Pillai, Shashank Mohan, Alex Hofmann, Alex Zvoleff, Matt Berg
    </td>
  </tr>
  
  <tr>
    <td>
      Educational Consultants
    </td>
    
    <td>
      Rob Garfield, Anders Pearson, Ethan Jucovy, Zarina Mustapha
    </td>
  </tr>
  
  <tr>
    <td>
      Organizations
    </td>
    
    <td>
      <a href="http://www.gatesfoundation.org">Gates Foundation</a>, <a href="http://www.worldbank.org/">World Bank</a>, <a href="http://www.undp.org/">UNDP</a>
    </td>
  </tr>
</table>

 [1]: http://siteresources.worldbank.org/EXTDEVCOMMENG/Resources/Participatorycommunication.pdf
 [2]: http://modi.mech.columbia.edu/wp-content/uploads/2013/06/triptych-revised-1023x333.png
 [3]: http://modi.mech.columbia.edu/wp-content/uploads/2013/06/20100220-HowPythonIsGuidingInfrastructureConstructionInAfrica_img_49.jpg
 [4]: http://www.sciencedirect.com/science/article/pii/S0301421509003231
 [5]: http://modi.mech.columbia.edu/wp-content/uploads/2013/06/settlement-patterns-1024x768.png
 [6]: http://en.wikipedia.org/wiki/Graphics_processing_unit
 [7]: http://www.sciencedirect.com/science/article/pii/S0301421509000561
 [8]: https://new.sipa.columbia.edu/academics/programs/mpa-in-development-practice
 [9]: http://networkplanner.modilabs.org
 [10]: http://www.python.org/
 [11]: http://www.gdal.org/
 [12]: http://trac.osgeo.org/geos/
 [13]: http://lush.sourceforge.net/
 [14]: http://openlayers.org/
 [15]: http://www.amqp.org
 [16]: http://www.pnas.org/content/104/43/16775.abstract
 [17]: http://modi.mech.columbia.edu/wp-content/uploads/2013/06/20100220-HowPythonIsGuidingInfrastructureConstructionInAfrica_img_491.jpg
 [18]: http://us.pycon.org/2010/conference/schedule/event/97/
 [19]: http://modi.mech.columbia.edu/wp-content/uploads/2013/06/HowPythonIsGuidingInfrastructureConstructionInAfrica_img_49.png
 [20]: http://www.earthinstitute.columbia.edu/videos/watch/56
 [21]: http://www.earthinstitute.columbia.edu/videos/watch/5
 [22]: http://www.earthinstitute.columbia.edu/videos/watch/55
 [23]: http://en.oreilly.com/where2010/public/schedule/detail/11162
 [24]: http://modi.mech.columbia.edu/wp-content/uploads/2013/06/UNMillenniumVillagesFromSusanKum-resized.png