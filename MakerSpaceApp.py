
from flask import Flask, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:@localhost/StauntonMakerSpace"
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

    def serialize(self):
        return{'id' : self.id,
        'username' : self.username,
        'email' : self.email,
        'bios' : self.bios

        }

    def __repr__(self):
        return "<User %r>" % self.username

@app.route("/")
def index():
	return "Homepage"

@app.route("/User", methods=["GET"])
def get_all_users():
    members = []
    for x in User.query.all():
        members.append(x.serialize())   
    return jsonify({'member' : members})

@app.route("/User", methods=["POST"])
def create_user():
	user = User(request.form["username"], request.form["email"])
	db.session.add(user)
	db.session.commit()
	return redirect(url_for("index"))

@app.route("/User/<id>", methods=["GET"])
def get_user(id):
    user = db.session.query(User).filter_by(id = id).first()
    return jsonify({'user' : user.serialize()})

@app.route("/User/<username>", methods=["POST"])
def create_profile():
    bios = profile(request.form["profile"])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/User/<username>", methods=["PUT"])
def update_profile():
    return "hello"

@app.route("/User/<username>", methods=["DELETE"])
def delete_profile():
    return "hello"

if __name__ == "__main__":
    app.run()

