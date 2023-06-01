from Usuario import Usuario
from Funcoes import Funcoes
from Produto import Produto

class Estabelecimento(Usuario):
    def __init__(self, id_usuario=None, cnpj_usuario=None, nome_usuario=None, email_usuario=None, tipo_estabelecimento=None):
        super().__init__(id_usuario=id_usuario, cnpj_usuario=cnpj_usuario, nome_usuario=nome_usuario, email_usuario=email_usuario)
        self.tipo_estabelecimento = tipo_estabelecimento

    def cadastrarEstabelecimento(dsn, dicEstabelecimentos, id_usuario):
        # INSTANCIANDO NOVO ESTABELECIMENTO
        novo_estabelecimento = Estabelecimento()

        Funcoes.menuCabecalho()

        # SETANDO ID DO USUÁRIO
        id_usuario = id_usuario

        # SETANDO CNPJ DO ESTABELECIMENTO
        cnpj_usuario = input("DIGITE O SEU CNPJ (APENAS NÚMEROS, EXEMPLO: 12345678000200): ")
        while (Funcoes.validarCNPJ(cnpj_usuario) == False or cnpj_usuario in [estabelecimento.cnpj_usuario for estabelecimento in dicEstabelecimentos.values()]):
            print("CNPJ INVÁLIDO OU JÁ CADASTRADO.")
            cnpj_usuario = input("DIGITE O SEU CNPJ (APENAS NÚMEROS, EXEMPLO: 12345678000200): ")

        # SETANDO NOME DO ESTABELECIMENTO
        nome_usuario = input("DIGITE O NOME DO ESTABELECIMENTO COMPLETO: ")
        nome_usuario = Funcoes.validarPreenchimento("DIGITE O NOME DO ESTABELECIMENTO COMPLETO: ", nome_usuario)

        # SETANDO EMAIL DO ESTABELECIMENTO
        email_usuario = input("DIGITE O SEU EMAIL: ")
        email_usuario = Funcoes.validarPreenchimento("DIGITE O SEU EMAIL: ", email_usuario)
        while (email_usuario in [estabelecimento.email_usuario for estabelecimento in dicEstabelecimentos.values()]):
            print("EMAIL INVÁLIDO OU JÁ CADASTRADO.")
            email_usuario = input("DIGITE O SEU EMAIL: ")

        # PERGUNTAR TIPO DE ESTABELECIMENTO (RESTAURANTE OU MERCADO)
        tipo_estabelecimento = input("DIGITE O TIPO DE ESTABELECIMENTO (RESTAURANTE OU MERCADO): ")
        while (tipo_estabelecimento.lower() != "restaurante" and tipo_estabelecimento.lower() != "mercado"):
            print("TIPO DE ESTABELECIMENTO INVÁLIDO.")
            tipo_estabelecimento = input("DIGITE O TIPO DE ESTABELECIMENTO (RESTAURANTE OU MERCADO): ")

        print("------------------------------------------")

        # ADICIONANDO O ESTABELECIMENTO NO DICIONÁRIO DE ESTABELECIMENTOS
        novo_estabelecimento = Estabelecimento(id_usuario=id_usuario, cnpj_usuario=cnpj_usuario, nome_usuario=nome_usuario, email_usuario=email_usuario, tipo_estabelecimento=tipo_estabelecimento)
        dicEstabelecimentos[novo_estabelecimento.id_usuario] = novo_estabelecimento

        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        ##conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        ##cursor = conn.cursor()
        ##Funcoes.connect(dsn)

        # CADASTRANDO NO BANCO DE DADOS
        ##cursor.execute("INSERT INTO usuario (id_usuario, cnpj_usuario, nome_usuario, email_usuario) VALUES (:1, :2, :3, :4)", (novo_estabelecimento.id_usuario, novo_estabelecimento.cnpj_usuario, novo_estabelecimento.nome_usuario, novo_estabelecimento.email_usuario))
        ##cursor.execute("INSERT INTO restaurante (id_usuario) VALUES (:1)", (novo_estabelecimento.id_usuario,))
        ##cursor.connection.commit()

        # FECHANDO CONEXÃO COM O BANCO DE DADOS
        ##Funcoes.disconnect(conn, cursor)

        print(f"{tipo_estabelecimento.upper()} CADASTRADO COM SUCESSO!")
        input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")

    def editarEstabelecimento(self, dsn, dicEstabelecimentos, emails_cadastrados, Aluno):
        perfilEstabelecimento = 1
        Funcoes.exibirUsuariosAdmin(dicEstabelecimentos)
        id_buscado = int(input("DIGITE O ID DO ESTABELECIMENTO QUE DESEJA EDITAR: \n"))
        estabelecimento_buscado = Funcoes.buscarPorIdUsuario(id_buscado, dicEstabelecimentos)
        estabelecimento_buscado = Funcoes.validarUsuarioBuscado(estabelecimento_buscado, dicEstabelecimentos)

        while (perfilEstabelecimento == 1):
            opcao = int(input(Estabelecimento.perfilEstabelecimento(estabelecimento_buscado)))
            opcao = Funcoes.validarOpcao(opcao, 1, 6, Estabelecimento.perfilEstabelecimento(estabelecimento_buscado))

            if (opcao == 1):
                # (ADMIN) EDITAR ID DO ESTABELECIMENTO
                input(Funcoes.editarNegativo())

            elif (opcao == 2):
                # (ADMIN) EDITAR O CNPJ DO ESTABELECIMENTO
                input(Funcoes.editarNegativo())

            elif (opcao == 3):
                # (ADMIN) EDITAR O NOME DO ESTABELECIMENTO
                opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O NOME DO ESTABELECIMENTO {estabelecimento_buscado.nome_usuario}")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O NOME DO ESTABELECIMENTO {estabelecimento_buscado.nome_usuario}")))

                if (opcao == 1):
                    # (ADMIN) EDITAR O NOME DO ESTABELECIMENTO - SIM
                    Funcoes.editarNome(dsn, estabelecimento_buscado)
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 2):
                    # (ADMIN) EDITAR O NOME DO ESTABELECIMENTO - NÃO
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

            elif (opcao == 4):
                # (ADMIN) EDITAR O EMAIL DO ESTABELECIMENTO
                opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O EMAIL DO ESTABELECIMENTO {estabelecimento_buscado.nome_usuario}")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O EMAIL DO ESTABELECIMENTO {estabelecimento_buscado.nome_usuario}")))

                if (opcao == 1):
                    # (ADMIN) EDITAR O EMAIL DO ESTABELECIMENTO - SIM
                    Funcoes.editarEmail(dsn, estabelecimento_buscado, emails_cadastrados, Aluno)
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 2):
                    # (ADMIN) EDITAR O EMAIL DO ESTABELECIMENTO - NÃO
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

            elif (opcao == 5):
                # (ADMIN) CADASTRAR/EDITAR PRODUTO
                opcao_produto = int(input("1 - Cadastrar novo produto\n2 - Editar produto existente\nEscolha uma opção: "))
                if opcao_produto == 1:
                    estabelecimento_buscado.cadastrarProduto(dsn, dicProduto)
                elif opcao_produto == 2:
                    estabelecimento_buscado.editarProduto(dsn, dicProduto)
                else:
                    print("Opção inválida.")

            elif (opcao == 6):
                # (ADMIN) SAIR DO MENU EDITAR ESTABELECIMENTO
                perfilEstabelecimento = 0

    def perfilEstabelecimento(estabelecimento_buscado):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {estabelecimento_buscado.id_usuario}\n"
        retornoPerfil += f"02. CNPJ: {Funcoes.formatarCpf(estabelecimento_buscado.cnpj_usuario)}\n"
        retornoPerfil += f"03. NOME: {estabelecimento_buscado.nome_usuario}\n"
        retornoPerfil += f"04. EMAIL: {estabelecimento_buscado.email_usuario}\n"
        retornoPerfil += f"05. PRODUTO: {estabelecimento_buscado.produto_usuario}\n"
        retornoPerfil += "06. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil
