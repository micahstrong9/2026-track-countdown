from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to your Bounce Log!"

@app.route("/habits")
def habits():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)