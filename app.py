from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///customers.db"
db = SQLAlchemy(app)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)


@app.route("/")
def index():
    customers = Customer.query.all()
    return render_template("index_1.html", customers=customers)


@app.route("/add", methods=["POST"])
def add_customer():
    name = request.form["name"]
    email = request.form["email"]
    new_customer = Customer(name=name, email=email)
    db.session.add(new_customer)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/delete/<int:id>")
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
