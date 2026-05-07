from repositories.autor_repository import AutorRepository
from services.limpar_cmd import limpar_cmd


def use_autor():
    limpar_cmd()
    while True:
        print("===== MENU DE AUTOR =====")
        print("1 - Cadastrar autor")
        print("2 - Buscar autor por ID")
        print("3 - Voltar")

        opcao = input("Escolha: ")
        limpar_cmd()

        if opcao == '1':
            nome = input("Nome: ")
            nacionalidade = input("Nacionalidade: ")

            autor = AutorRepository(nome=nome, nacionalidade=nacionalidade)
            autor.create()

            print(f"\nAutor criado com ID: {autor.id}")
            input("\nENTER para continuar...")
        elif opcao == '2':
            try:
                id_autor = int(input("ID do autor: "))
            except ValueError:
                print("ID inválido.")
                input("\nENTER para continuar...")
                limpar_cmd()
                continue

            limpar_cmd()
            autor = AutorRepository.get_by_id(id_autor)

            if not autor:
                print("Autor não encontrado.")
                input("\nENTER para continuar...")
                limpar_cmd()
                continue

            while True:
                limpar_cmd()

                print("===== AUTOR =====")
                autor.show()

                print("\n1 - Atualizar")
                print("2 - Deletar")
                print("3 - Voltar")

                opcao2 = input("Escolha: ")
                limpar_cmd()

                if opcao2 == '1':
                    print("\nO que deseja atualizar?")
                    print("1 - Nome")
                    print("2 - Nacionalidade")

                    campo = input("Escolha: ")

                    if campo == '1':
                        autor.nome = input("Novo nome: ")
                    elif campo == '2':
                        autor.nacionalidade = input("Nova nacionalidade: ")
                    autor.update()
                    limpar_cmd()
                    print("\nAtualizado com sucesso!")
                    input("ENTER para continuar...")
                elif opcao2 == '2':
                    confirm = input("Tem certeza? (s/n): ")

                    if confirm.lower() == 's':
                        delete_sucess = autor.delete()
                        if delete_sucess:
                            print("Autor deletado.")
                        input("ENTER para continuar...")
                        break
                else:
                    break
                limpar_cmd()
        elif opcao == '3':
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")
            input("ENTER para continuar...")
        limpar_cmd()
