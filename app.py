from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    g,
    jsonify,
    flash,
)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (
    login_required,
    current_user,
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
)
import requests

app = Flask(__name__)

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "your_secret_key"  # Replace with a strong secret key

db = SQLAlchemy(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)


# Movie Model
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imdbID = db.Column(db.String(100), unique=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.String(4), nullable=False)
    users = db.relationship("User", secondary="user_movies")


# UserMovies association table
user_movies = db.Table(
    "user_movies",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("movie_id", db.Integer, db.ForeignKey("movie.id"), primary_key=True),
)


# User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    watchlist = db.relationship(
        "Movie", secondary=user_movies, backref="watchlist_users"
    )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# User loader function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Create database tables
with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)  # Log the user in
            return redirect(url_for("index"))
        return redirect(url_for("login", error="Invalid credentials"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    logout_user()  # Log the user out
    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Check if username already exists
        user = User.query.filter_by(username=username).first()
        if user:
            flash("Username already exists. Please choose a different one.")
            return redirect(url_for("register"))

        # Create new user
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful. Please log in.")
        return redirect(url_for("login"))  # Redirect to login page

    return render_template("register.html")


@app.route("/watchlist")
def watchlist():
    user = User.query.get(session["user_id"])
    return render_template("watchlist.html", movies=user.watchlist)


@app.route("/add_to_watchlist/<int:movie_id>", methods=["POST"])
@login_required
def add_to_watchlist(movie_id):
    print(f"Movie ID: {movie_id}")  # This will print the movie_id to the console
    movie = Movie.query.get(movie_id)
    if movie not in current_user.watchlist:
        current_user.watchlist.append(movie)
        db.session.commit()
    return redirect(url_for("watchlist"))


@app.route("/add_to_watchlist", methods=["POST"])
def add_to_watchlist_post():
    data = request.get_json()
    imdbID = data["imdbID"]
    title = data["title"]
    year = data["year"]
    # Rest of your code...

    # Check if movie already exists in the database
    movie = Movie.query.filter_by(imdbID=imdbID).first()

    # If movie doesn't exist, create a new one
    if movie is None:
        movie = Movie(imdbID=imdbID, title=title, year=year)
        db.session.add(movie)
        db.session.commit()

    # Add movie to user's watchlist
    user = User.query.get(session["user_id"])
    user.watchlist.append(movie)
    db.session.commit()

    return jsonify(success=True)


@app.route("/searchMovies")
def search_movies():
    title = request.args.get("title")
    api_key = "18da6aa6"
    url = f"http://www.omdbapi.com/?s={title}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)


@app.route("/getMovieDetails")
def get_movie_details():
    imdb_id = request.args.get("imdbID")
    api_key = "18da6aa6"
    url = f"http://www.omdbapi.com/?i={imdb_id}&apikey={api_key}&plot=full"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
