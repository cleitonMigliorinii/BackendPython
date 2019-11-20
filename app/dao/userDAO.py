from app import app, db, jsonify
from app.models.user import User
import json

columns = ('id','username', 'email', 'password', 'name' )


def buscarTodosUsuarios():

     print(User.query.order_by(User.id).all())
     return 'ok'

def salvarUsuario(usuario):

    db.session.add(usuario)
    db.session.commit()