from flask import Flask, render_template, redirect, request
from flask import request

app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/")
def main():
    return render_template("index4.html")


@app.route("/")
def index():
    return redirect("/login")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route('/destinations')
def destinations():
    return render_template('destinations.html')


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


@app.route('/yourbookings')
def yourbookings():
    return render_template('yourbookings.html')


@app.route('/transportation')
def transportation():
    return render_template('transportation.html')


if __name__ == "__main__":
    app.run(debug=True)
