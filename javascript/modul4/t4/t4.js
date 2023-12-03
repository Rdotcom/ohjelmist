document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('searchForm').addEventListener('submit', function(event) {
        event.preventDefault();
        searchTvShows();
        const query = document.getElementById('query').value;
        const apiUrl = `https://api.tvmaze.com/search/shows?q=${query}`;

   fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        console.log('Search result:', data);
        displayResults(data);
      })
      .catch(error => {
        console.log('Error fetching data:', error);
      });
      });
});
  function displayResults(results) {
    const resultsContainer = document.getElementById('results');

    if (results.length === 0) {
      resultsContainer.innerHTML = '<p>No results</p>';
    } else {
      results.forEach(result => {
        const showname = result.show.name;
        const showsummary = result.show.summary || 'No summary available';
        const showimage = result.show.image
            ? result.show.image.medium
            : 'https://via.placeholder.com/210x295?text=Not%20Found';

        const resultItem = `
              <div>
                <h2>${showname}</h2>
                <img src="${showimage}" alt="${showname} Image">
                <p>${showsummary}</p>
              </div>
            `;

        resultsContainer.innerHTML += resultItem;
      });
    }
  }

function searchTvShows() {
  const input = document.getElementById('query').value;
  fetch(`https://api.tvmaze.com/search/shows?q=${encodeURIComponent(input)}`)
      .then(response => response.json())
      .then(data => {
        document.getElementById('results').innerHTML = '';

        data.forEach(tvShow => {
          const article = document.createElement('article');
          const name = document.createElement('h2');
          const link = document.createElement('a');
          const image = document.createElement('img');
          const summary = document.createElement('div');

          name.textContent = tvShow.show.name;
          link.href = tvShow.show.url;
          link.target = '_blank';
          link.textContent = 'Details';
          image.src = tvShow.show.image?.medium ? tvShow.show.image.medium : 'https://via.placeholder.com/210x295?text=Not%20Found';
          image.alt = tvShow.show.name;
          summary.innerHTML = tvShow.show.summary;

          article.appendChild(name);
          article.appendChild(link);
          article.appendChild(image);
          article.appendChild(summary);

          document.getElementById('results').appendChild(article);
        });
        displayResults(data);
  })
      .catch(error => {
        console.log('fetch error', error);
      });
}


