from .autor_repository import AutorRepository
from config.database import conectar
from models.livro import Livro
import mysql.connector

db = conectar()
cursor = db.cursor()


class LivroRepository(Livro):
    def __init__(self, id=None, titulo=None, id_autor=None,
                 ano_publicacao=None, genero=None):
        super().__init__(id=id, titulo=titulo, id_autor=id_autor,
                         ano_publicacao=ano_publicacao, genero=genero)
        self.autor = AutorRepository.get_by_id(self.id_autor)

    @classmethod
    def get_by_id(cls, id):
        select = "SELECT id_livro, titulo, id_autor, ano_publicacao, "
        sql = "genero FROM Livro WHERE id_livro=%s"
        cursor.execute(select + sql, (id,))
        result = cursor.fetchone()

        if result:
            return cls(*result)
        return None

    def create(self):
        insert = "INSERT INTO Livro (titulo, id_autor, "
        sql = "ano_publicacao, genero) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert + sql, (self.titulo, self.id_autor,
                                      self.ano_publicacao, self.genero))
        db.commit()
        self.id = cursor.lastrowid

    def show(self):
        print(f"- ID: {self.id}")
        print(f"- Título: {self.titulo}")
        print(f"- Autor: {self.autor.nome}")
        print(f"- Ano de Publicação: {self.ano_publicacao}")
        print(f"- Gênero: {self.genero}")

    def update(self):
        self.autor = AutorRepository.get_by_id(self.id_autor)
        sql = "UPDATE Livro SET titulo=%s, id_autor=%s, "
        update = "ano_publicacao=%s, genero=%s WHERE id_livro=%s"
        cursor.execute(sql + update, (self.titulo, self.id_autor,
                                      self.ano_publicacao, self.genero,
                                      self.id))
        db.commit()

    def delete(self):
        try:
            sql = "DELETE FROM Livro WHERE id_livro=%s"
            cursor.execute(sql, (self.id,))
            db.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Erro ao deletar tabela: {err}")
            return False
