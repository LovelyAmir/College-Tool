import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Load variables from .env file into os.environ
load_dotenv()

app = Flask(__name__)

# Fetch the Neon URL from the environment (with a local fallback if needed)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

'''
# Define your routes
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


def main():
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)


if __name__ == "__main__":
    main()
    '''