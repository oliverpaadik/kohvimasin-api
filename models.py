from app import db

class Log(db.Model):
	__tablename__ = 'log'
	
	id = db.Column(db.Integer, primary_key=True)
	event_name = db.Column(db.String())
	timestamp = db.Column(db.String())
	machine = db.Column(db.String())
	received = db.Column(db.String())
	
	def __init_(self, event_name, timestamp, machine, received):
		self.event_name = event_name
		self.timestamp = timestamp
		self.machine = machine
		self.received = received
		
	def __repr__(self):
		return '<id {}>'.format(self.id)
		
	def serialize(self):
		return {
			'id': self.id, 
			'event_name': self.event_name,
			'timestamp': self.timestamp,
			'machine': self.machine,
			'received': self.received
		}