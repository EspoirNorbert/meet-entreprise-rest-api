from api.database import db
from api.utils import Utils
from datetime import datetime

detail_meet = db.Table('detail_meets',
    db.Column('meet_id', db.Integer, db.ForeignKey('meets.id'), primary_key=True),
    db.Column('participant_id', db.Integer, db.ForeignKey('participants.id'), primary_key=True)
)

class Participant(db.Model):
    __tablename__ = 'participants'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(2), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Participant {self.email}'

    def json(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'gender': self.gender,
            'email': self.email,
            'create_at': Utils.format_datetime(self.create_at),
            'update_at': Utils.format_datetime(self.update_at)
        }

    @staticmethod
    def exist_by_email(email: str):
        return Participant.query.filter(Participant.email == email).first() is not None
    
    @staticmethod
    def exist_by_field(fieldName: str):
        return Participant.query.filter(Participant.email == fieldName).first() is not None
    

class Room(db.Model):
    __tablename__ = 'rooms'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    capacity = db.Column(db.String(80), nullable=False)
    state = db.Column(db.Integer, default=0, nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    meets = db.relationship('Meet', backref='room')

    def __repr__(self):
        return f'<Room {self.name}'

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'capacity': self.capacity,
            'state': self.state,
            'create_at': Utils.format_datetime(self.create_at),
            'update_at': Utils.format_datetime(self.update_at)
        }

class Meet(db.Model):
    __tablename__ = 'meets'
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(80), nullable=False)
    hour = db.Column(db.String(80), nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    participants = db.relationship('Participant', secondary=detail_meet, backref=db.backref('participants', lazy='dynamic'))
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))

    def __repr__(self):
        return f'<Meet {self.subject}'

    def json(self):
        return {
            'id': self.id,
            'subject': self.subject,
            'hour': self.hour,
            'room': Room.query.filter_by(id=self.room_id).first().json(),
            'participants': [Participant.json(participant) for participant in self.participants],
            'create_at': Utils.format_datetime(self.create_at),
            'update_at': Utils.format_datetime(self.update_at)
        }
