from services.limpar_cmd import limpar_cmd
from .emprestimo import use_emprestimo
from .usuario import use_usuario
from .livro import use_livro
from .autor import use_autor


def menu():
    while True:
        limpar_cmd()
        print("===== MENU PRINCIPAL =====")
        print("Opções:")
        print("1 - Autor")
        print("2 - Usuário")
        print("3 - Livro")
        print("4 - Emprestimo")
        opcao = input("Digite aqui: ")
        if opcao == '1':
            use_autor()
        elif opcao == '2':
            use_usuario()
        elif opcao == '3':
            use_livro()
        elif opcao == '4':
            use_emprestimo()
        else:
            limpar_cmd()
            print("Opção inválida.\nPrograma encerrado!")
            input("Pressione qualquer tecla...")
            break
