from flask import Flask, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import os
import datetime
import pprint
import pytz

app = Flask(__name__)
cors = CORS(app)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False
app.config['CORS_HEADERS'] = 'Content-Type'

password = os.environ['API_KEY']
db = SQLAlchemy(app)

from models import *

@app.route("/data", methods=['POST'])
def add_log():
    # print(dict(request.headers))
    # print(request.data)
    
    if (request.authorization is None):
        return Response(status=401)

    if (request.authorization.password == password):
        timezone = pytz.timezone("Europe/Tallinn")
        request.data = request.data.decode("utf-8")
        # print(request.data)
        ids = []
        for json in request.json:
            motor_name = json.get('motor_name')
            timestamp = json.get('Start_time')
            transaction_id = json.get('Tran_id')
            machine = json.get('machine')
            received = datetime.datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
            try:
                log = Log(
                    motor_name=motor_name,
                    timestamp=timestamp,
                    transaction_id=transaction_id,
                    machine=machine,
                    received=received)
                db.session.add(log)
                db.session.commit()
                ids.append(log.id)
            except Exception as e:
                return (str(e))
        return "Event(s) with ID(s) added to log: {}".format(ids)
    else:
        return Response(status=401)


@app.route("/data")
@cross_origin()
def get_all():
    try:
        log = Log.query.all()
        return jsonify([e.serialize() for e in log])
    except Exception as e:
        return(str(e))

if __name__ == '__main__':
    app.run()
