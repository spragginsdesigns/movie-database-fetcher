from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


@app.route("/")
def index():
    # Serve the main page
    return render_template("index.html")


@app.route("/searchMovies")
def search_movies():
    # Search for movies by title
    title = request.args.get("title")
    api_key = "18da6aa6"  # Replace with your actual OMDB API key
    url = f"http://www.omdbapi.com/?s={title}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)


@app.route("/getMovieDetails")
def get_movie_details():
    # Get detailed information about a movie
    imdb_id = request.args.get("imdbID")
    api_key = "18da6aa6"  # Replace with your actual OMDB API key
    url = f"http://www.omdbapi.com/?i={imdb_id}&apikey={api_key}&plot=full"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
