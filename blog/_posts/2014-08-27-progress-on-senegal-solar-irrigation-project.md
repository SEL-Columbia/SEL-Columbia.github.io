---
id: 3909
title: Progress on Senegal Solar Irrigation Project
author: candice-heberer
guid: http://sel.columbia.edu/?p=3909
tags:
  - Acacia Irrigation
  - News
  - Smart Solar Irrigation
  - Irrigation
  - Solar
---
At long last the AC pump controller has arrived at our New York office. Shipped all the way from India this solar management prototype came just when all hope was lost. It promises to reinvigorate the controls development and provide a tangible battery-less solar management solution.

![shakti][1] 

<p class="wp-caption-text">
  AC Pump Controller
</p>



This mysterious white box arrived in tattered cardboard with no documentation and very little indication of how it functioned. After several early morning conversations with the manufacturers and an effort to research each component, a diagram was produced and an understanding of the system began to develop.

![shakti][2] 

<p class="wp-caption-text">
  AC Pump Controller Diagram
</p>



Another setback, the sturdy metal container housing the AC pump controller was heavily battered. A plexi window intended to protect the PLC, Programmable Logic Controller, and meter displays was shattered. The components inside were rattled.

![shakti_damage][3] 

<p class="wp-caption-text">
  AC Pump Controller Damage
</p>



As we analyzed the system, testing individual components, many connections had to be fixed and several components needed to be replaced. As an example, we replaced three 440VAC capacitors.

![shakti_BeforeAfter][4] 

<p class="wp-caption-text">
  Before | After
</p>



The system as is has two circuit breakers where the solar is hooked up. Those lines go directly into the inverter where DC is converted to AC. The inverter filters its input and output through two transformers to subvert electromagnetic interference that can disturb the meters. From the inverter three phase power lines loop through individual CTs, Current Transformers, so the total output can be metered. After looping through the CTs the main power is distributed to seven contactors.  The power lines from each contactor loop through their own CTs and then are outputted through several screw terminals.

![filtersContactosTerminals][5] 

<p class="wp-caption-text">
  Filters, Contactors, and Screw Terminals | Current Transformers
</p>



The control and metering side is powered by a UPS, Uninterruptible Power Supply, which is charged by a dedicated solar panel through a charge controller. Power is drawn from the UPS through a rectifier which outputs 24VDC. The contactors are signaled by the output of the UPS which is directed through the mechanical switches and the relays.

As we move forward, we face several challenges. We plan to retrofit the new AC pump controller to streamline the existing design and include our payment system. With respect to the overall controls, we are still working to measure the total power available. Without a battery bank or charge controller to measure energy available, a new solution must be found. We constructed a simulator to mimic the behavior of the sun programmatically, but the real behavior of the inverter and specific pumps is still unknown. The AC pump controller needs to easily adapt to fluctuations in power. The first field prototype will be used to experimentally verify the stability of the system so alterations can be made if necessary.

![shakti_Brett][6] 

<p class="wp-caption-text">
  Brett Gleitsmann tests out the AC Pump
</p>



Our team is working on several possible solutions simultaneously, but this one is the most promising. The main advantage of this Indian solution is cost. The inverter is almost unbelievably small for how powerful it is. In America or Europe, simply purchasing an inverter with similar capabilities is more expensive than developing the whole prototype in India. In addition, this inverter is promised to function off grid with no battery backup. This function is invaluable and hard to come by.

![horsePowerInverter][7] 

<p class="wp-caption-text">
  18 Horse Power Inverter
</p>



Currently we are in the process of developing an algorithm to manage when pumps should be switched on and off based on energy available, a daily schedule, and account credit. We decided to bypass the PLC, so we installed more sensitive relays and a RS485 to ethernet converter. Now we can access all eight meters and all seven contactors directly from a microcomputer. If it turns out to be cost effective we would like to replace the installed contactors and DC to AC relay system with three phase solid state relays that can be directly signaled from the microcomputer. This would however involve rewiring the physical switches.

![dcToAc][8] 

<p class="wp-caption-text">
  DC signal to AC relays
</p>



Another exciting development; the contract for the acquisition and installation of the 8k Solar Array has been finalized and is due to be installed this month. Procurement of international products has proven to be a large hindrance so this initial installment is a great success. Now that purchasing channels have been formed we anticipate future installments will proceed more smoothly.

We continue to work towards a more sustainable tomorrow.

![shakti_Jack][9] 

<p class="wp-caption-text">
  Jack Bott analyzes and configures the new architecture
</p>

 [1]: /assets/uploads/blog/2014/08/shakti1.jpg
 [2]: /assets/uploads/blog/2014/08/shakti.jpg
 [3]: /assets/uploads/blog/2014/08/shakti_damage.jpg
 [4]: /assets/uploads/blog/2014/08/shakti_BeforeAfter.jpg
 [5]: /assets/uploads/blog/2014/08/filtersContactosTerminals.jpg
 [6]: /assets/uploads/blog/2014/08/shakti_Brett.jpg
 [7]: /assets/uploads/blog/2014/08/horsePowerInverter.jpg
 [8]: /assets/uploads/blog/2014/08/dcToAc.jpg
 [9]: /assets/uploads/blog/2014/08/shakti_Jack.jpg
