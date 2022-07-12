from flask import Flask, redirect, url_for, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():  # put application's code here
    return render_template('home.html')


@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')


@app.route('/contact')
def contact():  # put application's code here
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
