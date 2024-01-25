# Movie Metadata Fetcher

## Project Overview
Movie Metadata Fetcher is a dynamic web application designed to provide users with comprehensive data on movies and TV shows. Leveraging the OMDB API, the app furnishes detailed information in an intuitive and user-friendly format, enhancing the movie-selection process. Additionally, it offers personalized features, such as a custom watch list and user profile integration.

## Features
- **Efficient Search**: Easily search for movies and TV shows by title.
- **Detailed Information**: Access in-depth details like plot, director, actors, and more.
- **Personal Watch List**: Conveniently add and manage titles in your watch list.
- **User Authentication**: Secure and straightforward user registration, login, and logout processes.
- **Profile Integration**: Personalize the experience with your profile picture on the navigation bar.
- **Elegant Interface**: Enjoy a visually appealing and user-friendly UI/UX.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask), Flask-Login for session management
- **API Integration**: OMDB API

## Installation and Setup
Ensure you have the following prerequisites:
- Python 3
- Flask
- Flask-Login
- Active Internet connection for API interactions

### Installation Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-github-username/movie-metadata-fetcher.git
   cd movie-metadata-fetcher
   ```

2. **Install Dependencies**
   ```bash
   pip install Flask flask-login
   ```

3. **API Key Configuration**
   - Obtain an API key from [OMDB API](https://www.omdbapi.com/).
   - Insert your API key in `app.py`.

4. **Run the Application**
   ```bash
   python -m flask run
   ```
   Access the app at [http://localhost:5000](http://localhost:5000).

## Usage Guide
- **Search**: Input a title in the search bar and select 'Search'.
- **View Details**: Click 'Details' for comprehensive information.
- **Watch List**: Use 'Add to Watch List' to bookmark titles.
- **User Accounts**: Register, log in, and manage your account.
- **Profile**: View your profile picture in the navigation bar.

## Contributing
We welcome contributions to enhance the Movie Metadata Fetcher!

- Fork the repository.
- Create a feature branch (`git checkout -b feature-branch`).
- Implement your changes and commit (`git commit -am 'Add some feature'`).
- Push to the branch (`git push origin feature-branch`).
- Submit a Pull Request.
