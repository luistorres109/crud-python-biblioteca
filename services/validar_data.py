import msvcrt
from datetime import datetime
from .limpar_cmd import limpar_cmd


def validar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def input_data(string):
    while True:
        data = ""

        print(f"{string}", end="", flush=True)

        while True:
            tecla = msvcrt.getch()

            if tecla == b'\r':
                break

            elif tecla == b'\x08':
                if len(data) > 0:
                    if data[-1] == "/":
                        data = data[:-1]
                        print("\b \b", end="", flush=True)

                    data = data[:-1]
                    print("\b \b", end="", flush=True)

            elif tecla.isdigit() and len(data) < 10:
                if len(data) in [2, 5]:
                    data += "/"
                    print("/", end="", flush=True)

                data += tecla.decode()
                print(tecla.decode(), end="", flush=True)

        print()

        if validar_data(data):
            return datetime.strptime(data, '%d/%m/%Y').date()

        limpar_cmd()
        print("Data inválida. Tente novamente.\n")
