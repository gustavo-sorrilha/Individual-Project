import cx_Oracle

from Usuario import Usuario
from Funcoes import Funcoes

class Professor(Usuario):
    def __init__(self, id_usuario=None, cpf_usuario=None, nome_usuario=None, email_usuario=None):
        super().__init__(id_usuario=id_usuario, cpf_usuario=cpf_usuario, nome_usuario=nome_usuario, email_usuario=email_usuario)

    def cadastrarProfessor(dsn, dicProfessores, id_usuario):
        # INSTANCIANDO NOVO PROFESSOR - OK
        novo_professor = Professor()
        
        Funcoes.menuCabecalho

        # SETANDO ID DO USUÁRIO - OK
        id_usuario = id_usuario

        # SETANDO CPF DO USUÁRIO - OK
        cpf_usuario = input("DIGITE O SEU CPF (APENAS NÚMEROS, EXEMPLO: 43102154278): ")
        while (Funcoes.validarCPF(cpf_usuario) == False or cpf_usuario in [professor.cpf_usuario for professor in dicProfessores.values()]):
            print("CPF INVÁLIDO OU JÁ CADASTRADO.")
            cpf_usuario = input("DIGITE O SEU CPF (APENAS NÚMEROS, EXEMPLO: 43102154278): ")

        # SETANDO NOME DO USUÁRIO - OK
        nome_usuario = input("DIGITE O SEU NOME COMPLETO: ")
        nome_usuario = Funcoes.validarPreenchimento("DIGITE O SEU NOME COMPLETO: ", nome_usuario)

        # SETANDO EMAIL DO USUÁRIO - OK
        email_usuario = input("DIGITE O SEU EMAIL: ")
        email_usuario = Funcoes.validarPreenchimento("DIGITE O SEU EMAIL: ", email_usuario)
        while (email_usuario in [professor.email_usuario for professor in dicProfessores.values()]):
            print("EMAIL INVÁLIDO OU JÁ CADASTRADO.")
            email_usuario = input("DIGITE O SEU EMAIL: ")

        print("------------------------------------------")

        # ADICIONANDO O PROFESSOR NO DICIONÁRIO DE PROFESSORES - OK
        novo_professor = Professor(id_usuario = id_usuario, cpf_usuario = cpf_usuario, nome_usuario = nome_usuario, email_usuario = email_usuario)
        dicProfessores[novo_professor.id_usuario] = novo_professor

         # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        cursor = conn.cursor()
        Funcoes.connect(dsn)

        # CADASTRANDO NO BANCO DE DADOS
        cursor.execute("INSERT INTO usuario (id_usuario, cpf_usuario, nome_usuario, email_usuario) VALUES (:1, :2, :3, :4)", (novo_professor.id_usuario, novo_professor.cpf_usuario, novo_professor.nome_usuario, novo_professor.email_usuario))
        cursor.execute("INSERT INTO professor (id_usuario) VALUES (:1)", (novo_professor.id_usuario,))
        cursor.connection.commit()

         # FECHANDO CONEXÃO COM O BANCO DE DADOS
        Funcoes.disconnect(conn, cursor)

        print("PROFESSOR CADASTRADO COM SUCESSO!")
        input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")
    
    def editarProfessor(self, dsn, dicProfessores, emails_cadastrados, Aluno):
        perfilProfessor = 1
        Funcoes.exibirUsuariosAdmin(dicProfessores)
        id_buscado = int(input("DIGITE O ID DO PROFESSOR QUE DESEJA EDITAR: \n"))
        professor_buscado = Funcoes.buscarPorIdUsuario(id_buscado, dicProfessores)
        professor_buscado = Funcoes.validarUsuarioBuscado(professor_buscado, dicProfessores)

        while (perfilProfessor == 1):
            opcao = int(input(Professor.perfilProfessor(professor_buscado)))
            opcao = Funcoes.validarOpcao(opcao, 1, 5, Professor.perfilProfessor(professor_buscado))

            if (opcao == 1):
                # (ADMIN) EDITAR ID DO PROFESSOR  - OK
                input(Funcoes.editarNegativo())

            elif (opcao == 2):
                # (ADMIN) EDITAR O CPF DO PROFESSOR - OK
                input(Funcoes.editarNegativo())
            
            elif (opcao == 3):
                # (ADMIN) EDITAR O NOME DO PROFESSOR - OK
                opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O NOME DO PROFESSOR {professor_buscado.nome_usuario}")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O NOME DO PROFESSOR {professor_buscado.nome_usuario}")))
                
                if (opcao == 1):
                    # (ADMIN) EDITAR O NOME DO PROFESSOR - SIM - OK
                    Funcoes.editarNome(dsn, professor_buscado)
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 2):
                    # (ADMIN) EDITAR O NOME DO PROFESSOR - NÃO - OK
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
            
            elif (opcao == 4):
                # (ADMIN) EDITAR O EMAIL DO PROFESSOR - OK
                opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O EMAIL DO PROFESSOR {professor_buscado.nome_usuario}")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O EMAIL DO PROFESSOR {professor_buscado.nome_usuario}")))
                
                if (opcao == 1):
                    # (ADMIN) EDITAR O EMAIL DO PROFESSOR - SIM - OK
                    Funcoes.editarEmail(dsn, professor_buscado, emails_cadastrados, Aluno)
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 2):
                    # (ADMIN) EDITAR O EMAIL DO PROFESSOR - NÃO - OK
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

            elif (opcao == 5):
                # (ADMIN) SAIR DO MENU EDITAR PROFESSOR - OK
                perfilProfessor = 0

    def perfilProfessor(professor_buscado):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {professor_buscado.id_usuario}\n"
        retornoPerfil += f"02. CPF: {Funcoes.formatarCpf(professor_buscado.cpf_usuario)}\n"
        retornoPerfil += f"03. NOME: {professor_buscado.nome_usuario}\n"
        retornoPerfil += f"04. EMAIL: {professor_buscado.email_usuario}\n"
        retornoPerfil += "05. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil