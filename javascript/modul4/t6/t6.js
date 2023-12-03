function searchJokes() {
            const searchTerm = document.getElementById('searchTerm').value;
            const apiUrl = `https://api.chucknorris.io/jokes/search?query=${encodeURIComponent(searchTerm)}`;

            fetch(apiUrl)
                .then(response => response.json())
                .then(data => {
                    const searchResults = document.getElementById('searchResults');
                    searchResults.innerHTML = '';

                    if (data.result.length === 0) {
                        searchResults.innerHTML = '<p>No results</p>';
                    } else {
                        data.result.forEach(joke => {
                            const article = document.createElement('article');
                            const joketext = document.createElement('p');
                            joketext.textContent = joke.value;

                            article.appendChild(joketext);
                            searchResults.appendChild(article);
                        });
                    }
                })
                .catch(error => {
                    console.error('Error fetching jokes:', error);
                });
        }