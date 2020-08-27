#
# Pour executer ce serveur
# Ouvrir un 'Anaconda PowerShell Prompt'
# python C:\appli\gitRepository\medica1\server-python\server.py
#
from flask import Flask, jsonify
from flask_cors import CORS
from flask import request
from flask import abort
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# ------------------- Class User -------------------


class User:
    def __init__(self, id, username, password, displayName):
        self.id = id
        self.username = username
        self.password = password
        self.displayName = displayName


# ------------------- List des users -------------------
# ------------------- (Un jour sera une une base ou ldap) -------------------
users = [
    User(1, 'a', 'a', 'Aaaa Bbbb'),
    User(2, 'bdecamus', 'a', 'Bruno Decamus')
]


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return vars(obj)
        else:
            return json.JSONEncoder.default(self, obj)


@app.route('/api/v1.0/user', methods=['GET'])
def get_users():

    print("-------------------------------------------------------------")
    print("Entre dans GET /api/v1.0/users")
    username = request.headers.get('username')
    password = request.headers.get('password')
    print("Verifie si l'utilisateur suivant existe : username : ",
          username, " - password : ", password)

    for user in users:
        if user.username == username:
            if user.password == password:
                print("Ce user existe.")
                return jsonify(json.dumps(user, cls=MyEncoder))

    print("Ce user n'existe pas. On retourne une HTTP 401")
    abort(401)


if __name__ == '__main__':
    app.run(debug=True)
