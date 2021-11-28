# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 17:02:49 2021

@author: maria
"""

from flask import Flask
import os
from jose import jwt
from flask import request

app = Flask(__name__)

@app.route("/")
def inicio():
    test = os.environ.get("Test")
    return test

@app.route("/crear-token")
def crear():
    nombre = request.args.get('nombre')
    id_persona = request.args.get('id')
    rolId = request.args.get('id_rol')
    try:
        secret_key = os.environ.get("JWT_SECRET_KEY")
        token = jwt.encode({'nombre': nombre , 'id': id_persona , 'rol': rolId }, secret_key , algorithm='HS256')
        return token
    except Exception as e:
        return 'Error al crear token'
    

@app.route("/validar-token")
def validar():
    token = request.args.get('token')
    rol = request.args.get('rol')
    try:
        secret_key = os.environ.get("JWT_SECRET_KEY")
        token= jwt.decode(token, secret_key, algorithms=['HS256'])
        if token["rol"] == rol:
            return "OK"
        else:
            "KO"
    except Exception as e:
        return ""
    

if __name__ =='__main__':
    app.run(host='localhost', port=5001)
