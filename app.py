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
import requests

app = Flask(__name__)

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "your_secret_key"  # Replace with a strong secret key

db = SQLAlchemy(app)


# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


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
            session["user_id"] = user.id
            session["username"] = user.username  # Store username in session
            return redirect(url_for("index"))
        return redirect(url_for("login", error="Invalid credentials"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()  # Clear session
    return redirect(url_for("index"))  # Redirect to home page


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
    if "user_id" not in session:
        return redirect(url_for("login"))
    # Logic to display watchlist goes here
    return render_template("watchlist.html")


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
