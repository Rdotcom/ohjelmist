document.addEventListener('DOMContentLoaded', function () {
      document.getElementById('searchForm').addEventListener('submit', function(event) {
        event.preventDefault();

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

      function displayResults(results) {
        const resultsContainer = document.getElementById('searchResults');
        resultsContainer.innerHTML = '';

        if (results.length === 0) {
          resultsContainer.innerHTML = '<p>No results</p>';
        } else {
          results.forEach(result => {
            const showname = result.show.name;
            const showsummary = result.show.summary || 'No summary available';
            const showimage = result.show.image ? result.show.image.medium : 'no image';

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
    });
