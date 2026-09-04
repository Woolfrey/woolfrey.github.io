/*
 * MediaListFilter
 * ---------------------------------------------------------------
 * Shared sort + filter engine for the Recommended Reading and
 * Recommended Viewing pages. Both pages fetch their own JSON data
 * (books.json / movies.json) and instantiate this with their own
 * field names -- the sort/filter/render logic itself lives here
 * once, instead of being duplicated on each page.
 *
 * Expected item shape (both books.json and movies.json match this):
 *   { title, year, genre: [...], cover, synopsis, <creatorField>: "..." }
 *   synopsis may be an empty string -- render() skips it when blank.
 *
 * Usage (see reading.md / viewing.md):
 *   new MediaListFilter({
 *     jsonUrl: '/assets/data/books.json',
 *     listId: 'reading-list',
 *     emptyId: 'reading-empty',
 *     sortId: 'reading-sort',
 *     genreId: 'reading-genre',
 *     yearId: 'reading-year',
 *     resetId: 'reading-reset',
 *     creatorField: 'author',
 *     creatorLabel: 'Author'
 *   }).init();
 */
class MediaListFilter {
  constructor(options) {
    this.jsonUrl      = options.jsonUrl;
    this.creatorField = options.creatorField;
    this.creatorLabel = options.creatorLabel;

    this.list        = document.getElementById(options.listId);
    this.emptyNotice = document.getElementById(options.emptyId);
    this.sortSelect  = document.getElementById(options.sortId);
    this.genreSelect = document.getElementById(options.genreId);
    this.yearSelect  = document.getElementById(options.yearId);
    this.resetButton = document.getElementById(options.resetId);

    this.items = [];
  }

  async init() {
    const res = await fetch(this.jsonUrl);
    this.items = await res.json();

    this.populateGenres();
    this.populateYears();
    this.bindEvents();
    this.render();
  }

  populateGenres() {
    const genres = [...new Set(this.items.flatMap(i => i.genre))].sort();
    genres.forEach(g => {
      const opt = document.createElement('option');
      opt.value = g;
      opt.textContent = g;
      this.genreSelect.appendChild(opt);
    });
  }

  populateYears() {
    // Some entries may have no year yet (year: null in the data) --
    // filter those out of the dropdown rather than showing "null".
    const years = [...new Set(this.items.map(i => i.year).filter(y => y))]
      .sort((a, b) => b - a);
    years.forEach(y => {
      const opt = document.createElement('option');
      opt.value = y;
      opt.textContent = y;
      this.yearSelect.appendChild(opt);
    });
  }

  bindEvents() {
    this.sortSelect.addEventListener('change', () => this.render());
    this.genreSelect.addEventListener('change', () => this.render());
    this.yearSelect.addEventListener('change', () => this.render());
    this.resetButton.addEventListener('click', () => {
      this.sortSelect.value = 'title-asc';
      this.genreSelect.value = '';
      this.yearSelect.value = '';
      this.render();
    });
  }

  render() {
    const genre = this.genreSelect.value;
    const year  = this.yearSelect.value;
    const sort  = this.sortSelect.value;

    const filtered = this.items.filter(i =>
      (!genre || i.genre.includes(genre)) &&
      (!year || String(i.year) === year)
    );

    filtered.sort((a, b) => {
      switch (sort) {
        case 'title-desc': return b.title.localeCompare(a.title);
        case 'year-asc':   return (a.year || 0) - (b.year || 0);
        case 'year-desc':  return (b.year || 0) - (a.year || 0);
        default:           return a.title.localeCompare(b.title); // title-asc
      }
    });

    this.list.innerHTML = filtered.map(i => `
      <li class="jw-media-row">
        <img class="jw-media-cover" src="${i.cover}" width="100" height="auto" loading="lazy" alt="${i.title} cover">
        <div class="jw-media-main">
          <span class="jw-media-title">${i.title}</span>
          <span class="jw-media-meta">${this.creatorLabel}: ${i[this.creatorField]}${i.year ? ` &middot; ${i.year}` : ''}</span>
          <span class="jw-media-tags">${i.genre.join(', ')}</span>
          ${i.synopsis ? `<span class="jw-media-synopsis">${i.synopsis}</span>` : ''}
        </div>
      </li>
    `).join('');

    this.emptyNotice.hidden = filtered.length !== 0;
  }
}
