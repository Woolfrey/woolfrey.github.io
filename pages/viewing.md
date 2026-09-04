---
layout: page
title: "Recommended Viewing"
permalink: /viewing/
---
<a id="top"></a>

<div class="post-filters">
  <label for="viewing-sort">Sort by:</label>
  <select id="viewing-sort">
    <option value="title-asc">Title (A&ndash;Z)</option>
    <option value="title-desc">Title (Z&ndash;A)</option>
    <option value="year-desc">Year (newest)</option>
    <option value="year-asc">Year (oldest)</option>
  </select>
  <label for="viewing-genre">Genre:</label>
  <select id="viewing-genre">
    <option value="">All</option>
  </select>
  <label for="viewing-year">Year:</label>
  <select id="viewing-year">
    <option value="">All</option>
  </select>
  <button id="viewing-reset" type="button">Reset</button>
</div>

<ul id="viewing-list" class="jw-media-list"></ul>
<p id="viewing-empty" class="post-list-empty" hidden>No films match those filters.</p>

<script src="{{ '/assets/js/media-list-filter.js' | relative_url }}"></script>
<script>
  new MediaListFilter({
    jsonUrl: '{{ "/assets/data/films.json" | relative_url }}',
    listId: 'viewing-list',
    emptyId: 'viewing-empty',
    sortId: 'viewing-sort',
    genreId: 'viewing-genre',
    yearId: 'viewing-year',
    resetId: 'viewing-reset',
    creatorField: 'director',
    creatorLabel: 'Director'
  }).init();
</script>

[🔝 Back to top.](#top)
