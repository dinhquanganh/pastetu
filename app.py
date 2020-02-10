from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/landing')
def landing():
    return render_template('landing-page.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')   

@app.route('/login')
def login():
    return render_template('login.html')   

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 