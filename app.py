from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')

# @app.route('/')
# def home('/home'):
#     return render_template("./templates/home.html")

@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/about')
def About():
    return render_template("./about.html")


@app.route('/enter')
def enter():
    return render_template("./enter.html")


@app.route('/shoppingbasket')
def shoppingbasket():
    return render_template("./shopping basket.html")


if __name__ == '__main__':
    app.run(debug=True)
