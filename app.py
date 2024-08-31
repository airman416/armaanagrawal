from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/me')
def me():
    return render_template("me.html")


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=81)
