from flask import Flask,render_template
from flask_pymongo import PyMongo
import json


app = Flask(__name__)

# mongodb connection
app.config["MONGO_URI"] = 'mongodb://localhost:27017/store'
mongo = PyMongo(app)


@app.route('/')
def show_users():
    users = mongo.db.users.find({})
    response = []
    for user in users: 
        user['_id'] = str(user['_id'])
        response.append(user["name"])
    return json.dumps(response)


if __name__=='__main__':
    app.run(port=3000, debug=True)