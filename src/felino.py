from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    return render_template("home.html",titulo="Felinos - Plasma tu idea!")

@app.route('/about', methods=["GET","POST"])
def about():
    return render_template("about.html",titulo="Felinos - Nosotros")

if __name__ == '__main__':
    app.run(debug=True)