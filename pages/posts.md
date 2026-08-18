---
layout: default
title: All Posts
---

# All Posts

<div class="post-filters">
  <label for="year-filter">Year:</label>
  <select id="year-filter">
    <option value="">All</option>
  </select>

  <label for="category-filter">Category:</label>
  <select id="category-filter">
    <option value="">All</option>
  </select>

  <button id="reset-filters" type="button">Reset</button>
</div>

<ul id="post-list" class="post-list"></ul>
<p id="post-list-empty" class="post-list-empty" hidden>No posts match those filters.</p>

<script>
(async function () {
  const res = await fetch('{{ "/assets/data/posts.json" | relative_url }}');
  const posts = await res.json();

  const yearSelect  = document.getElementById('year-filter');
  const catSelect   = document.getElementById('category-filter');
  const resetButton = document.getElementById('reset-filters');
  const list        = document.getElementById('post-list');
  const emptyNotice = document.getElementById('post-list-empty');

  // Populate Year dropdown, newest first
  const years = [...new Set(posts.map(p => p.year))].sort().reverse();
  years.forEach(y => {
    const opt = document.createElement('option');
    opt.value = y;
    opt.textContent = y;
    yearSelect.appendChild(opt);
  });

  // Populate Category dropdown, alphabetically
  const categories = [...new Set(posts.flatMap(p => p.categories))].sort();
  categories.forEach(c => {
    const opt = document.createElement('option');
    opt.value = c;
    opt.textContent = c;
    catSelect.appendChild(opt);
  });

  function render() {
    const y = yearSelect.value;
    const c = catSelect.value;

    const filtered = posts.filter(p =>
      (!y || p.year === y) && (!c || p.categories.includes(c))
    );

    list.innerHTML = filtered.map(p => `
      <li>
        <span class="post-date">${p.display_date}</span>
        <a href="${p.url}">${p.title}</a>
        <span class="post-categories">${p.categories.join(', ')}</span>
      </li>
    `).join('');

    emptyNotice.hidden = filtered.length !== 0;
  }

  yearSelect.addEventListener('change', render);
  catSelect.addEventListener('change', render);
  resetButton.addEventListener('click', () => {
    yearSelect.value = '';
    catSelect.value = '';
    render();
  });

  render();
})();
</script>
