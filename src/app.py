"""
Este módulo se encarga de iniciar el servidor API, cargar la base de datos y agregar los endpoints.
#https://www.youtube.com/watch?v=_6Fmuw-lGNk&t=2205s video con la explicacion 🤯
"""

import os  # Importa el módulo os para trabajar con funcionalidades dependientes del sistema operativo
from flask import Flask, request, jsonify, url_for  # Importa las clases necesarias de Flask para construir la API
from flask_cors import CORS  # Importa CORS para permitir solicitudes de diferentes orígenes
from utils import APIException, generate_sitemap  # Importa las funciones auxiliares
from datastructures import FamilyStructure  # Importa la clase FamilyStructure del módulo datastructures
# from models import Person  # Importa el modelo de datos de Persona si es necesario

app = Flask(__name__)  # Crea una instancia de la aplicación Flask con el nombre del módulo actual
app.url_map.strict_slashes = False  # Configura Flask para que las rutas no requieran una barra al final
CORS(app)  # Configura CORS para permitir solicitudes de cualquier origen

# Crea una instancia de la estructura de datos de la familia Jackson
jackson_family = FamilyStructure("Jackson")

# Maneja y serializa errores como un objeto JSON
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code  # Retorna el error como un JSON con el código de estado correspondiente

# Genera el sitemap con todos los endpoints disponibles en la aplicación
@app.route('/')
def sitemap():
    return generate_sitemap(app)  # Utiliza la función generate_sitemap del módulo utils para generar el sitemap

#----------------------------------------------------------GET ALL----------------------------------------------------------------#

# Endpoint para obtener todos los miembros de la familia
@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()  # Obtiene todos los miembros de la familia
    if not members:
        return jsonify({"done": False, "msg":"Error al obtener el miembro"}), 400  # Retorna un mensaje de error si falla con el código de estado 400, "done" es una convención que se utiliza comúnmente para indicar que una tarea o una operación se ha completado o realizado con éxito
    return jsonify(members), 200  # Retorna el miembro si tiene éxito con el código de estado 200


#-----------------------------------------------------------POST---------------------------------------------------------------#

# Endpoint para agregar un nuevo miembro a la familia
@app.route('/member', methods=['POST'])
def add_member():
    new_member = request.json  # Obtiene los datos del nuevo miembro desde la solicitud HTTP
    jackson_family.add_member(new_member)  # Agrega el nuevo miembro a la familia
    return jsonify({"done": True, "msg": "Usuario creado satisfactoriamente"}), 200  # Retorna un mensaje de éxito como JSON con el código de estado 200, "done" es una convención que se utiliza comúnmente para indicar que una tarea o una operación se ha completado o realizado con éxito
                                                                                     
#-----------------------------------------------------------DELETE---------------------------------------------------------------#

# Endpoint para eliminar un miembro de la familia según su ID
@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    eliminar_miembro = jackson_family.delete_member(member_id)  # Elimina el miembro de la familia
    if not eliminar_miembro:
        return jsonify({"done": False, "msg":"Error al eliminar el miembro"}), 400  # Retorna un mensaje de error si falla con el código de estado 400
    return jsonify({"done": True, "msg":"Se ha eliminado satisfactoriamente"}), 200  # Retorna un mensaje de éxito si tiene éxito con el código de estado 200, "done" es una convención que se utiliza comúnmente para indicar que una tarea o una operación se ha completado o realizado con éxito

#--------------------------------------------------------PUT------------------------------------------------------------------#

# Endpoint para actualizar un miembro de la familia según su ID
@app.route('/member/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    new_member = request.json  # Obtiene los datos del miembro actualizado desde la solicitud HTTP
    update_member = jackson_family.update_member(member_id, new_member)  # Actualiza el miembro de la familia
    if not update_member:
        return jsonify({"done": False, "msg":"Error al actualizar el miembro"}), 400  # Retorna un mensaje de error si falla con el código de estado 400
    return jsonify({"done": True, "msg":"Se ha actualizado satisfactoriamente"}), 200  # Retorna un mensaje de éxito si tiene éxito con el código de estado 200, "done" es una convención que se utiliza comúnmente para indicar que una tarea o una operación se ha completado o realizado con éxito

#------------------------------------------------------GET ONE--------------------------------------------------------------------#

# Endpoint para obtener un miembro de la familia según su ID
@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    miembro_buscado = jackson_family.get_member(member_id)  # Busca el miembro en la familia
    if not miembro_buscado:
        return jsonify({"done": False, "msg":"Error al obtener el miembro"}), 400  # Retorna un mensaje de error si falla con el código de estado 400
    return jsonify(miembro_buscado), 200  # Retorna el miembro si tiene éxito con el código de estado 200


#--------------------------------------------------------------------------------------------------------------------------#

# Este bloque se ejecuta solo si este script es ejecutado directamente
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))  # Obtiene el número de puerto del entorno, predeterminado es 3000
    app.run(host='0.0.0.0', port=PORT, debug=True)  # Inicia la aplicación Flask en el host y puerto especificados con modo de depuración activado
