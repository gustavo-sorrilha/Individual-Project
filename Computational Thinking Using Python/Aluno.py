import cx_Oracle

from Usuario import Usuario
from Funcoes import Funcoes
from datetime import datetime
from Level import Level

class Aluno(Usuario):
    def __init__(self, id_usuario=None, cpf_usuario=None, nome_usuario=None, email_usuario=None, data_nasc_aluno=None, data_registro_aluno=None, senha_aluno=None, moedas_aluno=None, level_aluno=None, produtos_aluno=None, certificados_aluno=None):
        super().__init__(id_usuario=id_usuario, cpf_usuario=cpf_usuario, nome_usuario=nome_usuario, email_usuario=email_usuario)
        self._data_nasc_aluno = data_nasc_aluno
        self._data_registro_aluno = data_registro_aluno
        self._senha_aluno = senha_aluno
        self._moedas_aluno = moedas_aluno
        self._level_aluno = level_aluno
        self._produtos_aluno = produtos_aluno if produtos_aluno is not None else []
        self._certificados_aluno = certificados_aluno if certificados_aluno is not None else []
        
    @property
    def data_nasc_aluno(self):
        return self._data_nasc_aluno
    
    @data_nasc_aluno.setter
    def data_nasc_aluno(self, data_nasc_aluno):
        self._data_nasc_aluno = data_nasc_aluno
    
    @property
    def data_registro_aluno(self):
        return self._data_registro_aluno
    
    @data_registro_aluno.setter
    def data_registro_aluno(self, data_registro_aluno):
        self._data_registro_aluno = data_registro_aluno
    
    @property
    def senha_aluno(self):
        return self._senha_aluno
    
    @senha_aluno.setter
    def senha_aluno(self, senha_aluno):
        self._senha_aluno = senha_aluno
    
    @property
    def moedas_aluno(self):
        return self._moedas_aluno
    
    @moedas_aluno.setter
    def moedas_aluno(self, moedas_aluno):
        self._moedas_aluno = moedas_aluno
    
    @property
    def level_aluno(self):
        return self._level_aluno
    
    @level_aluno.setter
    def level_aluno(self, level_aluno):
        self._level_aluno = level_aluno
    
    @property
    def produtos_aluno(self):
        return self._produtos_aluno
    
    def add_produto(self, produto):
        self._produtos_aluno.append(produto)
    
    def remove_produto(self, produto):
        self._produtos_aluno.remove(produto)
    
    @property
    def certificados_aluno(self):
        return self._certificados_aluno
    
    @certificados_aluno.setter
    def certificados_aluno(self, certificados_aluno):
        self._certificados_aluno = certificados_aluno
    
    def add_certificado(self, certificado):
        self._certificados_aluno.append(certificado)
    
    def remove_certificado(self, certificado):
        self._certificados_aluno.remove(certificado)
        
    def cadastrarAluno(dsn, cpfs_cadastrados, emails_cadastrados, dicAlunos, id_usuario):
        
        # INSTANCIANDO NOVO ALUNO - OK
        novo_aluno = Aluno()

        Funcoes.menuCabecalho

        # SETANDO ID DO USUÁRIO - OK
        id_usuario = id_usuario

        # SETANDO CPF DO USUÁRIO - OK
        cpf_usuario = input("DIGITE O SEU CPF (APENAS NÚMEROS, EXEMPLO: 43102154278): ")
        cpf_usuario = Funcoes.verificarCPF(cpf_usuario, cpfs_cadastrados)
        cpfs_cadastrados.add(cpf_usuario)

        # SETANDO NOME DO USUÁRIO - OK
        nome_usuario = input("DIGITE O SEU NOME COMPLETO: ")
        nome_usuario = Funcoes.validarPreenchimento("DIGITE O SEU NOME COMPLETO: ", nome_usuario)

        # SETANDO EMAIL DO USUÁRIO - OK
        email_usuario = input("DIGITE O SEU EMAIL: ")
        email_usuario = Funcoes.validarPreenchimento("DIGITE O SEU EMAIL: ", email_usuario)
        email_usuario = Funcoes.verificarEmail(email_usuario, emails_cadastrados)
        emails_cadastrados.add(email_usuario)

        # SETANDO DATA DE NASCIMENTO DO USUÁRIO - OK
        data_nasc_usuario = input("DIGITE A SUA DATA DE NASCIMENTO (DD/MM/YYYY): ")
        data_nasc_usuario = Funcoes.validarPreenchimento("DIGITE A SUA DATA DE NASCIMENTO (DD/MM/YYYY): ", data_nasc_usuario)
        data_formatada = datetime.strptime(data_nasc_usuario, '%d/%m/%Y')
        data_formatada = data_formatada.strftime("%d/%m/%Y")

        # SETANDO A DATA DE REGISTRO DO USUÁRIO - OK
        data_registro_aluno = datetime.fromtimestamp(datetime.now().timestamp()).strftime('%d/%m/%Y')

        # SETANDO SENHA DO ALUNO - OK
        senha_aluno = input("DIGITE A SUA SENHA: ")
        senha_aluno = Funcoes.validarPreenchimento("DIGITE A SUA SENHA: ", senha_aluno)
        conf_senha = input("CONFIRME A SUA SENHA: ")
        conf_senha = Funcoes.validarPreenchimento("CONFIRME A SUA SENHA: ", conf_senha)
        senha_aluno = Funcoes.validarSenha(senha_aluno, conf_senha)

        # SETANDO LEVEL DO USUÁRIO - OK
        level_aluno = Level.Iniciante

        # SETANDO MOEDAS DO USUÁRIO - OK
        moedas_aluno = 0

        # SETANDO PRODUTOS DO USUÁRIO - OK
        produtos_aluno = []

        # SETANDO CERTIFICADOS DO USUÁRIO - OK
        certificados_aluno = []

        print("------------------------------------------")

        # ADICIONANDO O ALUNO NO DICIONÁRIO DE ALUNOS - OK
        novo_aluno = Aluno(id_usuario = id_usuario, cpf_usuario = cpf_usuario, nome_usuario = nome_usuario, email_usuario = email_usuario, data_nasc_aluno = data_formatada, data_registro_aluno = data_registro_aluno, senha_aluno = senha_aluno, level_aluno = level_aluno, moedas_aluno = moedas_aluno, produtos_aluno = produtos_aluno, certificados_aluno = certificados_aluno)
        dicAlunos[novo_aluno.id_usuario] = novo_aluno

        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        cursor = conn.cursor()
        Funcoes.connect(dsn)

        # CADASTRANDO NO BANCO DE DADOS
        cursor.execute("INSERT INTO usuario (id_usuario, cpf_usuario, nome_usuario, email_usuario) VALUES (:1, :2, :3, :4)", (novo_aluno.id_usuario, novo_aluno.cpf_usuario, novo_aluno.nome_usuario, novo_aluno.email_usuario))
        cursor.execute("INSERT INTO aluno (id_usuario, dt_nasc_aluno, dt_reg_aluno, senha_aluno, moedas_aluno, nivel_aluno) VALUES (:1, TO_DATE(:2, 'DD/MM/YYYY'), TO_DATE(:3, 'DD/MM/YYYY'), :4, :5, :6)", (novo_aluno.id_usuario, novo_aluno.data_nasc_aluno, novo_aluno.data_registro_aluno, novo_aluno.senha_aluno, novo_aluno.moedas_aluno, novo_aluno.level_aluno.name))
        cursor.connection.commit()

        # FECHANDO CONEXÃO COM O BANCO DE DADOS
        Funcoes.disconnect(conn, cursor)

        print("USUÁRIO CADASTRADO COM SUCESSO!")
        input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")
    
    def editarAluno(self, dsn, dicAlunos, emails_cadastrados):
        # (ADMIN) EDITAR ALUNOS - OK
        perfilAluno = 1

        if (len(dicAlunos) == 0):
            input("NENHUM ALUNO CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

        else:
            Funcoes.exibirUsuariosAdmin(dicAlunos)
            id_buscado = int(input("DIGITE O ID DO ALUNO QUE DESEJA EDITAR: \n"))
            aluno_buscado = Funcoes.buscarPorIdUsuario(id_buscado, dicAlunos)
            aluno_buscado = Funcoes.validarUsuarioBuscado(aluno_buscado, dicAlunos)

            while (perfilAluno == 1):
                opcao = int(input(Aluno.perfilAluno(aluno_buscado)))
                opcao = Funcoes.validarOpcao(opcao, 1, 12, Aluno.perfilAluno(aluno_buscado))

                if (opcao == 1):
                    # (ADMIN) EDITAR ID DO ALUNO  - OK
                    input(Funcoes.editarNegativo())

                elif (opcao == 2):
                    # (ADMIN) EDITAR O CPF DO ALUNO - OK
                    input(Funcoes.editarNegativo())
                
                elif (opcao == 3):
                    # (ADMIN) EDITAR O NOME DO ALUNO - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O NOME DO ALUNO {aluno_buscado.nome_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O NOME DO ALUNO {aluno_buscado.nome_usuario}")))

                    if (opcao == 1):
                        # (ADMIN) EDITAR O NOME DO ALUNO - SIM - OK
                        Funcoes.editarNome(dsn, aluno_buscado)
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                    
                    elif (opcao == 2):
                        # (ADMIN) EDITAR O NOME DO ALUNO - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 4):
                    # (ADMIN) EDITAR O EMAIL DO ALUNO - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O EMAIL DO ALUNO {aluno_buscado.nome_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O EMAIL DO ALUNO {aluno_buscado.nome_usuario}")))
                    
                    if (opcao == 1):
                        # (ADMIN) EDITAR O EMAIL DO ALUNO - SIM - OK
                        Funcoes.editarEmail(dsn, aluno_buscado, emails_cadastrados, Aluno)
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                    
                    elif (opcao == 2):
                        # (ADMIN) EDITAR O EMAIL DO ALUNO - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 5):
                    # (ADMIN) EDITAR A DATA DE NASCIMENTO DO ALUNO - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A DATA DE NASCIMENTO DO ALUNO {aluno_buscado.nome_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A DATA DE NASCIMENTO DO ALUNO {aluno_buscado.nome_usuario}")))
                    
                    if (opcao == 1):
                        # (ADMIN) EDITAR A DATA DE NASCIMENTO DO ALUNO - SIM - OK
                        Funcoes.editarDataNasc(dsn, aluno_buscado)
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                    
                    elif (opcao == 2):
                        # (ADMIN) EDITAR A DATA DE NASCIMENTO DO ALUNO - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 6):
                    # (ADMIN) EDITAR A DATA DE REGISTRO DO ALUNO - OK
                    input(Funcoes.editarNegativo())

                elif (opcao == 7):
                    # (ADMIN) EDITAR AS MOEDAS DO ALUNO - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR AS MOEDAS DO ALUNO {aluno_buscado.nome_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR AS MOEDAS DO ALUNO {aluno_buscado.nome_usuario}")))

                    if (opcao == 1):
                        # (ADMIN) EDITAR AS MOEDAS DO ALUNO - SIM - OK
                        Funcoes.editarMoedas(dsn, aluno_buscado)
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                    
                    elif (opcao == 2):
                        # (ADMIN) EDITAR AS MOEDAS DO ALUNO - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 8):
                    # (ADMIN) EDITAR O LEVEL DO ALUNO - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O LEVEL DO ALUNO {aluno_buscado.nome_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O LEVEL DO ALUNO {aluno_buscado.nome_usuario}")))

                    if (opcao == 1):
                        # (ADMIN) EDITAR O LEVEL DO ALUNO - SIM - OK
                        Funcoes.editarLevel(dsn, aluno_buscado)
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                    
                    elif (opcao == 2):
                        # (ADMIN) EDITAR O LEVEL DO ALUNO - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 9):
                    # (ADMIN) EDITAR A SENHA DO ALUNO - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A SENHA DO ALUNO {aluno_buscado.nome_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A SENHA DO ALUNO {aluno_buscado.nome_usuario}")))

                    if (opcao == 1):
                        # (ADMIN) EDITAR A SENHA DO ALUNO - SIM - OK
                        Funcoes.editarSenha(dsn, aluno_buscado, "Aluno")
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                    
                    elif (opcao == 2):
                        # (ADMIN) EDITAR A SENHA DO ALUNO - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 10):
                    # (ADMIN) EDITAR PRODUTOS DO ALUNO  - OK
                    input(Funcoes.editarNegativo())

                elif (opcao == 11):
                    # (ADMIN) EDITAR CERTIFICADOS DO ALUNO  - OK
                    input(Funcoes.editarNegativo())
                
                elif (opcao == 12):
                    # (ADMIN) SAIR DO MENU EDITAR ALUNO - OK
                    perfilAluno = 0

    def perfilAluno(aluno_buscado):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {aluno_buscado.id_usuario}\n"
        retornoPerfil += f"02. CPF: {Funcoes.formatarCpf(aluno_buscado.cpf_usuario)}\n"
        retornoPerfil += f"03. NOME: {aluno_buscado.nome_usuario}\n"
        retornoPerfil += f"04. EMAIL: {aluno_buscado.email_usuario}\n"
        retornoPerfil += f"05. DATA DE NASCIMENTO: {Funcoes.formatarData(aluno_buscado.data_nasc_aluno)}\n"
        retornoPerfil += f"06. DATA DE REGISTRO: {Funcoes.formatarData(aluno_buscado.data_registro_aluno)}\n"
        retornoPerfil += f"07. MOEDAS: {aluno_buscado.moedas_aluno}\n"
        retornoPerfil += f"08. LEVEL: {aluno_buscado.level_aluno}\n"
        retornoPerfil += f"09. SENHA: {aluno_buscado.senha_aluno}\n"

        retornoPerfil += "10. PRODUTOS COMPRADOS: "
        if len(aluno_buscado.produtos_aluno) == 0:
            retornoPerfil += "NENHUM PRODUTO COMPRADO\n"
        else:
            for i, produto in enumerate(aluno_buscado.produtos_aluno):
                if i == 0:
                    retornoPerfil += f"\n 10.{i+1}. NOME: {produto['nome_produto']} | QUANTIDADE: {produto['qtd_produto']}\n"
                else:
                    retornoPerfil += f" 10.{i+1}. NOME: {produto['nome_produto']} | QUANTIDADE: {produto['qtd_produto']}\n"
        
        retornoPerfil += "11. CERTIFICADOS: "
        if len(aluno_buscado.certificados_aluno) == 0:
            retornoPerfil += "VOCÊ NÃO POSSUI CERTIFICADOS\n"
        else:
            for i, certificado in enumerate(aluno_buscado.certificados_aluno):
                if i == 0:
                    retornoPerfil += f"\n 11.{i+1}. ID: {certificado['id_certificado']} | DATA: {Funcoes.formatarData(certificado['data_certificado'])}\n"
                else:
                    retornoPerfil += f" 11.{i+1}. ID: {certificado['id_certificado']} | DATA: {Funcoes.formatarData(certificado['data_certificado'])}\n"
            
        retornoPerfil += "12. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil