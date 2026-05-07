from repositories.emprestimo_repository import EmprestimoRepository
from services.validar_data import input_data
from services.limpar_cmd import limpar_cmd


def use_emprestimo():
    limpar_cmd()
    while True:
        print("===== MENU DE EMPRÉSTIMO =====")
        print("1 - Cadastrar empréstimo")
        print("2 - Buscar empréstimo por ID")
        print("3 - Voltar")
        opcao = input("Escolha: ")
        limpar_cmd()

        if opcao == '1':
            id_livro = input("ID de livro: ")
            id_usuario = input("ID de usuário: ")
            data_emprestimo = input_data("Data de emprestimo: ")
            data_devolucao = input_data("Data de devolução: ")
            emprestimo = EmprestimoRepository(id_livro=id_livro,
                                              id_usuario=id_usuario,
                                              data_emprestimo=data_emprestimo,
                                              data_devolucao=data_devolucao)

            create_sucess = emprestimo.create()
            if create_sucess:
                print(f"Empréstimo criado com ID: {emprestimo.id}")
            input("\nENTER para continuar...")
            limpar_cmd()
        elif opcao == '2':
            try:
                id = int(input("ID do empréstimo: "))
            except ValueError:
                print("ID inválido.")
                input("\nENTER para continuar...")
                limpar_cmd()
                continue

            limpar_cmd()
            emprestimo = EmprestimoRepository.get_by_id(id)

            if not emprestimo:
                print("Empréstimo não encontrado.")
                input("\nENTER para continuar...")
                limpar_cmd()
                continue

            while True:
                limpar_cmd()

                print("===== EMPRÉSTIMO =====")
                emprestimo.show()

                print("\n1 - Atualizar")
                print("2 - Deletar")
                print("3 - Voltar")

                opcao2 = input("Escolha: ")
                limpar_cmd()

                if opcao2 == '1':
                    print("O que deseja atualizar?")
                    print("1 - ID de livro")
                    print("2 - ID de usuário")
                    print("3 - Data de emprestimo")
                    print("4 - Data de devolução")
                    campo = input("Escolha: ")

                    if campo == '1':
                        emprestimo.id_livro = input("ID de livro: ")
                    elif campo == '2':
                        emprestimo.id_usuario = input("Novo ID de usuário: ")
                    elif campo == '3':
                        emprestimo.data_emprestimo = input_data(
                            "Nova data de emprestimo: ")
                    elif campo == '4':
                        emprestimo.data_devolucao = input_data(
                            "Nova data de devolução: ")
                    else:
                        print("Valor inválido!")
                        input("\nENTER para continuar...")
                        limpar_cmd()
                        continue
                    update_sucess = emprestimo.update()
                    limpar_cmd()
                    if update_sucess:
                        print("Atualizado com sucesso!")
                    input("ENTER para continuar...")
                elif opcao2 == '2':
                    confirm = input("Tem certeza? (s/n): ")

                    if confirm.lower() == 's':
                        emprestimo.delete()
                        print("Empréstimo deletado.")
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
