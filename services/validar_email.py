import re
from .limpar_cmd import limpar_cmd


def validar_email():
    while True:
        try:
            email = input("E-mail: ")
            padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(padrao, email):
                raise ValueError("E-mail inválido!")
            return email
        except Exception as e:
            limpar_cmd()
            print(f"{e}")
            continue
