##import cx_Oracle

from Usuario import Usuario
from Funcoes import Funcoes
from Produto import Produto

class Mercado(Usuario):
    def __init__(self, id_usuario=None, cnpj_usuario=None, nome_usuario=None, email_usuario=None):
        super().__init__(id_usuario=id_usuario, cnpj_usuario=cnpj_usuario, nome_usuario=nome_usuario, email_usuario=email_usuario)

    def cadastrarMercado(dsn, dicMercados, id_usuario):
        # INSTANCIANDO NOVO MERCADO - OK
        novo_mercado = Mercado()
        
        Funcoes.menuCabecalho

        # SETANDO ID DO USUÁRIO - OK
        id_usuario = id_usuario

        # SETANDO CNPJ DO USUÁRIO - 
        cnpj_usuario = input("DIGITE O SEU CNPJ (APENAS NÚMEROS, EXEMPLO: 12345678000200): ")
        while (Funcoes.validarCNPJ(cnpj_usuario) == False or cnpj_usuario in [mercado.cnpj_usuario for mercado in dicMercados.values()]):
            print("CNPJ INVÁLIDO OU JÁ CADASTRADO.")
            cnpj_usuario = input("DIGITE O SEU CNPJ (APENAS NÚMEROS, EXEMPLO: 12345678000200): ")

        # SETANDO NOME DO USUÁRIO - OK
        nome_usuario = input("DIGITE O NOME DO MERCADO COMPLETO: ")
        nome_usuario = Funcoes.validarPreenchimento("DIGITE O NOME DO MERCADO COMPLETO: ", nome_usuario)

        # SETANDO EMAIL DO USUÁRIO - OK
        email_usuario = input("DIGITE O SEU EMAIL: ")
        email_usuario = Funcoes.validarPreenchimento("DIGITE O SEU EMAIL: ", email_usuario)
        while (email_usuario in [mercado.email_usuario for mercado in dicMercados.values()]):
            print("EMAIL INVÁLIDO OU JÁ CADASTRADO.")
            email_usuario = input("DIGITE O SEU EMAIL: ")

        print("------------------------------------------")

        # ADICIONANDO O MERCADO NO DICIONÁRIO DE MERCADOS - 
        novo_mercado = Mercado(id_usuario = id_usuario, cnpj_usuario = cnpj_usuario, nome_usuario = nome_usuario, email_usuario = email_usuario)
        dicMercados[novo_mercado.id_usuario] = novo_mercado

         # CRIANDO CONEXÃO COM O BANCO DE DADOS
        ##conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        ##cursor = conn.cursor()
        ##Funcoes.connect(dsn)

        # CADASTRANDO NO BANCO DE DADOS
        ##cursor.execute("INSERT INTO usuario (id_usuario, cnpj_usuario, nome_usuario, email_usuario) VALUES (:1, :2, :3, :4)", (novo_mercado.id_usuario, novo_mercado.cnpj_usuario, novo_mercado.nome_usuario, novo_mercado.email_usuario))
        ##cursor.execute("INSERT INTO mercado (id_usuario) VALUES (:1)", (novo_mercado.id_usuario,))
        ##cursor.connection.commit()

         # FECHANDO CONEXÃO COM O BANCO DE DADOS
        ##Funcoes.disconnect(conn, cursor)

        print("MERCADO CADASTRADO COM SUCESSO!")
        input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")
    
    def editarMercado(self, dsn, dicMercados, emails_cadastrados, Aluno):
        perfilMercado = 1
        Funcoes.exibirUsuariosAdmin(dicMercados)
        id_buscado = int(input("DIGITE O ID DO MERCADO QUE DESEJA EDITAR: \n"))
        mercado_buscado = Funcoes.buscarPorIdUsuario(id_buscado, dicMercados)
        mercado_buscado = Funcoes.validarUsuarioBuscado(mercado_buscado, dicMercados)

        while (perfilMercado == 1):
            opcao = int(input(Mercado.perfilMercado(mercado_buscado)))
            opcao = Funcoes.validarOpcao(opcao, 1, 5, Mercado.perfilMercado(mercado_buscado))

            if (opcao == 1):
                # (ADMIN) EDITAR ID DO MERCADO  - OK
                input(Funcoes.editarNegativo())

            elif (opcao == 2):
                # (ADMIN) EDITAR O CNPJ DO MERCADO - OK
                input(Funcoes.editarNegativo())
            
            elif (opcao == 3):
                # (ADMIN) EDITAR O NOME DO MERCADO - OK
                opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O NOME DO MERCADO {mercado_buscado.nome_usuario}")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O NOME DO MERCADO {mercado_buscado.nome_usuario}")))
                
                if (opcao == 1):
                    # (ADMIN) EDITAR O NOME DO MERCADO - SIM - OK
                    Funcoes.editarNome(dsn, mercado_buscado)
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 2):
                    # (ADMIN) EDITAR O NOME DO MERCADO - NÃO - OK
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
            
            elif (opcao == 4):
                # (ADMIN) EDITAR O EMAIL DO MERCADO - OK
                opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O EMAIL DO MERCADO {mercado_buscado.nome_usuario}")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O EMAIL DO MERCADO {mercado_buscado.nome_usuario}")))
                
                if (opcao == 1):
                    # (ADMIN) EDITAR O EMAIL DO MERCADO - SIM - OK
                    Funcoes.editarEmail(dsn, mercado_buscado, emails_cadastrados, Aluno)
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 2):
                    # (ADMIN) EDITAR O EMAIL DO MERCADO - NÃO - OK
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
            
            elif (opcao == 5):
            # (ADMIN) CADASTRAR/EDITAR PRODUTO
                opcao_produto = int(input("1 - Cadastrar novo produto\n2 - Editar produto existente\nEscolha uma opção: "))
                if opcao_produto == 1:
                    mercado_buscado.cadastrarProduto(dsn, dicProduto)
                elif opcao_produto == 2:
                    mercado_buscado.editarProduto(dsn, dicProduto)
                else:
                    print("Opção inválida.")
            elif (opcao == 6):
                # (ADMIN) SAIR DO MENU EDITAR MERCADO - 
                perfilMercado = 0

    def perfilMercado(mercado_buscado):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {mercado_buscado.id_usuario}\n"
        retornoPerfil += f"02. CNPJ: {Funcoes.formatarCpf(mercado_buscado.cnpj_usuario)}\n"
        retornoPerfil += f"03. NOME: {mercado_buscado.nome_usuario}\n"
        retornoPerfil += f"04. EMAIL: {mercado_buscado.email_usuario}\n"
        retornoPerfil += f"05. PRODUTO: {mercado_buscado.produto_usuario}\n"
        retornoPerfil += "05. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil