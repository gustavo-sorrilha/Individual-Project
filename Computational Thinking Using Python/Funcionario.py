import cx_Oracle

from Usuario import Usuario
from Funcoes import Funcoes

class Funcionario(Usuario):
    def __init__(self, id_usuario=None, cpf_usuario=None, nome_usuario=None, email_usuario=None, senha_funcionario=None, cargo_funcionario=None):
        super().__init__(id_usuario=id_usuario, cpf_usuario=cpf_usuario, nome_usuario=nome_usuario, email_usuario=email_usuario)
        self._senha_funcionario = senha_funcionario
        self._cargo_funcionario = cargo_funcionario
    
    @property
    def senha_funcionario(self):
        return self._senha_funcionario
    
    @senha_funcionario.setter
    def senha_funcionario(self, senha_funcionario):
        self._senha_funcionario = senha_funcionario
    
    @property
    def cargo_funcionario(self):
        return self._cargo_funcionario
    
    @cargo_funcionario.setter
    def cargo_funcionario(self, cargo_funcionario):
        self._cargo_funcionario = cargo_funcionario

    def cadastrarFuncionario(dsn, dicFuncionarios, id_usuario):
        # INSTANCIANDO NOVO FUNCIONÁRIO - OK
        novo_funcionario = Funcionario()
        
        Funcoes.menuCabecalho

        # SETANDO ID DO USUÁRIO - OK
        id_usuario = id_usuario

        # SETANDO CPF DO USUÁRIO - OK
        cpf_usuario = input("DIGITE O SEU CPF (APENAS NÚMEROS, EXEMPLO: 43102154278): ")
        while (Funcoes.validarCPF(cpf_usuario) == False or cpf_usuario in [funcionario.cpf_usuario for funcionario in dicFuncionarios.values()]):
            print("CPF INVÁLIDO OU JÁ CADASTRADO.")
            cpf_usuario = input("DIGITE O SEU CPF (APENAS NÚMEROS, EXEMPLO: 43102154278): ")

        # SETANDO NOME DO USUÁRIO - OK
        nome_usuario = input("DIGITE O SEU NOME COMPLETO: ")
        nome_usuario = Funcoes.validarPreenchimento("DIGITE O SEU NOME COMPLETO: ", nome_usuario)

        # SETANDO EMAIL DO USUÁRIO - OK
        email_usuario = input("DIGITE O SEU EMAIL: ")
        email_usuario = Funcoes.validarPreenchimento("DIGITE O SEU EMAIL: ", email_usuario)
        while (email_usuario in [funcionario.email_usuario for funcionario in dicFuncionarios.values()]):
            print("EMAIL INVÁLIDO OU JÁ CADASTRADO.")
            email_usuario = input("DIGITE O SEU EMAIL: ")
            email_usuario = Funcoes.validarPreenchimento("DIGITE O SEU EMAIL: ", email_usuario)

        # SETANDO SENHA DO FUNCIONÁRIO - OK
        senha_funcionario = input("DIGITE A SUA SENHA: ")
        senha_funcionario = Funcoes.validarPreenchimento("DIGITE A SUA SENHA: ", senha_funcionario)
        conf_senha = input("CONFIRME A SUA SENHA: ")
        conf_senha = Funcoes.validarPreenchimento("CONFIRME A SUA SENHA: ", conf_senha)
        senha_funcionario = Funcoes.validarSenha(senha_funcionario, conf_senha)

        # SETANDO O CARGO DO FUNCIONÁRIO - OK
        cargo_funcionario = input("DIGITE O CARGO DO FUNCIONÁRIO: ")
        cargo_funcionario = Funcoes.validarPreenchimento("DIGITE O CARGO DO FUNCIONÁRIO: ", cargo_funcionario)

        print("------------------------------------------")

        # ADICIONANDO O FUNCIONÁRIO NO DICIONÁRIO DE FUNCIONÁRIOS - OK
        novo_funcionario = Funcionario(id_usuario = id_usuario, cpf_usuario = cpf_usuario, nome_usuario = nome_usuario, email_usuario = email_usuario, senha_funcionario = senha_funcionario, cargo_funcionario = cargo_funcionario)
        dicFuncionarios[novo_funcionario.id_usuario] = novo_funcionario

        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        cursor = conn.cursor()
        Funcoes.connect(dsn)

        # CADASTRANDO NO BANCO DE DADOS
        cursor.execute("INSERT INTO usuario (id_usuario, cpf_usuario, nome_usuario, email_usuario) VALUES (:1, :2, :3, :4)", (novo_funcionario.id_usuario, novo_funcionario.cpf_usuario, novo_funcionario.nome_usuario, novo_funcionario.email_usuario))
        cursor.execute("INSERT INTO funcionario (id_usuario, senha_funcionario, cargo_funcionario) VALUES (:1, :2, :3)", (novo_funcionario.id_usuario, novo_funcionario.senha_funcionario, novo_funcionario.cargo_funcionario))
        cursor.connection.commit()

         # FECHANDO CONEXÃO COM O BANCO DE DADOS
        Funcoes.disconnect(conn, cursor)

        print("FUNCIONÁRIO CADASTRADO COM SUCESSO!")
        input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")
    
    def editarFuncionario(self, dsn, dicFuncionarios, emails_cadastrados, Aluno):
        # (ADMIN) EDITAR FUNCIONÁRIOS - OK
        perfilFuncionario = 1
        Funcoes.exibirUsuariosAdmin(dicFuncionarios)
        id_buscado = int(input("DIGITE O ID DO FUNCIONÁRIO QUE DESEJA EDITAR: \n"))
        funcionario_buscado = Funcoes.buscarPorIdUsuario(id_buscado, dicFuncionarios)
        funcionario_buscado = Funcoes.validarUsuarioBuscado(funcionario_buscado, dicFuncionarios)

        while (perfilFuncionario == 1):
            opcao = int(input(Funcionario.perfilFuncionario(funcionario_buscado)))
            opcao = Funcoes.validarOpcao(opcao, 1, 7, Funcionario.perfilFuncionario(funcionario_buscado))

            if (opcao == 1):
                # (ADMIN) EDITAR ID DO FUNCIONÁRIO  - OK
                input(Funcoes.editarNegativo())

            elif (opcao == 2):
                # (ADMIN) EDITAR O CPF DO FUNCIONÁRIO - OK
                input(Funcoes.editarNegativo())
            
            elif (opcao == 3):
                # (ADMIN) EDITAR O NOME DO FUNCIONÁRIO - OK
                opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O NOME DO FUNCIONÁRIO {funcionario_buscado.nome_usuario}")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O NOME DO FUNCIONÁRIO {funcionario_buscado.nome_usuario}")))
                
                if (opcao == 1):
                    # (ADMIN) EDITAR O NOME DO FUNCIONÁRIO - SIM - OK
                    Funcoes.editarNome(dsn, funcionario_buscado)
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 2):
                    # (ADMIN) EDITAR O NOME DO FUNCIONÁRIO - NÃO - OK
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
            
            elif (opcao == 4):
                # (ADMIN) EDITAR O EMAIL DO FUNCIONÁRIO - OK
                opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O EMAIL DO FUNCIONÁRIO {funcionario_buscado.nome_usuario}")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O EMAIL DO FUNCIONÁRIO {funcionario_buscado.nome_usuario}")))
                
                if (opcao == 1):
                    # (ADMIN) EDITAR O EMAIL DO FUNCIONÁRIO - SIM - OK
                    Funcoes.editarEmail(dsn, funcionario_buscado, emails_cadastrados, Aluno)
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 2):
                    # (ADMIN) EDITAR O EMAIL DO FUNCIONÁRIO - NÃO - OK
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

            elif (opcao == 5):
                # (ADMIN) EDITAR A SENHA DO FUNCIONÁRIO - OK
                opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A SENHA DO FUNCIONÁRIO {funcionario_buscado.nome_usuario}")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A SENHA DO FUNCIONÁRIO {funcionario_buscado.nome_usuario}")))
                
                if (opcao == 1):
                    # (ADMIN) EDITAR A SENHA DO FUNCIONÁRIO - SIM - OK
                    Funcoes.editarSenha(dsn, funcionario_buscado, "Funcionario")
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 2):
                    # (ADMIN) EDITAR A SENHA DO FUNCIONÁRIO - NÃO - OK
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

            elif (opcao == 6):
                # (ADMIN) EDITAR O CARGO DO FUNCIONÁRIO - OK
                opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O CARGO DO FUNCIONÁRIO {funcionario_buscado.nome_usuario}")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O CARGO DO FUNCIONÁRIO {funcionario_buscado.nome_usuario}")))
                
                if (opcao == 1):
                    # (ADMIN) EDITAR O CARGO DO FUNCIONÁRIO - SIM - OK
                    Funcoes.editarCargo(dsn, funcionario_buscado)
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 2):
                    # (ADMIN) EDITAR O CARGO DO FUNCIONÁRIO - NÃO - OK
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

            elif (opcao == 7):
                # (ADMIN) SAIR DO MENU EDITAR FUNCIONÁRIO - OK
                perfilFuncionario = 0

    def perfilFuncionario(funcionario_buscado):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {funcionario_buscado.id_usuario}\n"
        retornoPerfil += f"02. CPF: {Funcoes.formatarCpf(funcionario_buscado.cpf_usuario)}\n"
        retornoPerfil += f"03. NOME: {funcionario_buscado.nome_usuario}\n"
        retornoPerfil += f"04. EMAIL: {funcionario_buscado.email_usuario}\n"
        retornoPerfil += f"05. SENHA: {funcionario_buscado.senha_funcionario}\n"
        retornoPerfil += f"06. CARGO: {funcionario_buscado.cargo_funcionario}\n"
        retornoPerfil += "07. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil
