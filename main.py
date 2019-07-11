from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about-me")
def about_me():
    return render_template("about.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/fakebook")
def clone_book():
    return render_template("fakebook.html")


@app.route("/boogle")
def google():
    return render_template("boogle.html")


@app.route("/hair-salon")
def hair_salon():
    return render_template("hairsalon.html")


if __name__ == '__main__':
    app.run()
