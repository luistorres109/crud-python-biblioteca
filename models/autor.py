from config.database import conectar

db = conectar()
cursor = db.cursor()


class Autor:
    def __init__(self, id=None, nome=None, nacionalidade=None):
        self.id = id
        self.nome = nome
        self.nacionalidade = nacionalidade
