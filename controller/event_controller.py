from flask import Blueprint, jsonify, render_template, request
from controller.userlogin import verificar_token
from controller.validator.event_validator import EventValidator
from services.event_service import EventService

event = Blueprint('event', __name__)

event_service = EventService()

@event.route('', methods=['GET'])
def get_events():
    events = event_service.get_all_events()
    return jsonify([event.to_dict() for event in events])

@event.route('/<int:event_id>', methods=['GET'])
def get_event(event_id):
    try:
        event = event_service.get_event(event_id)
        return jsonify(event.to_dict())
    except ValueError as e:
        return jsonify({'message': str(e)}), 404
    
@event.route('', methods=['POST'])
def create_event():
        data = request.get_json()
        name = data.get('name')
        date = data.get('date')
        location = data.get('location')
        description = data.get('description')
        try:
            event_validator = EventValidator(name, date, location, description)
            event_validator.validate()
            event = event_service.create_event(name, date, location, description)
            return jsonify(event.to_dict()), 201
        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        
@event.route('/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.get_json()
    name = data.get('name')
    date = data.get('date')
    location = data.get('location')
    description = data.get('description')
    try:
        event = event_service.update_event(event_id, name, date, location, description)
        return jsonify(event.to_dict())
    except ValueError as e:
        return jsonify({'message': str(e)}), 404

@event.route('/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    try:
        event = event_service.delete_event(event_id)
        return jsonify(event.to_dict())
    except ValueError as e:
        return jsonify({'message': str(e)}), 404
    
## Logica para los templates ##

events_templates = Blueprint('events_templates',__name__)

@events_templates.route('/')
@verificar_token
def events():
    events = event_service.get_all_events()
    if request.cookies.get('access_token'):
        return render_template('events_protected.html', events=events)
    else:
        return render_template('events.html', events= events)
