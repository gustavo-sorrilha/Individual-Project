##import cx_Oracle

from Usuario import Usuario
from Funcoes import Funcoes
from Produto import Produto

class Restaurante(Usuario):
    def __init__(self, id_usuario=None, cnpj_usuario=None, nome_usuario=None, email_usuario=None):
        super().__init__(id_usuario=id_usuario, cnpj_usuario=cnpj_usuario, nome_usuario=nome_usuario, email_usuario=email_usuario)

    def cadastrarRestaurante(dsn, dicRestaurantes, id_usuario):
        # INSTANCIANDO NOVO RESTAURANTE - OK
        novo_restaurante = Restaurante()
        
        Funcoes.menuCabecalho

        # SETANDO ID DO USUÁRIO - OK
        id_usuario = id_usuario

        # SETANDO CPF DO USUÁRIO - OK
        cpf_usuario = input("DIGITE O SEU CNPJ (APENAS NÚMEROS, EXEMPLO: 12345678000200): ")
        while (Funcoes.validarCNPJ(cnpj_usuario) == False or cnpj_usuario in [restaurante.cnpj_usuario for restaurante in dicRestaurantes.values()]):
            print("CNPJ INVÁLIDO OU JÁ CADASTRADO.")
            cnpj_usuario = input("DIGITE O SEU CNPJ (APENAS NÚMEROS, EXEMPLO: 12345678000200): ")

        # SETANDO NOME DO USUÁRIO - OK
        nome_usuario = input("DIGITE O NOME DO RESTAURANTE COMPLETO: ")
        nome_usuario = Funcoes.validarPreenchimento("DIGITE O NOME DO RESTAURANTE COMPLETO: ", nome_usuario)

        # SETANDO EMAIL DO USUÁRIO - OK
        email_usuario = input("DIGITE O SEU EMAIL: ")
        email_usuario = Funcoes.validarPreenchimento("DIGITE O SEU EMAIL: ", email_usuario)
        while (email_usuario in [restaurante.email_usuario for restaurante in dicRestaurantes.values()]):
            print("EMAIL INVÁLIDO OU JÁ CADASTRADO.")
            email_usuario = input("DIGITE O SEU EMAIL: ")

        print("------------------------------------------")

        # ADICIONANDO O RESTAURANTE NO DICIONÁRIO DE RESTAURANTES - 
        novo_restaurante = Restaurante(id_usuario = id_usuario, cpf_usuario = cpf_usuario, nome_usuario = nome_usuario, email_usuario = email_usuario)
        dicRestaurantes[novo_restaurante.id_usuario] = novo_restaurante

         # CRIANDO CONEXÃO COM O BANCO DE DADOS
        ##conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        ##cursor = conn.cursor()
        ##Funcoes.connect(dsn)

        # CADASTRANDO NO BANCO DE DADOS
        ##cursor.execute("INSERT INTO usuario (id_usuario, cpf_usuario, nome_usuario, email_usuario) VALUES (:1, :2, :3, :4)", (novo_restaurante.id_usuario, novo_restaurante.cpf_usuario, novo_restaurante.nome_usuario, novo_restaurante.email_usuario))
        ##cursor.execute("INSERT INTO restaurante (id_usuario) VALUES (:1)", (novo_restaurante.id_usuario,))
        ##cursor.connection.commit()

         # FECHANDO CONEXÃO COM O BANCO DE DADOS
        ##Funcoes.disconnect(conn, cursor)

        print("RESTAURANTE CADASTRADO COM SUCESSO!")
        input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")
    
    def editarRestaurante(self, dsn, dicRestaurantes, emails_cadastrados, Aluno):
        perfilRestaurante = 1
        Funcoes.exibirUsuariosAdmin(dicRestaurantes)
        id_buscado = int(input("DIGITE O ID DO RESTAURANTE QUE DESEJA EDITAR: \n"))
        restaurante_buscado = Funcoes.buscarPorIdUsuario(id_buscado, dicRestaurantes)
        restaurante_buscado = Funcoes.validarUsuarioBuscado(restaurante_buscado, dicRestaurantes)

        while (perfilRestaurante == 1):
            opcao = int(input(Restaurante.perfilRestaurante(restaurante_buscado)))
            opcao = Funcoes.validarOpcao(opcao, 1, 5, Restaurante.perfilRestaurante(restaurante_buscado))

            if (opcao == 1):
                # (ADMIN) EDITAR ID DO RESTAURANTE  - OK
                input(Funcoes.editarNegativo())

            elif (opcao == 2):
                # (ADMIN) EDITAR O CNPJ DO RESTAURANTE - OK
                input(Funcoes.editarNegativo())
            
            elif (opcao == 3):
                # (ADMIN) EDITAR O NOME DO RESTAURANTE - OK
                opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O NOME DO RESTAURANTE {restaurante_buscado.nome_usuario}")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O NOME DO RESTAURANTE {restaurante_buscado.nome_usuario}")))
                
                if (opcao == 1):
                    # (ADMIN) EDITAR O NOME DO RESTAURANTE - SIM - OK
                    Funcoes.editarNome(dsn, restaurante_buscado)
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 2):
                    # (ADMIN) EDITAR O NOME DO RESTAURANTE - NÃO - OK
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
            
            elif (opcao == 4):
                # (ADMIN) EDITAR O EMAIL DO RESTAURANTE - OK
                opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O EMAIL DO RESTAURANTE {restaurante_buscado.nome_usuario}")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O EMAIL DO RESTAURANTE {restaurante_buscado.nome_usuario}")))
                
                if (opcao == 1):
                    # (ADMIN) EDITAR O EMAIL DO RESTAURANTE - SIM - OK
                    Funcoes.editarEmail(dsn, restaurante_buscado, emails_cadastrados, Aluno)
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 2):
                    # (ADMIN) EDITAR O EMAIL DO RESTAURANTE - NÃO - OK
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
            
            elif (opcao == 5):
            # (ADMIN) CADASTRAR/EDITAR PRODUTO
                opcao_produto = int(input("1 - Cadastrar novo prato\n2 - Editar prato existente\nEscolha uma opção: "))
                if opcao_produto == 1:
                    restaurante_buscado.cadastrarProduto(dsn, dicProduto)
                elif opcao_produto == 2:
                    restaurante_buscado.editarProduto(dsn, dicProduto)
                else:
                    print("Opção inválida.")
            elif (opcao == 6):
                # (ADMIN) SAIR DO MENU EDITAR RESTAURANTE - 
                perfilRestaurante = 0

    def perfilRestaurante(restaurante_buscado):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {restaurante_buscado.id_usuario}\n"
        retornoPerfil += f"02. CNPJ: {Funcoes.formatarCpf(restaurante_buscado.cpf_usuario)}\n"
        retornoPerfil += f"03. NOME: {restaurante_buscado.nome_usuario}\n"
        retornoPerfil += f"04. EMAIL: {restaurante_buscado.email_usuario}\n"
        retornoPerfil += f"05. PRODUTO: {restaurante_buscado.produto_usuario}\n"
        retornoPerfil += "05. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil