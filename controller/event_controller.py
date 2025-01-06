from flask import Blueprint, jsonify, render_template, request
from controller.userlogin import verificar_token, verificar_token_directo
from controller.validator.event_validator import EventValidator
from database.db_connection import get_db_connection
from services.event_service import EventService

event = Blueprint('event', __name__)

event_service = EventService()

@event.route('', methods=['GET'])
def get_events():
    events = event_service.get_all_events()
    return jsonify([event for event in event_service.get_all_events()])

@event.route('/<int:event_id>', methods=['GET'])
def get_event(event_id):
    try:
        event = event_service.get_event(event_id)
        return jsonify(event)
    except ValueError as e:
        return jsonify({'message': str(e)}), 404
    
@event.route('', methods=['POST'])
def create_event():
        data = request.get_json()
        name = data.get('name')
        date = data.get('date')
        description = data.get('description')
        content = data.get('content')
        try:
            event_validate = EventValidator(name, date, description)
            event_validate.validate()
            event = event_service.create_event(name, date, description, content)
            return jsonify({'message': 'Event created successfully', 'Event': event}), 201
        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        
@event.route('/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.get_json()
    name = data.get('name')
    date = data.get('date')
    description = data.get('description')
    content = data.get('content')
    try:
        event_valudate = EventValidator(name, date, description)
        event_valudate.validate()
        event = event_service.update_event(event_id, name, date, description, content)
        return jsonify({'message': 'Event updated successfully', 'Event': event})
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
def events():
    events = event_service.get_all_events()
    token = request.cookies.get('access_token')  # Obtén el token de las cookies
    user = verificar_token_directo(token)  # Decodifica el token
    if user:  # Si el token es válido
        return render_template('events_protected.html', events=events, user=user)
    else:
        return render_template('events.html', events= events)
    
@events_templates.route('/detail')
def event_detail_query():
    # Obtener el parámetro `id` de la query string
    event_id = request.args.get('id', type=int)

    if not event_id:
        return "ID del evento no proporcionado", 400

    # Consultar los datos del evento
    event = event_service.get_event(event_id)
    if not event:
        return "Evento no encontrado", 404
    token = request.cookies.get('access_token')  # Obtén el token de las cookies
    user = verificar_token_directo(token)  # Decodifica el token
    if user:  # Si el token es válido
        return render_template('event_detail_protected.html', event=event, user=user)
    else:
        return render_template('event_detail.html', event=event)