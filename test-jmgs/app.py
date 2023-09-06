from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import ObjectId
import bcrypt

app = Flask(__name__)

# Configura la conexión a MongoDB
app.config['MONGO_URI'] = 'mongodb://localhost:27017/tienda'
mongo = PyMongo(app)

# Ruta para el inicio de sesión
@app.route('/api/login', methods=['POST'])
def login():
    # Obtiene los datos de inicio de sesión del cuerpo de la solicitud
    data = request.get_json()
    nombre_usuario = data.get('nombreUsuario')
    contrasena = data.get('contrasena')

    # Busca el usuario en la base de datos por nombre de usuario
    usuario = mongo.db.usuarios.find_one({'nombre': nombre_usuario})

    if usuario:
        # Verifica la contraseña almacenada en la base de datos
        if bcrypt.checkpw(contrasena.encode('utf-8'), usuario['contrasena']):
            return jsonify({'authenticated': True, 'usuario': nombre_usuario})
    
    return jsonify({'authenticated': False, 'usuario': None})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import ObjectId
import bcrypt

app = Flask(__name__)

# Configura la conexión a MongoDB
app.config['MONGO_URI'] = 'mongodb://localhost:27017/tienda'
mongo = PyMongo(app)

# Ruta para el inicio de sesión
@app.route('/api/login', methods=['POST'])
def login():
    # Obtiene los datos de inicio de sesión del cuerpo de la solicitud
    data = request.get_json()
    nombre_usuario = data.get('_id')
    contrasena = data.get('contraseña')

    # Busca el usuario en la base de datos por nombre de usuario
    usuario = mongo.db.usuarios.find_one({'_id': nombre_usuario})

    if usuario:
        # Verifica la contraseña almacenada en la base de datos
        if bcrypt.checkpw(contrasena.encode('utf-8'), usuario['contraseña']):
            return jsonify({'authenticated': True, 'usuario': nombre_usuario})
    
    return jsonify({'authenticated': False, 'usuario': None})

if __name__ == '__main__':
    app.run(debug=True)
