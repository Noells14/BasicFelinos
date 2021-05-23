from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    return render_template("home.html",titulo="Felinos - Plasma tu idea!")

@app.route('/about', methods=["GET","POST"])
def about():
    return render_template("about.html",titulo="Felinos - Nosotros")

@app.route('/products', methods=["GET","POST"])
def products():
    return render_template("products.html",titulo="Felinos - Trabajando!")

if __name__ == '__main__':
    app.run(host="0.0.0.0")