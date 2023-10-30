from flask import Blueprint , abort , request
from api.models import Participant
from api.utils import APIResponse , Utils
from api.factory import ObjectFactory
from api.database import db
from api.decorators import validate_json_payload , validate_data , validate_gender , check_entity_existence

participants = Blueprint("participants" , __name__)

@participants.route('/participants/total' ,methods=['GET'])
def get_participant_total():
    total = Participant.query.count()
    return APIResponse.response(data={'total': total})

@participants.route('/participants' ,methods=['GET'])
def get_all_participant():
    participants =  Participant.query.order_by(Participant.update_at.desc())
    results = [Participant.json(participant) for participant in participants]
    return APIResponse.response(results)

@participants.route('/participants',methods=['POST'])
@validate_json_payload
@validate_data(entity='participant')
@validate_gender
@check_entity_existence(Participant, field_name='email')
def create_participant():
    data = request.json
    new_participant = create_new_participant(data)
    db.session.add(new_participant)
    db.session.commit()
    
    return APIResponse.response(data=new_participant.json()) 

@participants.route('/participants/<int:id>',methods=['GET'])
def show(id):
    participant = exist_by_id(id)
    return APIResponse.response(data=participant.json())

@participants.route('/participants/<int:id>',methods=['PUT'])
@validate_json_payload
@validate_data(entity='participant')
@validate_gender
@check_entity_existence(Participant, field_name='email')
def update_participant(id):    
    participant = exist_by_id(id=id)
    data = request.get_json(True)
    firstname , lastname , gender = data['firstname'] , data['lastname'] , data['gender']
    participant.lastname = lastname
    participant.firstname = firstname
    participant.gender = gender
    participant.email = Utils.generate_email(firstname=firstname,lastname=lastname)
    db.session.commit()
    return APIResponse.response(data=participant.json())


@participants.route('/participants/<int:id>',methods=['DELETE'])
def delete(id):
    participant = exist_by_id(id)   
    db.session.delete(participant)
    db.session.commit()

def create_new_participant(data):
    firstname, lastname = data.get('firstname'), data.get('lastname')
    generated_email = Utils.generate_email(firstname=firstname, lastname=lastname)
    return ObjectFactory.create_participant(data=data, email=generated_email)

def exist_by_id(id) -> Participant | None:
    participant = Participant.query.filter(Participant.id == id).first()
    if participant is None:
        return abort(code=404 , description=f"Participant with ID {id} not found !")
    
    return participant