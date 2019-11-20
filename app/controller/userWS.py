from app import app,request
from app.dao import userDAO
from app.models.user import User

@app.route("/buscarTodosUsuarios", methods=['POST'])
def buscarTodosUsuarios():
    return userDAO.buscarTodosUsuarios()


@app.route("/salvarUsuario", methods=['POST'])
def salvarUsuario():
    obj = request.get_json()
    
    user = User(obj.get('username'), obj.get('email'), obj.get('password'), obj.get('name'))

    return userDAO.salvarUsuario(user)
