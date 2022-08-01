from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/birthday/')
def products():
    return render_template('birthday.html')

@app.route('/wrong/')
def wrong():
    return render_template('wrong.html')

@app.route('/blah-blah/')
def whow():
    return render_template('blah-blah.html')

@app.route('/wishes/')
def whaow():
    return render_template('wishes.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/oshibka/')
def oshibka():
    return render_template('oshibka.html')

@app.route('/goroskop/')
def goroskop():
    return render_template('goroskop.html')

@app.route('/stol/')
def stol():
    return render_template('stol.html')

if __name__ == "__main__":
    app.run()