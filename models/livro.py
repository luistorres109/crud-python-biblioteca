from config.database import conectar

db = conectar()
cursor = db.cursor()


class Livro:
    def __init__(self, id=None, titulo=None, id_autor=None,
                 ano_publicacao=None, genero=None):
        self.id = id
        self.titulo = titulo
        self.id_autor = id_autor
        self.ano_publicacao = ano_publicacao
        self.genero = genero
