from services.converter_data import converter_data
from .usuario_repository import UsuarioRepository
from .livro_repository import LivroRepository
from models.emprestimo import Emprestimo
from config.database import conectar
import mysql.connector

db = conectar()
cursor = db.cursor()


class EmprestimoRepository(Emprestimo):
    def __init__(self, id=None, id_livro=None, id_usuario=None,
                 data_emprestimo=None, data_devolucao=None):
        super().__init__(id=id, id_livro=id_livro, id_usuario=id_usuario,
                         data_emprestimo=data_emprestimo,
                         data_devolucao=data_devolucao)
        self.usuario = UsuarioRepository.get_by_id(self.id_usuario)
        self.livro = LivroRepository.get_by_id(self.id_livro)

    @classmethod
    def get_by_id(cls, id):
        select = "SELECT id_emprestimo, id_livro, id_usuario, "
        sql = "data_emprestimo, data_devolucao FROM "
        sql2 = "Emprestimo WHERE id_emprestimo=%s"
        cursor.execute(select + sql + sql2, (id,))
        result = cursor.fetchone()

        if result:
            return cls(*result)
        return None

    def create(self):
        try:
            insert = "INSERT INTO Emprestimo (id_livro, id_usuario, "
            sql = "data_emprestimo, data_devolucao) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert + sql, (self.id_livro, self.id_usuario,
                                          self.data_emprestimo,
                                          self.data_devolucao))
            db.commit()
            self.id = cursor.lastrowid
            return True
        except mysql.connector.Error as err:
            print(f"Erro ao deletar tabela: {err}")
            return False

    def show(self):
        print(f"- ID: {self.id}")
        print(f"- Livro: {self.livro.titulo}")
        print(f"- Usuario: {self.usuario.nome}")
        print(f"- Data de Emprestimo: {converter_data(self.data_emprestimo)}")
        print(f"- Data de Devolução: {converter_data(self.data_devolucao)}")

    def update(self):
        try:
            self.usuario = UsuarioRepository.get_by_id(self.id_usuario)
            self.livro = LivroRepository.get_by_id(self.id_livro)
            sql = "UPDATE Emprestimo SET id_livro=%s, id_usuario=%s, "
            update = "data_emprestimo=%s, data_devolucao=%s "
            "WHERE id_emprestimo=%s"
            cursor.execute(sql + update, (self.id_livro, self.id_usuario,
                                          self.data_emprestimo,
                                          self.data_devolucao, self.id))
            db.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Erro ao deletar tabela: {err}")
            return False

    def delete(self):
        sql = "DELETE FROM Emprestimo WHERE id_emprestimo=%s"
        cursor.execute(sql, (self.id,))
        db.commit()
