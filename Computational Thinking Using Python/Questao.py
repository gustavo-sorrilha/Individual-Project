import cx_Oracle

from enum import Enum
from typing import List
from Funcoes import Funcoes
from Resposta import Resposta

from enum import Enum

class Questao:
    def __init__(self, id_questao=None, pergunta=None, altA=None, altB=None, altC=None, altD=None, altE=None, resposta=None):
        self._id_questao = id_questao
        self._pergunta = pergunta
        self._altA = altA
        self._altB = altB
        self._altC = altC
        self._altD = altD
        self._altE = altE
        self._resposta = resposta

    @property
    def id_questao(self):
        return self._id_questao

    @id_questao.setter
    def id_questao(self, id_questao):
        self._id_questao = id_questao

    @property
    def pergunta(self):
        return self._pergunta
    
    @pergunta.setter
    def pergunta(self, pergunta):
        self._pergunta = pergunta
    
    @property
    def altA(self):
        return self._altA
    
    @altA.setter
    def altA(self, altA):
        self._altA = altA
    
    @property
    def altB(self):
        return self._altB
    
    @altB.setter
    def altB(self, altB):
        self._altB = altB
    
    @property
    def altC(self):
        return self._altC
    
    @altC.setter
    def altC(self, altC):
        self._altC = altC
    
    @property
    def altD(self):
        return self._altD
    
    @altD.setter
    def altD(self, altD):
        self._altD = altD
    
    @property
    def altE(self):
        return self._altE
    
    @altE.setter
    def altE(self, altE):
        self._altE = altE

    @property
    def resposta(self):
        return self._resposta

    @resposta.setter
    def resposta(self, resposta):
        self._resposta = resposta

    @staticmethod
    def from_dict(questao_dict: dict) -> 'Questao':
        return Questao(
            questao_dict['id_questao'],
            questao_dict['pergunta'],
            questao_dict['altA'],
            questao_dict['altB'],
            questao_dict['altC'],
            questao_dict['altD'],
            questao_dict['altE'],
            questao_dict['resposta']
        )

    @staticmethod
    def to_dict(questao: 'Questao') -> dict:
        return {
            'id_questao': questao.id_questao,
            'pergunta': questao.pergunta,
            'altA': questao.altA,
            'altB': questao.altB,
            'altC': questao.altC,
            'altD': questao.altD,
            'altE': questao.altE,
            'resposta': questao.resposta
        }

    @staticmethod
    def from_list(questao_list: List[dict]) -> List['Questao']:
        return [Questao.from_dict(questao_dict) for questao_dict in questao_list]

    @staticmethod
    def to_list(questao: List['Questao']) -> List[dict]:
        return [Questao.to_dict(q) for q in questao]

    def cadastrarQuestao(dsn, id_questao, listaQuestoes):
        Funcoes.menuCabecalho

        # SETANDO ID DA QUESTÃO - OK
        id_questao = id_questao

        # SETANDO PERGUNTA DA QUESTÃO - OK
        pergunta = input("DIGITE A PERGUNTA DA QUESTÃO: ")
        pergunta = Funcoes.validarPreenchimento("DIGITE A PERGUNTA DA QUESTÃO: ", pergunta)

        # SETANDO ALTERNATIVA A DA QUESTÃO - OK
        altA = input("DIGITE A ALTERNATIVA A DA QUESTÃO: ")
        altA = Funcoes.validarPreenchimento("DIGITE A ALTERNATIVA A DA QUESTÃO: ", altA)

        # SETANDO ALTERNATIVA B DA QUESTÃO - OK
        altB = input("DIGITE A ALTERNATIVA B DA QUESTÃO: ")
        altB = Funcoes.validarPreenchimento("DIGITE A ALTERNATIVA B DA QUESTÃO: ", altB)

        # SETANDO ALTERNATIVA C DA QUESTÃO - OK
        altC = input("DIGITE A ALTERNATIVA C DA QUESTÃO: ")
        altC = Funcoes.validarPreenchimento("DIGITE A ALTERNATIVA C DA QUESTÃO: ", altC)

        # SETANDO ALTERNATIVA D DA QUESTÃO - OK
        altD = input("DIGITE A ALTERNATIVA D DA QUESTÃO: ")
        altD = Funcoes.validarPreenchimento("DIGITE A ALTERNATIVA D DA QUESTÃO: ", altD)

        # SETANDO ALTERNATIVA E DA QUESTÃO - OK
        altE = input("DIGITE A ALTERNATIVA E DA QUESTÃO: ")
        altE = Funcoes.validarPreenchimento("DIGITE A ALTERNATIVA E DA QUESTÃO: ", altE)

        # SETANDO RESPOSTA DA QUESTÃO - OK                  
        opcao = int(input(Funcoes.menuAdminRespostas()))
        opcao = Funcoes.validarOpcao(opcao, 1, 25, Funcoes.menuAdminRespostas())

        if opcao == 1:
            resposta = 'A'
        elif opcao == 2:
            resposta = 'AB'
        elif opcao == 3:
            resposta = 'AC'
        elif opcao == 4:
            resposta = 'AD'
        elif opcao == 5:
            resposta = 'AE'
        elif opcao == 6:
            resposta = 'B'
        elif opcao == 7:
            resposta = 'BA'
        elif opcao == 8:
            resposta = 'BC'
        elif opcao == 9:
            resposta = 'BD'
        elif opcao == 10:
            resposta = 'BE'
        elif opcao == 11:
            resposta = 'C'
        elif opcao == 12:
            resposta = 'CA'
        elif opcao == 13:
            resposta = 'CB'
        elif opcao == 14:
            resposta = 'CD'
        elif opcao == 15:
            resposta = 'CE'
        elif opcao == 16:
            resposta = 'D'
        elif opcao == 17:
            resposta = 'DA'
        elif opcao == 18:
            resposta = 'DB'
        elif opcao == 19:
            resposta = 'DC'
        elif opcao == 20:
            resposta = 'DE'
        elif opcao == 21:
            resposta = 'E'
        elif opcao == 22:
            resposta = 'EA'
        elif opcao == 23:
            resposta = 'EB'
        elif opcao == 24:
            resposta = 'EC'
        elif opcao == 25:
            resposta = 'ED'
        print("------------------------------------------")

        # ADICIONANDO A QUESTÃO NA LISTA DE QUESTÕES - OK
        nova_questao = Questao(id_questao = id_questao, pergunta = pergunta, altA = altA, altB = altB, altC = altC, altD = altD, altE = altE, resposta = resposta)
        listaQuestoes.append(nova_questao)

        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        cursor = conn.cursor()
        Funcoes.connect(dsn)

        # CADASTRANDO NO BANCO DE DADOS
        cursor.execute("INSERT INTO questao (id_questao, pergunta_questao, alt_a_questao, alt_b_questao, alt_c_questao, alt_d_questao, alt_e_questao, resposta_questao) VALUES (:1, :2, :3, :4, :5, :6, :7, :8)", (nova_questao.id_questao, nova_questao.pergunta, nova_questao.altA, nova_questao.altB, nova_questao.altC, nova_questao.altD, nova_questao.altE, nova_questao.resposta))
        cursor.connection.commit()

        # FECHANDO CONEXÃO COM O BANCO DE DADOS
        Funcoes.disconnect(conn, cursor)

        print("QUESTÃO CADASTRADA COM SUCESSO!")
        input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")

    def editarQuestao(self, dsn, listaQuestoes):
        perfilQuestao = 1
        Funcoes.exibirQuestoesAdmin(listaQuestoes)
        id_buscado = int(input("DIGITE O ID DA QUESTÃO QUE DESEJA EDITAR: \n"))
        questao_buscada = Funcoes.buscarPorIdQuestao(id_buscado, listaQuestoes)
        questao_buscada = Funcoes.validarQuestaoBuscada(questao_buscada, listaQuestoes)

        while (perfilQuestao == 1):
            opcao = int(input(Questao.perfilQuestao(questao_buscada)))
            opcao = Funcoes.validarOpcao(opcao, 1, 9, Questao.perfilQuestao(questao_buscada))

            if (opcao == 1):
                # (ADMIN) EDITAR O ID DA QUESTÃO  - OK
                input(Funcoes.editarNegativo())
            
            elif (opcao == 2):
                # (ADMIN) EDITAR A PERGUNTA DA QUESTÃO - OK
                opcao = int(input(Funcoes.confirmarAcao("EDITAR PERGUNTA")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao("EDITAR PERGUNTA")))

                if (opcao == 1):
                    if Funcoes.confirmarAcao("EDITAR PERGUNTA"):
                        nova_pergunta = input("DIGITE A NOVA PERGUNTA DA QUESTÃO: ")
                        nova_pergunta = Funcoes.validarPreenchimento("DIGITE A NOVA PERGUNTA DA QUESTÃO: ", nova_pergunta)

                        # CRIANDO CONEXÃO COM O BANCO DE DADOS
                        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                        cursor = conn.cursor()
                        Funcoes.connect(dsn)

                        # EDITANDO NO BANCO DE DADOS E NO CONSOLE
                        cursor.execute("UPDATE questao SET pergunta_questao = :nova_pergunta WHERE id_questao = :id_questao", {"nova_pergunta": nova_pergunta, "id_questao": questao_buscada.id_questao})
                        cursor.connection.commit()
                        questao_buscada.pergunta = nova_pergunta
                        print("QUESTÃO EDITADA COM SUCESSO!")
                        input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")

                        # FECHANDO CONEXÃO COM O BANCO DE DADOS
                        Funcoes.disconnect(conn, cursor)

                    else:
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 2):
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

            elif (opcao == 3):
                # (ADMIN) EDITAR A ALTERNATIVA A DA QUESTÃO - OK
                opcao = int(input(Funcoes.confirmarAcao("EDITAR ALTERNATIVA A")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao("EDITAR ALTERNATIVA A")))

                if (opcao == 1):
                    if Funcoes.confirmarAcao("EDITAR ALTERNATIVA A"):
                        nova_altA = input("DIGITE A NOVA ALTERNATIVA A DA QUESTÃO: ")
                        nova_altA = Funcoes.validarPreenchimento("DIGITE A NOVA ALTERNATIVA A DA QUESTÃO: ", nova_altA)

                        # CRIANDO CONEXÃO COM O BANCO DE DADOS
                        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                        cursor = conn.cursor()
                        Funcoes.connect(dsn)

                        # EDITANDO NO BANCO DE DADOS E NO CONSOLE
                        cursor.execute("UPDATE questao SET alt_a_questao = :nova_altA WHERE id_questao = :id_questao", {"nova_altA": nova_altA, "id_questao": questao_buscada.id_questao})
                        cursor.connection.commit()
                        questao_buscada.altA = nova_altA
                        print("QUESTÃO EDITADA COM SUCESSO!")
                        input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")

                        # FECHANDO CONEXÃO COM O BANCO DE DADOS
                        Funcoes.disconnect(conn, cursor)

                    else:
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 2):
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

            elif (opcao == 4):
                # (ADMIN) EDITAR A ALTERNATIVA B DA QUESTÃO - OK
                opcao = int(input(Funcoes.confirmarAcao("EDITAR ALTERNATIVA B")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao("EDITAR ALTERNATIVA B")))

                if (opcao == 1):
                    if Funcoes.confirmarAcao("EDITAR ALTERNATIVA B"):
                        nova_altB = input("DIGITE A NOVA ALTERNATIVA B DA QUESTÃO: ")
                        nova_altB = Funcoes.validarPreenchimento("DIGITE A NOVA ALTERNATIVA B DA QUESTÃO: ", nova_altB)

                        # CRIANDO CONEXÃO COM O BANCO DE DADOS
                        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                        cursor = conn.cursor()
                        Funcoes.connect(dsn)

                        # EDITANDO NO BANCO DE DADOS E NO CONSOLE
                        cursor.execute("UPDATE questao SET alt_b_questao = :nova_altB WHERE id_questao = :id_questao", {"nova_altB": nova_altB, "id_questao": questao_buscada.id_questao})
                        cursor.connection.commit()
                        questao_buscada.altB = nova_altB
                        print("QUESTÃO EDITADA COM SUCESSO!")
                        input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")

                        # FECHANDO CONEXÃO COM O BANCO DE DADOS
                        Funcoes.disconnect(conn, cursor)

                    else:
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                        
                elif (opcao == 2):
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

            elif (opcao == 5):
                # (ADMIN) EDITAR A ALTERNATIVA C DA QUESTÃO - OK
                opcao = int(input(Funcoes.confirmarAcao("EDITAR ALTERNATIVA C")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao("EDITAR ALTERNATIVA C")))

                if (opcao == 1):
                    if Funcoes.confirmarAcao("EDITAR ALTERNATIVA C"):
                        nova_altC = input("DIGITE A NOVA ALTERNATIVA C DA QUESTÃO: ")
                        nova_altC = Funcoes.validarPreenchimento("DIGITE A NOVA ALTERNATIVA C DA QUESTÃO: ", nova_altC)

                        # CRIANDO CONEXÃO COM O BANCO DE DADOS
                        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                        cursor = conn.cursor()
                        Funcoes.connect(dsn)

                        # EDITANDO NO BANCO DE DADOS E NO CONSOLE
                        cursor.execute("UPDATE questao SET alt_c_questao = :nova_altC WHERE id_questao = :id_questao", {"nova_altC": nova_altC, "id_questao": questao_buscada.id_questao})
                        cursor.connection.commit()
                        questao_buscada.altC = nova_altC
                        print("QUESTÃO EDITADA COM SUCESSO!")
                        input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")

                        # FECHANDO CONEXÃO COM O BANCO DE DADOS
                        Funcoes.disconnect(conn, cursor)

                    else:
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 2):
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

            elif (opcao == 6):
                # (ADMIN) EDITAR A ALTERNATIVA D DA QUESTÃO - OK
                opcao = int(input(Funcoes.confirmarAcao("EDITAR ALTERNATIVA D")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao("EDITAR ALTERNATIVA D")))

                if (opcao == 1):
                    if Funcoes.confirmarAcao("EDITAR ALTERNATIVA D"):
                        nova_altD = input("DIGITE A NOVA ALTERNATIVA D DA QUESTÃO: ")
                        nova_altD = Funcoes.validarPreenchimento("DIGITE A NOVA ALTERNATIVA D DA QUESTÃO: ", nova_altD)

                        # CRIANDO CONEXÃO COM O BANCO DE DADOS
                        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                        cursor = conn.cursor()
                        Funcoes.connect(dsn)

                        # EDITANDO NO BANCO DE DADOS E NO CONSOLE
                        cursor.execute("UPDATE questao SET alt_d_questao = :nova_altD WHERE id_questao = :id_questao", {"nova_altD": nova_altD, "id_questao": questao_buscada.id_questao})
                        cursor.connection.commit()
                        questao_buscada.altD = nova_altD
                        print("QUESTÃO EDITADA COM SUCESSO!")
                        input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")

                        # FECHANDO CONEXÃO COM O BANCO DE DADOS
                        Funcoes.disconnect(conn, cursor)

                    else:
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 2):
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

            elif (opcao == 7):
                # (ADMIN) EDITAR A ALTERNATIVA E DA QUESTÃO - OK
                opcao = int(input(Funcoes.confirmarAcao("EDITAR ALTERNATIVA E")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao("EDITAR ALTERNATIVA E")))

                if (opcao == 1):
                    if Funcoes.confirmarAcao("EDITAR ALTERNATIVA E"):
                        nova_altE = input("DIGITE A NOVA ALTERNATIVA E DA QUESTÃO: ")
                        nova_altE = Funcoes.validarPreenchimento("DIGITE A NOVA ALTERNATIVA E DA QUESTÃO: ", nova_altE)

                        # CRIANDO CONEXÃO COM O BANCO DE DADOS
                        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                        cursor = conn.cursor()
                        Funcoes.connect(dsn)

                        # EDITANDO NO BANCO DE DADOS E NO CONSOLE
                        cursor.execute("UPDATE questao SET alt_e_questao = :nova_altE WHERE id_questao = :id_questao", {"nova_altE": nova_altE, "id_questao": questao_buscada.id_questao})
                        cursor.connection.commit()
                        questao_buscada.altE = nova_altE
                        print("QUESTÃO EDITADA COM SUCESSO!")
                        input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")

                        # FECHANDO CONEXÃO COM O BANCO DE DADOS
                        Funcoes.disconnect(conn, cursor)

                    else:
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 2):
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

            elif (opcao == 8):
                # (ADMIN) EDITAR A ALTERNATIVA E DA QUESTÃO - OK
                opcao = int(input(Funcoes.confirmarAcao("EDITAR RESPOSTA")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao("EDITAR RESPOSTA")))

                if (opcao == 1):
                    if Funcoes.confirmarAcao("EDITAR RESPOSTA"):
                        opcao = int(input(Funcoes.menuAdminRespostas()))
                        opcao = Funcoes.validarOpcao(opcao, 1, 25, Funcoes.menuAdminRespostas())
                        if opcao == 1:
                            nova_resposta = 'A'
                        elif opcao == 2:
                            nova_resposta = 'AB'
                        elif opcao == 3:
                            nova_resposta = 'AC'
                        elif opcao == 4:
                            nova_resposta = 'AD'
                        elif opcao == 5:
                            nova_resposta = 'AE'
                        elif opcao == 6:
                            nova_resposta = 'B'
                        elif opcao == 7:
                            nova_resposta = 'BA'
                        elif opcao == 8:
                            nova_resposta = 'BC'
                        elif opcao == 9:
                            nova_resposta = 'BD'
                        elif opcao == 10:
                            nova_resposta = 'BE'
                        elif opcao == 11:
                            nova_resposta = 'C'
                        elif opcao == 12:
                            nova_resposta = 'CA'
                        elif opcao == 13:
                            nova_resposta = 'CB'
                        elif opcao == 14:
                            nova_resposta = 'CD'
                        elif opcao == 15:
                            nova_resposta = 'CE'
                        elif opcao == 16:
                            nova_resposta = 'D'
                        elif opcao == 17:
                            nova_resposta = 'DA'
                        elif opcao == 18:
                            nova_resposta = 'DB'
                        elif opcao == 19:
                            nova_resposta = 'DC'
                        elif opcao == 20:
                            nova_resposta = 'DE'
                        elif opcao == 21:
                            nova_resposta = 'E'
                        elif opcao == 22:
                            nova_resposta = 'EA'
                        elif opcao == 23:
                            nova_resposta = 'EB'
                        elif opcao == 24:
                            nova_resposta = 'EC'
                        elif opcao == 25:
                            nova_resposta = 'ED'

                        # CRIANDO CONEXÃO COM O BANCO DE DADOS
                        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                        cursor = conn.cursor()
                        Funcoes.connect(dsn)

                        # EDITANDO NO BANCO DE DADOS E NO CONSOLE
                        cursor.execute("UPDATE questao SET resposta_questao = :nova_resposta WHERE id_questao = :id_questao", {"nova_resposta": nova_resposta, "id_questao": questao_buscada.id_questao})
                        cursor.connection.commit()
                        questao_buscada.resposta = nova_resposta
                        print("RESPOSTA EDITADA COM SUCESSO!")
                        input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")

                        # FECHANDO CONEXÃO COM O BANCO DE DADOS
                        Funcoes.disconnect(conn, cursor)

                    else:
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 2):
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

            elif (opcao == 9):
                # (ADMIN) SAIR DO MENU EDITAR QUESTÃO - OK
                perfilQuestao = 0

    def perfilQuestao(questao_buscada):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {questao_buscada.id_questao}\n"
        retornoPerfil += f"02. PERGUNTA: {questao_buscada.pergunta}\n"
        retornoPerfil += f"03. ALTERNATIVA A: {questao_buscada.altA}\n"
        retornoPerfil += f"04. ALTERNATIVA B: {questao_buscada.altB}\n"
        retornoPerfil += f"05. ALTERNATIVA C: {questao_buscada.altC}\n"
        retornoPerfil += f"06. ALTERNATIVA D: {questao_buscada.altD}\n"
        retornoPerfil += f"07. ALTERNATIVA E: {questao_buscada.altE}\n"
        retornoPerfil += f"08. RESPOSTA: {questao_buscada.resposta}\n"
        retornoPerfil += "09. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil
            
