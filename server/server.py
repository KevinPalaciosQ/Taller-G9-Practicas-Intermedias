from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)
host = '0.0.0.0'
port = 3001

def load_users():
    if os.path.exists('users.json'):
        with open('users.json', 'r') as file:
            return json.load(file)
    return []

def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=2)

@app.route('/')
def home():
    return 'Taller, introducción a Raspberry Pi'

@app.route('/register', methods=['POST'])
def register():
    users = load_users()
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if any(user['username'] == username for user in users):
        print('El usuario ya existe')
        return jsonify({'message': 'El usuario ya existe'}), 400

    users.append({'username': username, 'password': password})
    save_users(users)
    print('Usuario registrado exitosamente')
    return jsonify({'message': 'Usuario registrado exitosamente'})

@app.route('/login', methods=['POST'])
def login():
    users = load_users()
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = next((user for user in users if user['username'] == username and user['password'] == password), None)

    if not user:
        print('Credenciales incorrectas')
        return jsonify({'message': 'Credenciales incorrectas'}), 401
    
    print('Login exitoso')
    return jsonify({'message': 'Login exitoso'})

if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)
    print('Servidor corriendo en http://{}:{}'.format(host, port))