# Movie Metadata Fetcher

## Project Overview
Movie Metadata Fetcher is a web application that allows users to search for movies and TV shows, view detailed information about them, and create a personal watch list. The app utilizes the OMDB API to fetch data and presents it in an easily navigable format.

## Features
- Search for movies and TV shows by title
- View detailed information including plot, director, actors, and more
- Add titles to a personal watch list
- Elegant and user-friendly interface

## Technologies Used
- Frontend: HTML, CSS, JavaScript
- Backend: Python (Flask)
- API: OMDB API

## Installation and Setup

### Prerequisites
- Python 3
- Flask
- Internet connection for API access

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-github-username/movie-metadata-fetcher.git
   cd movie-metadata-fetcher
   ```

2. **Install Flask**
   If Flask is not already installed:
   ```bash
   pip install Flask
   ```

3. **API Key Configuration**
   - Obtain an API key from [OMDB API](https://www.omdbapi.com/apikey.aspx).
   - Insert your API key in `app.py`.

4. **Run the Application**
   ```bash
   python -m flask run
   ```
   Access the app at `http://localhost:5000`.

## Usage
- **Search**: Enter a movie or TV show title in the search bar and hit 'Search'.
- **View Details**: Click on 'Details' to view more information about the title.
- **Add to Watch List**: Click on 'Add to Watch List' to save the title for later viewing.

## Contributing
Contributions to the Movie Metadata Fetcher are welcome!
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.