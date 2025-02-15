---
title: Rechargeable Portable PowerPack
author: jack-bott
type: Sustainable Energy
image: /assets/uploads/blog/2010/04/powerpack.png
main_link: /powerpack/
related_blog_entries: /tags/#PowerPack
summary: "The portable PowerPack has multiple potential uses but was primarily designed to address the lighting needs of rural populations in developing countries where nearly two billion people worldwide currently lack access to electric lighting."
---

<div class="row-fluid">
  <div class="span12">
    <img src="/assets/uploads/blog/2010/04/DigitalDesignRev7circuit.jpg" alt="PowerPack" />
  </div>
</div>

<br>

<div class="row-fluid">
  <div class="span9">

    <p>
      The portable PowerPack has multiple potential uses but was primarily designed to address the lighting needs of rural populations in developing countries where nearly two billion people worldwide currently lack access to electric lighting.
    </p>

    <p>
      For example, only 2% of rural western Kenya has access to grid electrification, and 97% of homes use kerosene wick lamps and kerosene lanterns for lighting. Kerosene wick lamps have a very low initial purchase cost, generally less than $0.25, but provide very little light. They produce between 10-20 lumens (or 0.5 lux at 2m) &#8212; little more than a standard wax candle. And despite costs as high as $20-25 per year for kerosene to fuel the wick lamp for 3 to 4 hours per day, the light is substandard, grossly inadequate for reading and produces a sooty flame.
    </p>

  </div>

  <div class="span3">
    <p class="wp-caption-text" style="line-height:17pt;">
      <strong>Project Type:</strong> Sustainable Energy
    </p>

    <p class="wp-caption-text" style="line-height:17pt;">
      <strong>Menu:</strong><br />
      <a href="#Papers">Papers</a><br />
      <a href="/tags/#PowerPack"> Related Blog Entries</a>
    </p>

  </div>
</div>

<div class="row-fluid">
  <div class="span12">

    <p>
      The PowerPack offers substantially better light than kerosene lamps as well as the flexibility to power other appliances. It provides nearly 2.5 Ampere-hours of usable electricity at 12V and can power either a 5W compact fluorescent (200 lumens) or a one watt LED bulb (35 lumens). Both the CFL and LED lights can provide 20 to 40 times the lux levels of a kerosene wick lamp. The LED achieves these high lux levels by directing its lower lumen output to a smaller spot size ideal for task lighting. The Power Pack can also provide power to charge a cell phone or run a 12V radio.
    </p>

    <p>
      The PowerPack consists of a charge and discharge control circuit and a sealed lead acid battery. It has one input jack, to connect to a DC charging source, and two outlets so it can be used for lighting as well as playing a 12V radio at the same time. It can also be used to recharge a cell phone with an appropriate adapter. The PowerPack can be recharged using a solar panel. Alternatively, when discharged, the portable PowerPack can be carried to a charging location, such as a school, community center, or battery charging business. Where AC power is available, the PowerPack can be charged by an AC/DC converter that provides DC input.
    </p>

    <p>
      The electronic features of the PowerPack also offer advantages. The PowerPack includes a charge and discharge control circuit that ensures efficient and safe charging. The circuitry protects the battery from the damage caused by deep discharge, excessively rapid charging, or charging beyond the battery’s upper limit. This protection is designed to prolong the lifespan of the PowerPack’s battery.
    </p>

  </div>
</div>

<div class="row-fluid">
  <div class="span12">
    <hr />
    <a id="Papers"></a>
    <h3>Papers</h3>
    <div class="post-list" style="list-style-type:none">
      {% for post in site.categories.publications %}
        {%if post.tags contains 'PowerPack' %}
          {% include pub_project_listing.html post=post %}
        {% endif %}
      {% endfor %}
    </div>
  </div>
</div>
