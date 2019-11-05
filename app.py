from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import datetime

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False
db = SQLAlchemy(app)

from models import *

<<<<<<< HEAD
=======
@app.route("/")
def hello():
    return "Hello World!"

>>>>>>> 55718b2... initial commit of v2
@app.route("/add", methods=['POST'])
def add_log():
    event_name = request.json.get('event_name')
    timestamp = request.json.get('timestamp')
    machine = request.json.get('machine')
    received = datetime.datetime.now().isoformat()
    try:
        log=Log(
            event_name = event_name,
            timestamp = timestamp,
            machine = machine,
            received = received
        )
        db.session.add(log)
        db.session.commit()
        return "Event added to log: {}".format(log.id)
    except Exception as e:
        return (str(e))

@app.route("/getall")
def get_all():
    try:
        log=Log.query.all()
        return  jsonify([e.serialize() for e in log])
    except Exception as e:
	    return(str(e))


if __name__ == '__main__':
    app.run()