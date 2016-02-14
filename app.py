from flask import Flask


app = Flask(__name__)


@app.route("/page")
def hello():
    return "Some page"

if __name__ == "__main__":
    app.run()
