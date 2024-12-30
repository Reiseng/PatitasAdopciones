from flask import jsonify, render_template,Blueprint, request
from backend.database.db_connection import get_db_connection

events_bp = Blueprint('events_bp',__name__)
event_bp = Blueprint('event_bp',__name__)

@events_bp.route('')
def events():
    # Consultar todos los eventos desde la base de datos
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM eventos ORDER BY fecha DESC")
    events = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('events.html', events= events)

@events_bp.route('/')
def get_events():
    # Simulación de eventos desde una base de datos
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, nombre, fecha, descrpcion FROM eventos ORDER BY fecha ASC LIMIT 3")
    events = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(events)

@event_bp.route('')
def event_detail_query():
    # Obtener el parámetro `id` de la query string
    event_id = request.args.get('id', type=int)

    if not event_id:
        return "ID del evento no proporcionado", 400

     #Consultar los datos del evento
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM eventos WHERE id = %s", (event_id,))
    event = cursor.fetchone()
    cursor.close()
    connection.close()
    print(event)
    if not event:
        return "Evento no encontrado", 404
    
    return render_template('event_detail.html', event=event)
