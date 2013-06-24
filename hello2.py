import bottle
import pymongo

@bottle.route('/')
def index():
    connection = pymongo.MongoClient('localhost', 27017)
    db = connection.test
    name = db.names

    item = name.find_one()
    return '<b>Hello %s!<b>' % item['name']

bottle.run(host='162.209.87.173', port=8080)
