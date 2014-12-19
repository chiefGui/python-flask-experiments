from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)

@app.route('/')
def index():
    online_users = mongo.db.users.find({'online': True})
    return render_template('index.html', online_users = online_users)
