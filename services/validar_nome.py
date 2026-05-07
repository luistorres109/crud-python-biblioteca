from .limpar_cmd import limpar_cmd


def validar_nome():
    while True:
        try:
            nome = input("Nome: ")
            if not nome.strip():
                raise ValueError("Nome inválido!")
            return nome
        except Exception as e:
            limpar_cmd()
            print(f"{e}")
            continue
