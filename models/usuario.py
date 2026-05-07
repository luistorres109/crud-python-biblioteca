from config.database import conectar

db = conectar()
cursor = db.cursor()


class Usuario:
    def __init__(self, id=None, nome=None, email=None, data_cad=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.data_cad = data_cad
