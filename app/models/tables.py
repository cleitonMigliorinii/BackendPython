from app import db

class Turma(db.Model):

    __tablename__ = 'turmas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, nome):
        self.nome = nome
     
    def __repr__(self):
        return '<Turma %r>' % self.nome


class Aluno(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String)
    name = db.Column(db.String)

    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'))
    turma = db.relationship('Turma',foreign_keys=turma_id)

    def __init__(self, username, email,password,name,turma_id,id):
        self.username = username
        self.email = email
        self.password = password
        self.name = name
        self.id = id
        self.turma_id = turma_id

    def __repr__(self):
        return '<Aluno %r>' % self.username