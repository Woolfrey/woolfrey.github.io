---
layout: page
title: "Recommended Reading"
permalink: /reading/
---
<a id="top"></a>

People often ask me what kind of books they should read. The answer is: anything that interests you! But otherwise, here is a list of books I have read that I find compelling in some way.

> If you work with data of any kind, I highly recommend the following (all by Edward Tufte):
> 1. The Visual Display of Quantitative Information
> 2. Envisioning Information
> 3. Visual Explanations

<div class="post-filters">
  <label for="reading-sort">Sort by:</label>
  <select id="reading-sort">
    <option value="title-asc">Title (A&ndash;Z)</option>
    <option value="title-desc">Title (Z&ndash;A)</option>
    <option value="year-desc">Year (newest)</option>
    <option value="year-asc">Year (oldest)</option>
  </select>
  <label for="reading-genre">Genre:</label>
  <select id="reading-genre">
    <option value="">All</option>
  </select>
  <label for="reading-year">Year:</label>
  <select id="reading-year">
    <option value="">All</option>
  </select>
  <button id="reading-reset" type="button">Reset</button>
</div>

<ul id="reading-list" class="jw-media-list"></ul>
<p id="reading-empty" class="post-list-empty" hidden>No books match those filters.</p>

<script src="{{ '/assets/js/media-list-filter.js' | relative_url }}"></script>
<script>
  new MediaListFilter({
    jsonUrl: '{{ "/assets/data/books.json" | relative_url }}',
    listId: 'reading-list',
    emptyId: 'reading-empty',
    sortId: 'reading-sort',
    genreId: 'reading-genre',
    yearId: 'reading-year',
    resetId: 'reading-reset',
    creatorField: 'author',
    creatorLabel: 'Author'
  }).init();
</script>

[🔝 Back to top.](#top)
