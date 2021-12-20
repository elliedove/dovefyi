from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route('/film/')
def about():
    return render_template('film.html')

if __name__ == '__main__':
    app.run(debug=True)