from pickleshare import *

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
