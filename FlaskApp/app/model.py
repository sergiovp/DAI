from pickleshare import *

'''
    Para Pickleshare
'''

def start_db():
    data_base = PickleShareDB('usuarios_db')
    return data_base

# Variable global BD
data_base = start_db()

def check_key_exists(key):
    return (key in data_base.keys())

def check_password(user, password):
    return (password == data_base[user].get('password'))

def store_user(user, password):
    data_base[user] = {'password': password}

def delete_user(usuario):
    del data_base[usuario]

def update_user_pass(user, password):
    data_base[user] = {'password': password}

'''
    Para MongoDB
'''
import pymongo
from pymongo import MongoClient

client = MongoClient("mongo", 27017)
db = client.SampleCollections

def get_pokemon(query):
    return (db.samples_pokemon.find(query))

def get_coleccion_pokemon():
    coleccion = db.samples_pokemon.find()
    return coleccion

def eliminar_pokemon(pokemon):
    db.samples_pokemon.delete_one({"name": pokemon})

def modificar_pokemon(query, valor_nuevo):
    db.samples_pokemon.update_one(query, valor_nuevo)

def aniadir_pokemon(nuevo_pokemon):
    db.samples_pokemon.insert_one(nuevo_pokemon)

def eliminar_pokemon_query(query):
    db.samples_pokemon.delete_one(query)

def get_one_pokemon(query):
    return (db.samples_pokemon.find_one(query))
