from app import db


class Log(db.Model):
    __tablename__ = 'log'
    id = db.Column(db.Integer, primary_key=True)
    motor_name = db.Column(db.String())
    timestamp = db.Column(db.String())
    transaction_id = db.Column(db.Integer())
    machine = db.Column(db.String())
    received = db.Column(db.String())

    def __init_(self, motor_name, timestamp, transaction_id, machine, received):
        self.motor_name = motor_name
        self.timestamp = timestamp
        self.transaction_id = transaction_id
        self.machine = machine
        self.received = received

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'motor_name': self.motor_name,
            'timestamp': self.timestamp,
            'transaction_id': self.transaction_id,
            'machine': self.machine,
            'received': self.received
        }
