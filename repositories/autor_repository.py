from config.database import conectar
from models.autor import Autor
import mysql.connector

db = conectar()
cursor = db.cursor()


class AutorRepository(Autor):
    def __init__(self, id=None, nome=None, nacionalidade=None):
        super().__init__(id=id, nome=nome, nacionalidade=nacionalidade)

    @classmethod
    def get_by_id(cls, id):
        select = "SELECT id_autor, nome, nacionalidade "
        sql = "FROM Autor WHERE id_autor=%s"
        cursor.execute(select + sql, (id,))
        result = cursor.fetchone()

        if result:
            return cls(*result)
        return None

    def create(self):
        sql = "INSERT INTO Autor (nome, nacionalidade) VALUES (%s, %s)"
        cursor.execute(sql, (self.nome, self.nacionalidade))
        db.commit()
        self.id = cursor.lastrowid

    def show(self):
        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Nacionalidade: {self.nacionalidade}")

    def update(self):
        sql = "UPDATE Autor SET nome=%s, nacionalidade=%s WHERE id_autor=%s"
        cursor.execute(sql, (self.nome, self.nacionalidade, self.id))
        db.commit()

    def delete(self):
        try:
            sql = "DELETE FROM Autor WHERE id_autor=%s"
            cursor.execute(sql, (self.id,))
            db.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Erro ao deletar tabela: {err}")
            return False
