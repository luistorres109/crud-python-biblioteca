from services.converter_data import converter_data
from config.database import conectar
from models.usuario import Usuario
import mysql.connector

db = conectar()
cursor = db.cursor()


class UsuarioRepository(Usuario):
    def __init__(self, id=None, nome=None, email=None, data_cad=None):
        super().__init__(id=id, nome=nome, email=email, data_cad=data_cad)

    @classmethod
    def get_by_id(cls, id):
        select = "SELECT id_usuario, nome, email, data_cadastro "
        sql = "FROM Usuario WHERE id_usuario=%s"
        cursor.execute(select + sql, (id,))
        result = cursor.fetchone()

        if result:
            return cls(*result)
        return None

    def create(self):
        insert = "INSERT INTO Usuario (nome, email, "
        sql = "data_cadastro) VALUES (%s, %s, %s)"
        cursor.execute(insert + sql, (self.nome, self.email, self.data_cad))
        db.commit()
        self.id = cursor.lastrowid

    def show(self):
        print(f"- ID: {self.id}")
        print(f"- Nome: {self.nome}")
        print(f"- E-mail: {self.email}")
        print(f"- Data de Cadastro: {converter_data(self.data_cad)}")

    def update(self):
        sql = "UPDATE Usuario SET nome=%s, email=%s, "
        update = "data_cadastro=%s WHERE id_usuario=%s"
        cursor.execute(sql + update, (self.nome, self.email,
                                      self.data_cad, self.id))
        db.commit()

    def delete(self):
        try:
            sql = "DELETE FROM Usuario WHERE id_usuario=%s"
            cursor.execute(sql, (self.id,))
            db.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Erro ao deletar tabela: {err}")
            return False
