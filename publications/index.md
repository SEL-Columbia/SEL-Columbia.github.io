---
title: Publications
---

<style>
  :root {
    --brand-blue: #00adef;
    --badge-bg: #e5f2ff;
    --badge-color: #005fa3;
  }

  /* ─── PANEL (SORT + FILTERS) ──────────────────────────────────────── */
  .panel-div {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    align-items: center;
    margin: 1.5rem 0;
  }
  .sort-group {
    margin-left: auto;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }
  .sort-group label {
    font-weight: 600;
    color: #333;
  }
  .sort-group select {
    padding: 0.3rem 0.6rem;
    border-radius: 4px;
    border: 1px solid #ccc;
  }
  .filter-group { position: relative; }
  .filter-button {
    background: var(--brand-blue);
    color: #fff;
    border: none;
    border-radius: 999px;
    padding: 0.5rem 1rem;
    cursor: pointer;
    font-weight: 600;
  }
  .filter-options {
    display: none;
    position: absolute;
    top: 110%; left: 0;
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 6px;
    padding: 0.75rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    min-width: 240px;
    z-index: 10;

    /* two-column checkbox layout */
    column-count: 2;
    column-gap: 1rem;
  }
  .filter-group.active .filter-options { display: block; }
  .filter-options .controls {
    display: flex;
    justify-content: space-between;
    margin-bottom: 0.5rem;
    column-span: all;
  }
  .filter-options .controls button {
    background: none;
    border: none;
    color: var(--brand-blue);
    text-decoration: underline;
    cursor: pointer;
    padding: 0;
    font-size: 0.9rem;
  }
  .filter-options label {
    display: block;
    break-inside: avoid-column;
    margin: 0.25rem 0;
    cursor: pointer;
  }
  .filter-options input { margin-right: 0.5rem; }

  /* ─── TWO-COLUMN GRID ──────────────────────────────────────────────── */
  #results {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
    list-style: none;
    padding: 0;
    margin: 0;
  }

  /* ─── CARD-STYLE ITEMS ─────────────────────────────────────────────── */
  .publication-item {
    background: #fff;
    border-radius: 8px;
    padding: 1rem;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    display: flex;
    flex-direction: column;
  }
  .publication-item a.pub-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--brand-blue);
    text-decoration: none;
  }
  .publication-item a.pub-title:hover {
    text-decoration: underline;
  }
  .pub-meta {
    margin-top: 0.5rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    font-size: 0.875rem;
    color: #555;
  }
  .pub-year { font-weight: bold; }
  .pub-tag {
    background: var(--badge-bg);
    color: var(--badge-color);
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
    font-size: 0.75rem;
  }
  .country-tag{
    font-style: italic;
  }
</style>

<div>
  <h2 id="products__tools">Publications, Reports, and Briefs</h2>

  <!-- SORT + FILTER PANEL -->
  <div class="panel-div">
    <!-- Years -->
    <div class="filter-group">
      <button class="filter-button">Years ▼</button>
      <div class="filter-options" id="filter-year">
        <div class="controls">
          <button type="button" class="select-all" data-group="year">Select All</button>
          <button type="button" class="clear-filter" data-group="year">Clear All</button>
          <!--need to make it where button is only one button that changes based on what you have clicked (e.g. if select all was clicked, button now says clear all and if clicked around would then say select all)-->
        </div>
        {% for y in (2009..2025) reversed %}
          <label><input type="checkbox" name="year" value="{{ y }}"> {{ y }}</label>
        {% endfor %}
      </div>
    </div>

    <!-- Tags -->
    <div class="filter-group">
      <button class="filter-button">Topics ▼</button>
      <div class="filter-options" id="filter-tags">
        <div class="controls">
          <button type="button" class="select-all" data-group="tags">Select All</button>
          <button type="button" class="clear-filter" data-group="tags">Clear All</button>
        </div>
        {% assign all_tags = site.categories.publications
             | map:"tags" | join:"," | split:"," | uniq | sort %}
        {% for tag in all_tags %}
          {% assign t = tag | strip %}
          <label><input type="checkbox" name="tags" value="{{ t }}"> {{ t }}</label>
        {% endfor %}
      </div>
    </div>

   <!-- countries-->
<div class="filter-group">
  <button class="filter-button">Countries ▼</button>
  <div class="filter-options" id="filter-countries">
    <div class="controls">
      <button type="button" class="select-all" data-group="countries">Select All</button>
      <button type="button" class="clear-filter" data-group="countries">Clear All</button>
    </div>
    {% assign all_countries = site.categories.publications
         | map:"countries" | join:"," | split:"," | uniq | sort %}
    {% assign highlight_countries = "United States,Uganda,Ethiopia,Nigeria,Tanzania,Kenya,Senegal,Ghana,Rwanda,Sub-Saharan Africa" | split: "," %}
    
    {% for country in all_countries %}
      {% assign trimmed = country | strip %}
      {% if highlight_countries contains trimmed %}
        <label><input type="checkbox" name="countries" value="{{ trimmed }}"> {{ trimmed }}</label>
      {% endif %}
    {% endfor %}
    <label><input type="checkbox" name="countries" value="Global"> Global</label>
    <label><input type="checkbox" name="countries" value="Other"> Other</label>
  </div>
</div>

    <!-- Sort by on right -->
    <div class="sort-group">
      <label for="sort-select">Sort by:</label>
      <select id="sort-select">
        <option value="desc">Recent → Oldest</option>
        <option value="asc">Oldest → Recent</option>
      </select>
    </div>
  </div>

  <!-- RESULTS GRID -->
  <ul id="results">
    {% for post in site.categories.publications %}
      <li class="publication-item"
          data-year="{{ post.date | date: '%Y' }}"
          data-tags="{{ post.tags | join: ',' }}"
          data-countries="{{ post.countries | join: ',' }}">
        <a class="pub-title" href="{{ post.link }}">{{ post.title }}</a>
        <div class="pub-meta">
          <span class="pub-year">{{ post.date | date: "%Y" }}</span>
          {% for tag in post.tags %}
            <span class="pub-tag">{{ tag }}</span>
          {% endfor %}
          {% assign highlight_countries = "United States,Uganda,Ethiopia,Nigeria,Tanzania,Kenya,Senegal,Ghana,Rwanda,Global,Sub-Saharan Africa" | split: "," %}
          {% assign display_countries = "" | split: "" %}
          {% assign fallback_countries = "" | split: "" %}

          {% for c in post.countries %}
            {% assign trimmed = c | strip %}
            {% if highlight_countries contains trimmed %}
              {% assign display_countries = display_countries | push: trimmed %}
            {% else %}
              {% assign fallback_countries = fallback_countries | push: trimmed %}
            {% endif %}
          {% endfor %}

          {% if display_countries.size > 0 %}
           <span class="country-tag">{{ display_countries | join: ', ' }}</span>
          {% elsif fallback_countries.size > 0 %}
           <span class="country-tag">Other</span>
          {% else %}
           <span class="country-tag">Global</span>
          {% endif %}

        </div>
      </li>
    {% endfor %}
  </ul>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
  // Dropdown toggles
  document.querySelectorAll('.filter-button').forEach(btn => {
    btn.addEventListener('click', () => {
      const g = btn.closest('.filter-group');
      document.querySelectorAll('.filter-group')
              .forEach(x=> x!==g && x.classList.remove('active'));
      g.classList.toggle('active');
    });
  });
  document.addEventListener('click', e => {
    if (!e.target.closest('.filter-group'))
      document.querySelectorAll('.filter-group')
              .forEach(x=> x.classList.remove('active'));
  });

  // Default all checked
  document.querySelectorAll('.filter-options input[type="checkbox"]')
          .forEach(i => i.checked = true);

  // Select All / Clear All
  document.querySelectorAll('.filter-options button').forEach(btn => {
    const grp = btn.dataset.group;
    const sel = btn.classList.contains('select-all');
    btn.addEventListener('click', () => {
      document.querySelectorAll(`input[name="${grp}"]`)
              .forEach(i => i.checked = sel);
      applyFiltersAndSort();
    });
  });

  // Sort change
  document.getElementById('sort-select')
          .addEventListener('change', applyFiltersAndSort);

  // Filter change
  document.querySelectorAll('.filter-options input[type="checkbox"]')
          .forEach(i => i.addEventListener('change', applyFiltersAndSort));

  applyFiltersAndSort();
});

function applyFiltersAndSort() {
  // Gather
  const years = Array.from(document.querySelectorAll('input[name="year"]:checked'))
                     .map(i => i.value);
  const allY  = years.length === document.querySelectorAll('input[name="year"]').length;

  const tags  = Array.from(document.querySelectorAll('input[name="tags"]:checked'))
                     .map(i => i.value);
  const allT  = tags.length === document.querySelectorAll('input[name="tags"]').length;

  const countries  = Array.from(document.querySelectorAll('input[name="countries"]:checked'))
                     .map(i => i.value);
  const allC  = countries.length === document.querySelectorAll('input[name="countries"]').length;

  // Filter + collect visible
  const items = Array.from(document.querySelectorAll('.publication-item'));
  const vis = items.filter(item => {
  const yr   = item.dataset.year;
  const tArr = item.dataset.tags.split(',');
  const okY  = allY || years.includes(yr);
  const okT  = allT || tags.some(tag => tArr.includes(tag));

  const highlightCountries = [
    "United States", "Uganda", "Ethiopia", "Nigeria",
    "Tanzania", "Kenya", "Senegal", "Ghana", "Rwanda", "Global", "Sub-Saharan Africa"
  ];
  const rawCountries = item.dataset.countries.split(',').map(c => c.trim());

  const mappedCountries = rawCountries.map(c => {
    if (c === "Global") return "Global";
    return highlightCountries.includes(c) ? c : "Other";
  });

  const okC = allC || mappedCountries.some(c => countries.includes(c));

  item.style.display = (okY && okT && okC) ? '' : 'none';
  return okY && okT && okC;
});


  // Sort
  const order = document.getElementById('sort-select').value;
  vis.sort((a, b) => {
    const ya = +a.dataset.year, yb = +b.dataset.year;
    return order === 'asc' ? ya - yb : yb - ya;
  });

  // Re-append in sorted order
  const container = document.getElementById('results');
  vis.forEach(item => container.appendChild(item));
}
</script>