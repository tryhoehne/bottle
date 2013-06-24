import bottle

@bottle.route('/')
def home_page():
    return "Hello World\n"

@bottle.route('/testpage')
def test_page():
    return 'This is a Test Page'

bottle.debug(True)
bottle.run(host='162.209.87.173', port=8080)
