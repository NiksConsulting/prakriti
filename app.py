from flask import Flask, redirect, url_for, render_template
from pathlib import Path
from flask_cors import CORS
import python_avatars as pa

BASE_DIR = Path(__file__).resolve()

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    # put application's code here
    return render_template('home.html')


@app.route('/avatar')
def avatar():
    randomize = pa.Avatar.random()
    # put application's code here
    randomize.render(self="random.svg", path=BASE_DIR / 'static' / 'img' / 'random')
    return render_template('avatar.html')


@app.route('/about')
def about():
    # put application's code here
    return render_template('about.html')


@app.route('/contact')
def contact():
    # put application's code here
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
