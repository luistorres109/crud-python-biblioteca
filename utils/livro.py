from repositories.livro_repository import LivroRepository
from services.limpar_cmd import limpar_cmd


def use_livro():
    limpar_cmd()
    while True:
        print("===== MENU DE LIVRO =====")
        print("1 - Cadastrar livro")
        print("2 - Buscar livro por ID")
        print("3 - Voltar")
        opcao = input("Escolha: ")
        limpar_cmd()

        if opcao == '1':
            titulo = input("Título: ")
            id_autor = input("ID do Autor: ")
            ano_publicacao = int(input("Ano de Publicação: "))
            genero = input("Gênero: ")
            livro = LivroRepository(titulo=titulo, id_autor=id_autor,
                                    ano_publicacao=ano_publicacao,
                                    genero=genero)
            livro.create()
            limpar_cmd()

            print(f"Livro com ID: {livro.id}")
            input("\nENTER para continuar...")
        elif opcao == '2':
            try:
                id_livro = int(input("ID do livro: "))
            except ValueError:
                print("ID inválido.")
                input("\nENTER para continuar...")
                limpar_cmd()
                continue

            limpar_cmd()
            livro = LivroRepository.get_by_id(id_livro)

            if not livro:
                print("Livro não encontrado.")
                input("\nENTER para continuar...")
                limpar_cmd()
                continue

            while True:
                limpar_cmd()

                print("===== LIVRO =====")
                livro.show()

                print("\n1 - Atualizar")
                print("2 - Deletar")
                print("3 - Voltar")

                opcao2 = input("Escolha: ")
                limpar_cmd()

                if opcao2 == '1':
                    print("O que deseja atualizar?")
                    print("1 - Título ")
                    print("2 - ID do Autor")
                    print("3 - Ano de Publicação")
                    print("4 - Gênero")

                    campo = input("Escolha: ")

                    if campo == '1':
                        livro.titulo = input("Novo título: ")
                    elif campo == '2':
                        livro.id_autor = input("Novo ID do autor: ")
                    elif campo == '3':
                        livro.ano_publicacao = int(input("Novo ano "
                                                         "de publicação: "))
                    elif campo == '4':
                        livro.genero = input("Novo gênero: ")
                    else:
                        print("Valor inválido!")
                        input("\nENTER para continuar...")
                        limpar_cmd()
                        continue
                    livro.update()
                    limpar_cmd()
                    print("Atualizado com sucesso!")
                    input("ENTER para continuar...")
                elif opcao2 == '2':
                    confirm = input("Tem certeza? (s/n): ")

                    if confirm.lower() == 's':
                        delete_sucess = livro.delete()
                        if delete_sucess:
                            print("Livro deletado.")
                        input("ENTER para continuar...")
                        break
                elif opcao2 == '3':
                    break
                else:
                    print("Valor inválido!")
                    input("\nENTER para continuar...")
                    limpar_cmd()
                    continue
                limpar_cmd()
        elif opcao == '3':
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")
            input("ENTER para continuar...")
        limpar_cmd()
