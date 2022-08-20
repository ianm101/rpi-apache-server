from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Spicy</p>"

if __name__ == "__main__":
    app.run(debug=True)