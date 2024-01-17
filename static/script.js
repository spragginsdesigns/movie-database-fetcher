document.getElementById('movieForm').addEventListener('submit', function (e) {
    e.preventDefault();
    var title = document.getElementById('title').value;

    fetch(`/searchMovies?title=${title}`)
        .then(response => response.json())
        .then(data => {
            const searchResults = document.getElementById('searchResults');
            searchResults.innerHTML = '';
            if (data.Search) {
                data.Search.forEach(movie => {
                    const movieElement = document.createElement('div');
                    movieElement.innerHTML = `
                        <p>${movie.Title} (${movie.Year}) 
                            <button onclick="fetchMovieDetails('${movie.imdbID}')">Details</button>
                            <button onclick="addToWatchList('${movie.imdbID}', '${movie.Title.replace(/'/g, "\\'")}', '${movie.Year}')">Add to Watch List</button>
                        </p>
                    `;
                    searchResults.appendChild(movieElement);
                });
            } else {
                searchResults.innerHTML = '<p>No movies found.</p>';
            }
        })
        .catch(error => console.error('Error:', error));
});

function fetchMovieDetails(imdbID) {
    fetch(`/getMovieDetails?imdbID=${imdbID}`)
        .then(response => response.json())
        .then(data => {
            const detailsHTML = `
                <h2>${data.Title} (${data.Year})</h2>
                <img src="${data.Poster}" alt="Movie Poster">
                <p><strong>Genre:</strong> ${data.Genre}</p>
                <p><strong>Director:</strong> ${data.Director}</p>
                <p><strong>Actors:</strong> ${data.Actors}</p>
                <p><strong>Plot:</strong> ${data.Plot}</p>
                <p><strong>Awards:</strong> ${data.Awards}</p>
                <p><strong>IMDB Rating:</strong> ${data.imdbRating}</p>
                <!-- Add more fields as needed -->
            `;
            document.getElementById('movieData').innerHTML = detailsHTML;
        })
        .catch(error => console.error('Error:', error));
}

function addToWatchList(imdbID, title, year) {
    let watchList = JSON.parse(localStorage.getItem('watchList')) || [];
    if (!watchList.includes(imdbID)) {
        watchList.push({ imdbID, title, year });
        localStorage.setItem('watchList', JSON.stringify(watchList));
        displayWatchList();
    }
}

function displayWatchList() {
    let watchList = JSON.parse(localStorage.getItem('watchList')) || [];
    const watchListItems = document.getElementById('watchListItems');
    watchListItems.innerHTML = '';

    watchList.forEach(item => {
        const itemElement = document.createElement('div');
        itemElement.innerHTML = `
            <p>${item.title} (${item.year}) 
                <button onclick="fetchMovieDetails('${item.imdbID}')">View Details</button>
            </p>
        `;
        watchListItems.appendChild(itemElement);
    });
}

document.addEventListener('DOMContentLoaded', displayWatchList);
