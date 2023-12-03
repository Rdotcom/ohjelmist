async function fetchJoke() {
  try {
    const response = await fetch('https://api.chucknorris.io/jokes/random');
    const joke = await response.json();
    console.log(joke.value);
  } catch (error) {
    console.log('fetch error', error);
  }
}
fetchJoke();

 function getrandomjoke() {
            fetch('https://api.chucknorris.io/jokes/random')
                .then(response => response.json())
                .then(data => {
                    const randomJokeText = document.getElementById('randomJokeText');
                    randomJokeText.textContent = data.value;
                })
                .catch(error => {
                    console.error('Error fetching random joke:', error);
                });
        }

