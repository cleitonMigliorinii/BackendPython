from app import app, db, jsonify
from app.models.tables import Aluno
import json
from app.controller.encoderJson import AlchemyEncoder

def buscarTodosUsuarios():

     lista=  Aluno.query.order_by(Aluno.id).all()
   
     return json.dumps(lista, cls=AlchemyEncoder)

def deletarAluno(idUser):

    usuario =  Aluno.query.filter_by(id=idUser).first()

    db.session.delete(usuario)
    db.session.commit()

    return { "code": 200, "msg": "" }

def buscarAluno(idUser):

    return Aluno.query.filter_by(id=idUser).first()

def salvarUsuario(usuario):

    code = 200
    msg = ""

    try:

        if usuario.id:

            usuarioAntigo = buscarAluno(usuario.id)

            usuarioAntigo.name = usuario.name
            usuarioAntigo.username = usuario.username
            usuarioAntigo.email = usuario.email
            usuarioAntigo.password = usuario.password
        
        else:
            db.session.add(usuario)
        
        db.session.commit()

    except expression as identifier:
        code = 500
        msg =  "Erro ao gravar"

    return { "code": code, "msg": msg }