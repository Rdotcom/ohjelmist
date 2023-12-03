
function searchTvShows() {
  const input = document.getElementById('searchInput').value;
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
          image.src = tvShow.show.image?.medium || '';
          image.alt = tvShow.show.name;
          summary.innerHTML = tvShow.show.summary;

          article.appendChild(name);
          article.appendChild(link);
          article.appendChild(image);
          article.appendChild(summary);

          document.getElementById('results').appendChild(article);
        });
  })
      .catch(error => {
        console.log('fetch error', error);
      });
}

