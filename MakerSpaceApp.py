from flask import Flask, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:kb052591@localhost/StauntonMakerSpace"
app.debug = True
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    bios = db.Column(db.String())
    phone = db.Column(db.Integer())

    def __init__(self, username, email, bios, phone):
        self.username = username
        self.email = email
        self.bios = bios
        self.phone = phone

    def __repr__(self):
        return "<User %r>" % self.username

@app.route("/")
def index():
	return "Homepage"

@app.route("/Users", methods=["GET","POST"])
def users():
	user = User(request.form["username"], request.form["email"])
	db.session.add(user)
	db.session.commit()
	return redirect(url_for("index"))

@app.route("/Users/<username>", methods=["GET","POST","PUT","DELETE"])
def profile():
	return "hello"
if __name__ == "__main__":
    app.run()
