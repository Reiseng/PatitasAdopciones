from flask import Blueprint, jsonify, request
from persistence.company_persistence import (buscarEmpresa,actualizarEmpresa)

company_bp = Blueprint('company',__name__)

@company_bp.route('/', methods=['GET'])
def get_empresa():
    empresa = buscarEmpresa()  # Llamas a la función para obtener la empresa
    if empresa:
        return jsonify(empresa.to_dict()), 200  # Devuelves los datos como JSON con código 200 (éxito)
    else:
        return jsonify({'error': 'Empresa no encontrada'}), 404  # Manejas el caso en que no se encuentra la empresa
    
@company_bp.route('/', methods=['PUT'])
def update_empresa():
    data = request.get_json()
    empresa = buscarEmpresa()  # Llamas a la función para obtener la empresa
    if empresa:
        empresa.nombre = data.get('nombre', empresa.nombre)
        empresa.mail = data.get('mail', empresa.mail)
        empresa.telefono = data.get('telefono', empresa.telefono)
        empresa.facebook = data.get('facebook', empresa.facebook)
        empresa.instagram = data.get('instagram', empresa.instagram)
        empresa.twitter = data.get('twitter', empresa.twitter)
    actualizarEmpresa(empresa)  # Llamas a la función para actualizar la empresa