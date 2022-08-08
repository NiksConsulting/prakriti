from flask import Flask, redirect, url_for, render_template, send_from_directory, current_app, request
from pathlib import Path
from flask_cors import CORS
import python_avatars as pa
import os

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__, static_url_path='/static')
app.config['UPLOAD_FOLDER'] = 'random'
CORS(app)


@app.route('/')
def home():
    # put application's code here
    return render_template('home.html')


@app.route('/avatar', methods=['GET'])
def avatar():
    args = request.args

    # Get attributes from request
    print("Args:", len(args))
    if len(args) > 0:
        style = args.get("avatarStyle")
        if style is not None:
            style = style.upper()
        else:
            style = 'TRANSPARENT'

        top = args.get("topType")
        if top:
            top = top.upper()
        else:
            top = 'DREADS'

        skin_color = args.get("skinColor")
        if skin_color:
            skin_color = str("#") + str(skin_color)

        mouth = args.get("mouthType")
        if mouth:
            mouth = mouth.upper()
        else:
            mouth = 'DEFAULT'
        print("top:", top, "skin:", skin_color, "mouth:", mouth)
        my_avatar = pa.Avatar(

            style=pa.AvatarStyle[style],  # 0
            skin_color=skin_color,  # 1
            mouth=pa.MouthType[mouth],  # 2

            top=pa.HairType[top],  # 5
        )
    else:
        my_avatar = pa.Avatar.random()
    # put application's code here
    my_avatar.render(path=BASE_DIR / 'static' / 'img' / 'random' / 'random.svg')
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
