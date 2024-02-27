from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/input_form")
def input_form():
    return render_template("input_form.html")


if __name__ == "__main__":
    app.run()