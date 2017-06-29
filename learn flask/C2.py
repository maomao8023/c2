#-*- encoding=UTF-8 -*-

from flask import Flask, render_template, request, make_response, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'

@app.route('/profile/<int:uid>/')
def profile(uid):
    return render_template('profile.html', uid=uid)

@app.route('/request/')
def request_demo():
    res = request.args.get('key', 'defaultkey') + '<br>'
    res = res + request.url +request.path
    for property in dir(request):
        res = res + '<br>' + str(eval('request.' + property)) + '<br>'
        response = make_response(res)
    return response

@app.route('/newpath/')
def newpath():
    return 'newpath'

@app.route('/re/<int:code>')
def redirect_demo(code):
    return redirect('/newpath', code=code)

if __name__ == '__main__':
    app.run(debug=True)
