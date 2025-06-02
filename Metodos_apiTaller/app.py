from Flask import Flask, request, jsonify

app = Flask(__name__)

# Simulamos un usuario de ejemplo
usuario = {"id": 1, "nombre": "Nicolás", "email": "nico@mail.com"}

# Ruta base
@app.route('/')
def home():
    return "¡API en Flask funcionando!"

# GET: obtener usuario
@app.route('/usuario', methods=['GET'])
def get_usuario():
    return jsonify(usuario)

# POST: crear usuario
@app.route('/usuario', methods=['POST'])
def post_usuario():
    global usuario
    usuario = request.json
    return jsonify({"mensaje": "Usuario creado", "datos": usuario}), 201

# PUT: reemplazar usuario
@app.route('/usuario', methods=['PUT'])
def put_usuario():
    global usuario
    usuario = request.json
    return jsonify({"mensaje": "Usuario reemplazado", "datos": usuario})

# PATCH: actualizar parcialmente usuario
@app.route('/usuario', methods=['PATCH'])
def patch_usuario():
    global usuario
    usuario.update(request.json)
    return jsonify({"mensaje": "Usuario actualizado parcialmente", "datos": usuario})

# DELETE: eliminar usuario
@app.route('/usuario', methods=['DELETE'])
def delete_usuario():
    global usuario
    usuario = {}
    return jsonify({"mensaje": "Usuario eliminado"})

# HEAD: cabecera
@app.route('/usuario', methods=['HEAD'])
def head_usuario():
    return ('', 200)

# OPTIONS: métodos disponibles
@app.route('/usuario', methods=['OPTIONS'])
def options_usuario():
    return ('', 200, {'Allow': 'GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS'})

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
