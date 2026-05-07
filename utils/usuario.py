from repositories.usuario_repository import UsuarioRepository
from services.validar_email import validar_email
from services.validar_nome import validar_nome
from services.limpar_cmd import limpar_cmd
from datetime import date


def use_usuario():
    limpar_cmd()
    while True:
        print("===== MENU DE USUÁRIO =====")
        print("1 - Cadastrar usuário")
        print("2 - Buscar usuário por ID")
        print("3 - Voltar")
        opcao = input("Escolha: ")
        limpar_cmd()

        if opcao == '1':
            nome = validar_nome()
            email = validar_email()
            usuario = UsuarioRepository(nome=nome, email=email,
                                        data_cad=date.today())
            usuario.create()
            limpar_cmd()

            print(f"Usuário criado com ID: {usuario.id}")
            input("\nENTER para continuar...")
        elif opcao == '2':
            try:
                id_usuario = int(input("ID do usuário: "))
            except ValueError:
                print("ID inválido.")
                input("\nENTER para continuar...")
                limpar_cmd()
                continue

            limpar_cmd()
            usuario = UsuarioRepository.get_by_id(id_usuario)

            if not usuario:
                print("Usuário não encontrado.")
                input("\nENTER para continuar...")
                limpar_cmd()
                continue

            while True:
                limpar_cmd()

                print("===== USUÁRIO =====")
                usuario.show()

                print("\n1 - Atualizar")
                print("2 - Deletar")
                print("3 - Voltar")

                opcao2 = input("Escolha: ")
                limpar_cmd()

                if opcao2 == '1':
                    print("O que deseja atualizar?")
                    print("1 - Nome")
                    print("2 - E-mail")

                    campo = input("Escolha: ")

                    if campo == '1':
                        usuario.nome = input("Novo nome: ")
                    elif campo == '2':
                        usuario.email = input("Novo e-mail: ")
                    else:
                        print("Valor inválido!")
                        input("\nENTER para continuar...")
                        limpar_cmd()
                        continue
                    usuario.update()
                    limpar_cmd()
                    print("Atualizado com sucesso!")
                    input("ENTER para continuar...")
                elif opcao2 == '2':
                    confirm = input("Tem certeza? (s/n): ")

                    if confirm.lower() == 's':
                        delete_sucess = usuario.delete()
                        if delete_sucess:
                            print("Usuário deletado.")
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
