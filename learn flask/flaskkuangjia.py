# -*- encoding=UTF-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'
    print 1/10.94
if __name__ == '__main__':
    app.run(debug=True)
