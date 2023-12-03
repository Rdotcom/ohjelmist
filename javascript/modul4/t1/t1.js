document.addEventListener('DOMContentLoaded', function (event) {
      event.preventDefault();

        const query = document.getElementById('query').value;
        const apiUrl = `https://api.tvmaze.com/search/shows?q=${query}`;

        fetch(apiUrl)
          .then(response => response.json())
          .then(data => {
            console.log('Search result:', data);
          })
          .catch(error => {
            console.log('Error fetching data:', error);
          });
      });
