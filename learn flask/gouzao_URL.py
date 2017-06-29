from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/')
def index():
    pass

@app.route('/login')
def login():
    pass

@app.route('/user/<username>')
def profile(username=None):
    return render_template('profile.html',name = username)

with app.test_request_context():
    print url_for('index')
    print url_for('login')
    print url_for('login', next='/')
    print url_for('profile', username = 'maomao')
    print url_for('static', filename='style.css')

if __name__ == '__main__':
    app.run()