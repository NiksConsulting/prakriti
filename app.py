from flask import Flask, redirect, url_for, render_template, send_from_directory, current_app
from pathlib import Path
from flask_cors import CORS
import python_avatars as pa
import os

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'random'
CORS(app)


@app.route('/')
def home():
    # put application's code here
    return render_template('home.html')


@app.route('/avatar')
def avatar():
    randomize = pa.Avatar.random()
    # put application's code here
    randomize.render(path=BASE_DIR / 'static' / 'img' / 'random' / 'random.svg')
    return render_template('avatar.html')


@app.route('/static/img/random/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    DOWNLOAD_DIR = BASE_DIR / 'static' / 'img'
    uploads = os.path.join(DOWNLOAD_DIR, app.config['UPLOAD_FOLDER'])
    print(uploads)
    return send_from_directory(directory=uploads, path=DOWNLOAD_DIR, filename=filename)


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
