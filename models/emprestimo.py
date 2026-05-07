from config.database import conectar

db = conectar()
cursor = db.cursor()


class Emprestimo:
    def __init__(self, id=None, id_livro=None, id_usuario=None,
                 data_emprestimo=None, data_devolucao=None):
        self.id = id
        self.id_livro = id_livro
        self.id_usuario = id_usuario
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
