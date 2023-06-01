##import cx_Oracle

from Usuario import Usuario
from Funcoes import Funcoes
from datetime import datetime
from Level import Level

class Beneficiario(Usuario):
    def __init__(self, id_usuario=None, cpf_usuario=None, nome_usuario=None, email_usuario=None, data_nasc_beneficiario=None, data_registro_beneficiario=None, senha_beneficiario=None, moedas_Beneficiario=None, level_Beneficiario=None, produtos_Beneficiario=None, certificados_Beneficiario=None):
        super().__init__(id_usuario=id_usuario, cpf_usuario=cpf_usuario, nome_usuario=nome_usuario, email_usuario=email_usuario)
        self._data_nasc_beneficiario = data_nasc_beneficiario
        self._data_registro_beneficiario = data_registro_beneficiario
        self._senha_beneficiario = senha_beneficiario
    
    @property
    def data_nasc_beneficiario(self):
        return self._data_nasc_beneficiario
    
    @data_nasc_beneficiario.setter
    def data_nasc_beneficiario(self, data_nasc_beneficiario):
        self._data_nasc_beneficiario = data_nasc_beneficiario
    
    @property
    def data_registro_beneficiario(self):
        return self._data_registro_beneficiario
    
    @data_registro_beneficiario.setter
    def data_registro_beneficiario(self, data_registro_beneficiario):
        self._data_registro_beneficiario = data_registro_beneficiario
    
    @property
    def senha_beneficiario(self):
        return self._senha_beneficiario
    
    @senha_beneficiario.setter
    def senha_beneficiario(self, senha_beneficiario):
        self._senha_beneficiario = senha_beneficiario
    
        
    def cadastrarBeneficiario(dsn, cpfs_cadastrados, emails_cadastrados, dicBeneficiarios, id_usuario):
        
        # INSTANCIANDO NOVO Beneficiario - 
        novo_beneficiario = Beneficiario()

        Funcoes.menuCabecalho

        # SETANDO ID DO USUÁRIO - 
        id_usuario = id_usuario

        # SETANDO CPF DO USUÁRIO - 
        cpf_usuario = input("DIGITE O SEU CPF (APENAS NÚMEROS, EXEMPLO: 43102154278): ")
        cpf_usuario = Funcoes.verificarCPF(cpf_usuario, cpfs_cadastrados)
        cpfs_cadastrados.add(cpf_usuario)

        # SETANDO NOME DO USUÁRIO - 
        nome_usuario = input("DIGITE O SEU NOME COMPLETO: ")
        nome_usuario = Funcoes.validarPreenchimento("DIGITE O SEU NOME COMPLETO: ", nome_usuario)

        # SETANDO EMAIL DO USUÁRIO - 
        email_usuario = input("DIGITE O SEU EMAIL: ")
        email_usuario = Funcoes.validarPreenchimento("DIGITE O SEU EMAIL: ", email_usuario)
        email_usuario = Funcoes.verificarEmail(email_usuario, emails_cadastrados)
        emails_cadastrados.add(email_usuario)

        # SETANDO DATA DE NASCIMENTO DO USUÁRIO - 
        data_nasc_usuario = input("DIGITE A SUA DATA DE NASCIMENTO (DD/MM/YYYY): ")
        data_nasc_usuario = Funcoes.validarPreenchimento("DIGITE A SUA DATA DE NASCIMENTO (DD/MM/YYYY): ", data_nasc_usuario)
        data_formatada = datetime.strptime(data_nasc_usuario, '%d/%m/%Y')
        data_formatada = data_formatada.strftime("%d/%m/%Y")

        # SETANDO A DATA DE REGISTRO DO USUÁRIO - 
        data_registro_beneficiario = datetime.fromtimestamp(datetime.now().timestamp()).strftime('%d/%m/%Y')

        # SETANDO SENHA DO Beneficiario - 
        senha_beneficiario = input("DIGITE A SUA SENHA: ")
        senha_beneficiario = Funcoes.validarPreenchimento("DIGITE A SUA SENHA: ", senha_beneficiario)
        conf_senha = input("CONFIRME A SUA SENHA: ")
        conf_senha = Funcoes.validarPreenchimento("CONFIRME A SUA SENHA: ", conf_senha)
        senha_beneficiario = Funcoes.validarSenha(senha_beneficiario, conf_senha)


        print("------------------------------------------")

        # ADICIONANDO O Beneficiario NO DICIONÁRIO DE BeneficiarioS - 
        novo_beneficiario = Beneficiario(id_usuario = id_usuario, cpf_usuario = cpf_usuario, nome_usuario = nome_usuario, email_usuario = email_usuario, data_nasc_beneficiario = data_formatada, data_registro_beneficiario = data_registro_beneficiario, senha_beneficiario = senha_beneficiario)
        dicBeneficiarios[novo_beneficiario.id_usuario] = novo_beneficiario

        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        ##conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        ##cursor = conn.cursor()
        ##Funcoes.connect(dsn)

        # CADASTRANDO NO BANCO DE DADOS
        ##cursor.execute("INSERT INTO usuario (id_usuario, cpf_usuario, nome_usuario, email_usuario) VALUES (:1, :2, :3, :4)", (novo_beneficiario.id_usuario, novo_beneficiario.cpf_usuario, novo_beneficiario.nome_usuario, novo_beneficiario.email_usuario))
        ##cursor.execute("INSERT INTO Beneficiario (id_usuario, dt_nasc_Beneficiario, dt_reg_Beneficiario, senha_beneficiario) VALUES (:1, TO_DATE(:2, 'DD/MM/YYYY'), TO_DATE(:3, 'DD/MM/YYYY'), :4, :5, :6)", (novo_beneficiario.id_usuario, novo_beneficiario.data_nasc_beneficiario, novo_beneficiario.data_registro_beneficiario, novo_beneficiario.senha_beneficiario))
        ##cursor.connection.commit()

        # FECHANDO CONEXÃO COM O BANCO DE DADOS
        ##Funcoes.disconnect(conn, cursor)

        print("USUÁRIO CADASTRADO COM SUCESSO!")
        input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")
    
    def editarBeneficiario(self, dsn, dicBeneficiarios, emails_cadastrados):
        # (ADMIN) EDITAR BeneficiarioS - 
        perfilBeneficiario = 1

        if (len(dicBeneficiarios) == 0):
            input("NENHUM Beneficiario CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

        else:
            Funcoes.exibirUsuariosAdmin(dicBeneficiarios)
            id_buscado = int(input("DIGITE O ID DO Beneficiario QUE DESEJA EDITAR: \n"))
            Beneficiario_buscado = Funcoes.buscarPorIdUsuario(id_buscado, dicBeneficiarios)
            Beneficiario_buscado = Funcoes.validarUsuarioBuscado(Beneficiario_buscado, dicBeneficiarios)

            while (perfilBeneficiario == 1):
                opcao = int(input(Beneficiario.perfilBeneficiario(Beneficiario_buscado)))
                opcao = Funcoes.validarOpcao(opcao, 1, 12, Beneficiario.perfilBeneficiario(Beneficiario_buscado))

                if (opcao == 1):
                    # (ADMIN) EDITAR ID DO Beneficiario  - 
                    input(Funcoes.editarNegativo())

                elif (opcao == 2):
                    # (ADMIN) EDITAR O CPF DO Beneficiario - 
                    input(Funcoes.editarNegativo())
                
                elif (opcao == 3):
                    # (ADMIN) EDITAR O NOME DO Beneficiario - 
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O NOME DO Beneficiario {Beneficiario_buscado.nome_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O NOME DO Beneficiario {Beneficiario_buscado.nome_usuario}")))

                    if (opcao == 1):
                        # (ADMIN) EDITAR O NOME DO Beneficiario - SIM - 
                        Funcoes.editarNome(dsn, Beneficiario_buscado)
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                    
                    elif (opcao == 2):
                        # (ADMIN) EDITAR O NOME DO Beneficiario - NÃO - 
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 4):
                    # (ADMIN) EDITAR O EMAIL DO Beneficiario - 
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O EMAIL DO Beneficiario {Beneficiario_buscado.nome_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O EMAIL DO Beneficiario {Beneficiario_buscado.nome_usuario}")))
                    
                    if (opcao == 1):
                        # (ADMIN) EDITAR O EMAIL DO Beneficiario - SIM - 
                        Funcoes.editarEmail(dsn, Beneficiario_buscado, emails_cadastrados, Beneficiario)
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                    
                    elif (opcao == 2):
                        # (ADMIN) EDITAR O EMAIL DO Beneficiario - NÃO - 
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 5):
                    # (ADMIN) EDITAR A DATA DE NASCIMENTO DO Beneficiario - 
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A DATA DE NASCIMENTO DO Beneficiario {Beneficiario_buscado.nome_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A DATA DE NASCIMENTO DO Beneficiario {Beneficiario_buscado.nome_usuario}")))
                    
                    if (opcao == 1):
                        # (ADMIN) EDITAR A DATA DE NASCIMENTO DO Beneficiario - SIM - 
                        Funcoes.editarDataNasc(dsn, Beneficiario_buscado)
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                    
                    elif (opcao == 2):
                        # (ADMIN) EDITAR A DATA DE NASCIMENTO DO Beneficiario - NÃO - 
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 6):
                    # (ADMIN) EDITAR A DATA DE REGISTRO DO Beneficiario - 
                    input(Funcoes.editarNegativo())

                elif (opcao == 7):
                    # (ADMIN) EDITAR A SENHA DO Beneficiario - 
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A SENHA DO Beneficiario {Beneficiario_buscado.nome_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A SENHA DO Beneficiario {Beneficiario_buscado.nome_usuario}")))

                    if (opcao == 1):
                        # (ADMIN) EDITAR A SENHA DO Beneficiario - SIM - 
                        Funcoes.editarSenha(dsn, Beneficiario_buscado, "Beneficiario")
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                    
                    elif (opcao == 2):
                        # (ADMIN) EDITAR A SENHA DO Beneficiario - NÃO - 
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 8):
                    # (ADMIN) SAIR DO MENU EDITAR Beneficiario - 
                    perfilBeneficiario = 0

    def perfilBeneficiario(Beneficiario_buscado):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {Beneficiario_buscado.id_usuario}\n"
        retornoPerfil += f"02. CPF: {Funcoes.formatarCpf(Beneficiario_buscado.cpf_usuario)}\n"
        retornoPerfil += f"03. NOME: {Beneficiario_buscado.nome_usuario}\n"
        retornoPerfil += f"04. EMAIL: {Beneficiario_buscado.email_usuario}\n"
        retornoPerfil += f"05. DATA DE NASCIMENTO: {Funcoes.formatarData(Beneficiario_buscado.data_nasc_beneficiario)}\n"
        retornoPerfil += f"06. DATA DE REGISTRO: {Funcoes.formatarData(Beneficiario_buscado.data_registro_beneficiario)}\n"
        retornoPerfil += f"07. SENHA: {Beneficiario_buscado.senha_beneficiario}\n"
        retornoPerfil += "08. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil