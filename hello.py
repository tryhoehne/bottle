from bottle import route, run

@route('/hello')
def hello():
    return "Hello World!"

run(host='162.209.87.173', port=8080, debug=True)
