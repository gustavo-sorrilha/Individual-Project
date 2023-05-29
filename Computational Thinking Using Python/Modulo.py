import cx_Oracle

from typing import List
from Aula import Aula
from Level import Level
from Funcoes import Funcoes
from Questao import Questao

class Modulo:
    def __init__(self, id_modulo = None, nome_modulo = None, url_imagem_modulo = None, level_modulo = None, aulas_modulo = None, questoes_modulo = None):
        self._id_modulo = id_modulo
        self._nome_modulo = nome_modulo
        self._url_imagem_modulo = url_imagem_modulo
        self._level_modulo = level_modulo
        self._aulas_modulo = aulas_modulo if aulas_modulo is not None else []
        self._questoes_modulo = questoes_modulo if questoes_modulo is not None else []

    def add_aula(self, aula: Aula):
        self._aulas_modulo.append(aula)

    def remove_aula(self, aula: Aula):
        if aula in self._aulas_modulo:
            self._aulas_modulo.remove(aula)

    def listar_aulas(self):
        if not self._aulas_modulo:
            print("Não há aulas cadastradas nesse módulo.")
        else:
            print(f"Lista de aulas do módulo {self.nome_modulo}:")
            for aula in self._aulas_modulo:
                print(f"ID: {aula.id_aula} | Nome: {aula.nome_aula}")

    def add_questao(self, questao: Questao):
        self._questoes_modulo.append(questao)

    def remove_questao(self, questao: Questao):
        if questao in self._questoes_modulo:
            self._questoes_modulo.remove(questao)

    def listar_questoes(self):
        if not self._questoes_modulo:
            print("Não há questões cadastradas nesse módulo.")
        else:
            print(f"Lista de questões do módulo {self.nome_modulo}:")
            for questao in self._questoes_modulo:
                print(f"ID: {questao.id_aula} | Pergunta: {questao.pergunta}")

    @property
    def id_modulo(self) -> int:
        return self._id_modulo
    
    @id_modulo.setter
    def id_modulo(self, valor: int):
        self._id_modulo = valor

    @property
    def nome_modulo(self) -> str:
        return self._nome_modulo
    
    @nome_modulo.setter
    def nome_modulo(self, valor: str):
        self._nome_modulo = valor

    @property
    def url_imagem_modulo(self) -> str:
        return self._url_imagem_modulo
    
    @url_imagem_modulo.setter
    def url_imagem_modulo(self, valor: str):
        self._url_imagem_modulo = valor

    @property
    def level_modulo(self) -> Level:
        return self._level_modulo
    
    @level_modulo.setter
    def level_modulo(self, valor: Level):
        self._level_modulo = valor

    @property
    def aulas_modulo(self) -> List[Aula]:
        return self._aulas_modulo

    @aulas_modulo.setter
    def aulas_modulo(self, aulas: List[Aula]):
        self._aulas_modulo = aulas
    
    def add_aula(self, aula):
        self._aulas_modulo.append(aula)
    
    def remove_aula(self, aula):
        self._aulas_modulo.remove(aula)

    @property
    def questoes_modulo(self) -> List[Questao]:
        return self._questoes_modulo

    @questoes_modulo.setter
    def questoes_modulo(self, questoes: List[Questao]):
        self._questoes_modulo = questoes
    
    def add_questao(self, questao):
        self._questoes_modulo.append(questao)
    
    def remove_questao(self, questao):
        self._questoes_modulo.remove(questao)

    def cadastrarModulo(dsn, id_modulo, listaModulos, listaAulas, listaQuestoes):
        # INSTANCIANDO NOVO MÓDULO - OK
        novo_modulo = Modulo()

        Funcoes.menuCabecalho

        # SETANDO O ID DO NOVO MÓDULO - OK
        novo_modulo.id_modulo = id_modulo

        # SETANDO O NOME DO NOVO MÓDULO - OK
        nome_modulo = input("DIGITE O NOME DO MÓDULO: ")
        nome_modulo = Funcoes.validarPreenchimento("DIGITE O NOME DO MÓDULO: ", nome_modulo)
        novo_modulo.nome_modulo = nome_modulo

        # SETANDO A URL DE IMAGEM DO NOVO MÓDULO - OK
        url_imagem_modulo = input("DIGITE A URL DA IMAGEM DO MÓDULO: ")
        url_imagem_modulo = Funcoes.validarPreenchimento("DIGITE A URL DA IMAGEM DO MÓDULO: ", url_imagem_modulo)
        novo_modulo.url_imagem_modulo = url_imagem_modulo

        # SETANDO O LEVEL DO NOVO MÓDULO - OK
        level_modulo = int(input(f"QUAL O LEVEL DO MÓDULO?" + "\n" +
                            "01. Iniciante" + "\n" +
                            "02. Intermediário" + "\n" + 
                            "03. Avançado" + "\n" + 
                            Funcoes.menuRodape()))

        level_modulo = Funcoes.validarOpcao(level_modulo, 1, 3, f"QUAL O LEVEL DO MÓDULO?" + "\n" +
                            "01. Iniciante" + "\n" +
                            "02. Intermediário" + "\n" + 
                            "03. Avançado" + "\n" + 
                            Funcoes.menuRodape())
        
        level_map = {1: "Iniciante", 2: "Intermediário", 3: "Avançado"}
        level_modulo = level_map.get(level_modulo)

        novo_modulo.level_modulo = level_modulo

        # SETANDO AS AULAS DO NOVO MÓDULO - OK
        selecionar_aulas = 1
        aulas_modulo = []

        if (len(listaAulas) == 0):
            print("NÃO EXISTEM AULAS CADASTRADAS")
        
        else:
            while (selecionar_aulas == 1):
                print(Funcoes.exibirAulasAdmin(listaAulas))
                id_aula = int(input("DIGITE O ID DA AULA QUE DESEJA ADICIONAR A ESTE NOVO MÓDULO: "))
                id_aula = Funcoes.validarPreenchimento("DIGITE O ID DA AULA QUE DESEJA ADICIONAR A ESTE NOVO MÓDULO: ", id_aula)

                for aula in listaAulas:
                    if aula.id_aula == id_aula:
                        aula_selecionada = aula
                
                if aula_selecionada is not None:
                    aulaNovaEdit = {
                        'id_aula': aula_selecionada.id_aula,
                        'nome_aula': aula_selecionada.nome_aula,
                        'descricao_aula': aula_selecionada.descricao_aula,
                        'conteudo_aula': aula_selecionada.conteudo_aula,
                        'url_video_aula': aula_selecionada.url_video_aula,
                        'url_audio_aula': aula_selecionada.url_audio_aula
                    }

                    aulas_modulo.append(aulaNovaEdit)
                else:
                    print("AULA NÃO ENCONTRADA")
                
                print("------------------------------------------")
                opcao = int(input("DESEJA ADICIONAR NOVA AULA?" + "\n" +
                                "01. SIM" + "\n" +
                                "02. NÃO" + "\n"))
                opcao = int(Funcoes.validarOpcao(opcao,1,2, "DESEJA ADICIONAR NOVA AULA?" + "\n" +
                                "01. SIM" + "\n" +
                                "02. NÃO" + "\n"))
                
                if (opcao == 1):
                    selecionar_aulas = 1
                
                elif (opcao == 2):
                    selecionar_aulas = 0

        # SETANDO AS QUESTÕES DO NOVO MÓDULO - OK
        selecionar_questoes = 1
        questoes_modulo = []

        if (len(listaQuestoes) == 0):
            print("NÃO EXISTEM QUESTÕES CADASTRADAS")
        
        else:
            while (selecionar_questoes == 1):
                print(Funcoes.exibirQuestoesAdmin(listaQuestoes))
                id_questao = int(input("DIGITE O ID DA QUESTÃO QUE DESEJA ADICIONAR A ESTE NOVO MÓDULO: "))
                id_questao = Funcoes.validarPreenchimento("DIGITE O ID DA QUESTÃO QUE DESEJA ADICIONAR A ESTE NOVO MÓDULO: ", id_questao)

                for questao in listaQuestoes:
                    if questao.id_questao == id_questao:
                        questao_selecionada = questao
                
                if questao_selecionada is not None:
                    questaoNovaEdit = {
                        'id_questao': questao_selecionada.id_questao,
                        'pergunta': questao_selecionada.pergunta,
                        'altA': questao_selecionada.altA,
                        'altB': questao_selecionada.altB,
                        'altC': questao_selecionada.altC,
                        'altD': questao_selecionada.altD,
                        'altE': questao_selecionada.altE,
                        'resposta': questao_selecionada.resposta
                    }

                    questoes_modulo.append(questaoNovaEdit)
                else:
                    print("QUESTÃO NÃO ENCONTRADA")
                
                print("------------------------------------------")
                opcao = int(input("DESEJA ADICIONAR NOVA QUESTÃO?" + "\n" +
                                "01. SIM" + "\n" +
                                "02. NÃO" + "\n"))
                opcao = int(Funcoes.validarOpcao(opcao,1,2, "DESEJA ADICIONAR NOVA QUESTÃO?" + "\n" +
                                "01. SIM" + "\n" +
                                "02. NÃO" + "\n"))
                
                if (opcao == 1):
                    selecionar_questoes = 1
                
                elif (opcao == 2):
                    selecionar_questoes = 0

        # ADICIONANDO O MÓDULO NA LISTA DE MÓDULOS - OK
        novo_modulo = Modulo(id_modulo = id_modulo, nome_modulo = nome_modulo, url_imagem_modulo = url_imagem_modulo, level_modulo = level_modulo, aulas_modulo = aulas_modulo, questoes_modulo = questoes_modulo)
        listaModulos.append(novo_modulo)

        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        cursor = conn.cursor()
        Funcoes.connect(dsn)

        # CADASTRANDO NO BANCO DE DADOS
        cursor.execute("INSERT INTO modulo (id_modulo, nome_modulo, url_imagem_modulo, nivel_modulo) VALUES (:1, :2, :3, :4)", (novo_modulo.id_modulo, novo_modulo.nome_modulo, novo_modulo.url_imagem_modulo, novo_modulo.level_modulo))
        cursor.connection.commit()

        for aula in aulas_modulo:
            cursor.execute("INSERT INTO modulo_aula (id_modulo, id_aula) VALUES (:1, :2)", (novo_modulo.id_modulo, aula.get('id_aula')))
        cursor.connection.commit()

        for questao in questoes_modulo:
            cursor.execute("INSERT INTO modulo_questao (id_modulo, id_questao) VALUES (:1, :2)", (novo_modulo.id_modulo, questao.get('id_questao')))
        cursor.connection.commit()

        # FECHANDO CONEXÃO COM O BANCO DE DADOS
        Funcoes.disconnect(conn, cursor)

        print("MÓDULO CADASTRADO COM SUCESSO!")
        input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")

    def editarModulo(self, dsn, listaModulos, listaAulas, listaQuestoes):
        perfilModulo = 1
        Funcoes.exibirModulosAdmin(listaModulos)
        id_buscado = int(input("DIGITE O ID DO MÓDULO QUE DESEJA EDITAR: \n"))
        modulo_buscado = Funcoes.buscarPorIdModulo(id_buscado, listaModulos)
        modulo_buscado = Funcoes.validarModuloBuscado(modulo_buscado, listaModulos)

        while (perfilModulo == 1):
            opcao = int(input(Modulo.perfilModulo(modulo_buscado)))
            opcao = Funcoes.validarOpcao(opcao, 1, 7, Modulo.perfilModulo(modulo_buscado))

            if (opcao == 1):
                # (ADMIN) EDITAR ID DO MÓDULO  - OK
                input(Funcoes.editarNegativo()) 
                
            elif (opcao == 2):
                # (ADMIN) EDITAR NOME DO MÓDULO - OK
                opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O NOME DO MÓDULO {modulo_buscado.nome_modulo}")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O NOME DO MÓDULO {modulo_buscado.nome_modulo}")))
                
                if (opcao == 1):
                    # (ADMIN) EDITAR O NOME DO MÓDULO - SIM - OK
                    novo_nome = input("DIGITE O NOVO NOME: ")
                    novo_nome = Funcoes.validarPreenchimento("DIGITE O NOVO NOME: ", novo_nome)

                    # CRIANDO CONEXÃO COM O BANCO DE DADOS
                    conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                    cursor = conn.cursor()
                    Funcoes.connect(dsn)

                    # EDITANDO NO BANCO DE DADOS E NO CONSOLE
                    cursor.execute("UPDATE modulo SET nome_modulo = :novo_nome WHERE id_modulo = :id_modulo", {"novo_nome": novo_nome, "id_modulo": modulo_buscado.id_modulo})
                    cursor.connection.commit()
                    modulo_buscado.nome_modulo = novo_nome
                    print("NOME DO MÓDULO EDITADO COM SUCESSO!")
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

                    # FECHANDO CONEXÃO COM O BANCO DE DADOS
                    Funcoes.disconnect(conn, cursor)
                
                elif (opcao == 2):
                    # (ADMIN) EDITAR O NOME DO MÓDULO - NÃO - OK
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
            
            elif (opcao == 3):
                # (ADMIN) EDITAR A URL DE IMAGEM DO MÓDULO - OK
                opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A URL DE IMAGEM DO MÓDULO {modulo_buscado.url_imagem_modulo}")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A URL DE IMAGEM DO MÓDULO {modulo_buscado.url_imagem_modulo}")))
                
                if (opcao == 1):
                    # (ADMIN) EDITAR A URL DE IMAGEM DO MÓDULO - SIM - OK
                    nova_url_imagem = input("DIGITE A NOVA URL DE IMAGEM: ")
                    nova_url_imagem = Funcoes.validarPreenchimento("DIGITE A NOVA URL DE IMAGEM: ", nova_url_imagem)

                    # CRIANDO CONEXÃO COM O BANCO DE DADOS
                    conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                    cursor = conn.cursor()
                    Funcoes.connect(dsn)

                    # EDITANDO NO BANCO DE DADOS E NO CONSOLE
                    cursor.execute("UPDATE modulo SET url_imagem_modulo = :nova_url_imagem WHERE id_modulo = :id_modulo", {"nova_url_imagem": nova_url_imagem, "id_modulo": modulo_buscado.id_modulo})
                    cursor.connection.commit()
                    modulo_buscado.url_imagem = nova_url_imagem
                    print("URL DE IMAGEM DO MÓDULO EDITADA COM SUCESSO!")
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

                    # FECHANDO CONEXÃO COM O BANCO DE DADOS
                    Funcoes.disconnect(conn, cursor)
                
                elif (opcao == 2):
                    # (ADMIN) EDITAR A URL DE IMAGEM DO MÓDULO - NÃO - OK
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

            elif (opcao == 4):
                # (ADMIN) EDITAR O LEVEL DO MÓDULO - OK
                opcao = int(input(Funcoes.confirmarAcao("EDITAR NÍVEL")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao("EDITAR NÍVEL")))

                if (opcao == 1):
                    level_modulo = int(input(f"QUAL O LEVEL DO MÓDULO?" + "\n" +
                                "01. Iniciante" + "\n" +
                                "02. Intermediário" + "\n" + 
                                "03. Avançado" + "\n" + 
                                Funcoes.menuRodape()))

                    level_modulo = Funcoes.validarOpcao(level_modulo, 1, 3, level_modulo)

                    level_map = {1: "Iniciante", 2: "Intermediário", 3: "Avançado"}
                    level_modulo = level_map.get(level_modulo)

                    # CRIANDO CONEXÃO COM O BANCO DE DADOS
                    conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                    cursor = conn.cursor()
                    Funcoes.connect(dsn)

                    # EDITANDO NO BANCO DE DADOS E NO CONSOLE
                    cursor.execute("UPDATE modulo SET nivel_modulo = :level_modulo WHERE id_modulo = :id_modulo", {"level_modulo": level_modulo, "id_modulo": modulo_buscado.id_modulo})
                    cursor.connection.commit()
                    modulo_buscado.level_modulo = level_modulo
                    input("LEVEL DO MÓDULO EDITADO COM SUCESSO! TECLE ENTER PARA SEGUIR.")

                    # FECHANDO CONEXÃO COM O BANCO DE DADOS
                    Funcoes.disconnect(conn, cursor)
                
                elif (opcao == 2):
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
                
            elif (opcao == 5):
                # (ADMIN) EDITAR AS AULAS DO MÓDULO - OK
                opcao = int(input(Funcoes.confirmarAcao("EDITAR AULAS")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao("EDITAR AULAS")))

                if (opcao == 1):

                    selecionar_aulas = 1
                    aulas_modulo = []

                    if (len(listaAulas) == 0):
                        input("NÃO EXISTEM AULAS CADASTRADAS. TECLE ENTER PARA SEGUIR.")
                    
                    else:
                        while (selecionar_aulas == 1):
                            Funcoes.exibirAulasAdmin(listaAulas)
                            id_aula = int(input("DIGITE O ID DA AULA QUE DESEJA ADICIONAR A ESTE MÓDULO: "))
                            id_aula = Funcoes.validarPreenchimento("DIGITE O ID DA AULA QUE DESEJA ADICIONAR A ESTE NOVO MÓDULO: ", id_aula)
                            aula_buscada = Funcoes.buscarPorIdAula(id_aula, listaAulas)
                            aula_buscada = Funcoes.validarAulaBuscada(aula_buscada, listaAulas)
                            
                            for aula in listaAulas:
                                if aula == aula_buscada:
                                    aula_selecionada = aula_buscada
                            
                            if aula_selecionada is not None:
                                aulaNovaEdit = {
                                    'id_aula': aula_selecionada.id_aula,
                                    'nome_aula': aula_selecionada.nome_aula,
                                    'descricao_aula': aula_selecionada.descricao_aula,
                                    'conteudo_aula': aula_selecionada.conteudo_aula,
                                    'url_video_aula': aula_selecionada.url_video_aula,
                                    'url_audio_aula': aula_selecionada.url_audio_aula
                                }

                                aulas_modulo.append(aulaNovaEdit)
                            else:
                                print("AULA NÃO ENCONTRADA")
                            
                            print("------------------------------------------")
                            opcao = int(input("DESEJA ADICIONAR NOVA AULA?" + "\n" +
                                            "01. SIM" + "\n" +
                                            "02. NÃO" + "\n"))
                            opcao = int(Funcoes.validarOpcao(opcao,1,2, "DESEJA ADICIONAR NOVA AULA?" + "\n" +
                                            "01. SIM" + "\n" +
                                            "02. NÃO" + "\n"))
                            
                            if (opcao == 1):
                                selecionar_aulas = 1
                            
                            elif (opcao == 2):
                                selecionar_aulas = 0
                        
                        # CRIANDO CONEXÃO COM O BANCO DE DADOS
                        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                        cursor = conn.cursor()
                        Funcoes.connect(dsn)

                        try:
                            # EDITANDO NO BANCO DE DADOS E NO CONSOLE
                            cursor.execute("DELETE FROM modulo_aula WHERE id_modulo = :1", (modulo_buscado.id_modulo,))
                            cursor.connection.commit()

                            for aula in aulas_modulo:
                                cursor.execute("INSERT INTO modulo_aula (id_modulo, id_aula) VALUES (:1, :2)", (modulo_buscado.id_modulo, aula.get('id_aula')))
                            cursor.connection.commit()

                            modulo_buscado.aulas_modulo = aulas_modulo
                            input("AULAS DO MÓDULO EDITADAS COM SUCESSO! TECLE ENTER PARA SEGUIR.")
                        except Exception as e:
                            print("ERRO AO EDITAR AS AULAS DO MÓDULO: ", e)
                            conn.rollback()
                        finally:
                            # FECHANDO CONEXÃO COM O BANCO DE DADOS
                            Funcoes.disconnect(conn, cursor)
                
                elif (opcao == 2):
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

            elif (opcao == 6):
                # (ADMIN) EDITAR AS QUESTÕES DO MÓDULO - OK
                opcao = int(input(Funcoes.confirmarAcao("EDITAR QUESTÕES")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao("EDITAR QUESTÕES")))

                if (opcao == 1):
                    selecionar_questoes = 1
                    questoes_modulo = []

                    if (len(listaQuestoes) == 0):
                        input("NÃO EXISTEM QUESTÕES CADASTRADAS. TECLE ENTER PARA SEGUIR")
                    
                    else:
                        while (selecionar_questoes == 1):
                            Funcoes.exibirQuestoesAdmin(listaQuestoes)
                            id_questao = int(input("DIGITE O ID DA QUESTÃO QUE DESEJA ADICIONAR A ESTE NOVO MÓDULO: "))
                            id_questao = Funcoes.validarPreenchimento("DIGITE O ID DA QUESTÃO QUE DESEJA ADICIONAR A ESTE NOVO MÓDULO: ", id_questao)
                            questao_buscada = Funcoes.buscarPorIdQuestao(id_questao, listaQuestoes)
                            questao_buscada = Funcoes.validarQuestaoBuscada(questao_buscada, listaQuestoes)
                            
                            for questao in listaQuestoes:
                                if questao == questao_buscada:
                                    questao_selecionada = questao_buscada
                            
                            if questao_selecionada is not None:
                                questaoNovaEdit = {
                                    'id_questao': questao_selecionada.id_questao,
                                    'pergunta': questao_selecionada.pergunta,
                                    'altA': questao_selecionada.altA,
                                    'altB': questao_selecionada.altB,
                                    'altC': questao_selecionada.altC,
                                    'altD': questao_selecionada.altD,
                                    'altE': questao_selecionada.altE,
                                    'resposta': questao_selecionada.resposta
                                }

                                questoes_modulo.append(questaoNovaEdit)
                            else:
                                print("QUESTÃO NÃO ENCONTRADA")
                            
                            print("------------------------------------------")
                            opcao = int(input("DESEJA ADICIONAR NOVA QUESTÃO?" + "\n" +
                                            "01. SIM" + "\n" +
                                            "02. NÃO" + "\n"))
                            opcao = int(Funcoes.validarOpcao(opcao,1,2, "DESEJA ADICIONAR NOVA QUESTÃO?" + "\n" +
                                            "01. SIM" + "\n" +
                                            "02. NÃO" + "\n"))
                            
                            if (opcao == 1):
                                selecionar_questoes = 1
                            
                            elif (opcao == 2):
                                selecionar_questoes = 0

                        # CRIANDO CONEXÃO COM O BANCO DE DADOS
                        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                        cursor = conn.cursor()
                        Funcoes.connect(dsn)

                        try:
                            # EDITANDO NO BANCO DE DADOS E NO CONSOLE
                            cursor.execute("DELETE FROM modulo_questao WHERE id_modulo = :1", (modulo_buscado.id_modulo,))
                            cursor.connection.commit()

                            for questao in questoes_modulo:
                                cursor.execute("INSERT INTO modulo_questao (id_modulo, id_questao) VALUES (:1, :2)", (modulo_buscado.id_modulo, questao.get('id_questao')))
                            cursor.connection.commit()

                            modulo_buscado.questoes_modulo = questoes_modulo
                            input("QUESTÕES DO MÓDULO EDITADAS COM SUCESSO! TECLE ENTER PARA SEGUIR.")
                        except Exception as e:
                            print("ERRO AO EDITAR AS QUESTÕES DO MÓDULO: ", e)
                            conn.rollback()
                        finally:
                            # FECHANDO CONEXÃO COM O BANCO DE DADOS
                            Funcoes.disconnect(conn, cursor)

                        # FECHANDO CONEXÃO COM O BANCO DE DADOS
                        Funcoes.disconnect(conn, cursor)
                
                elif (opcao == 2):
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

            elif (opcao == 7):
                # (ADMIN) SAIR DO MENU EDITAR MÓDULO - OK
                perfilModulo = 0
                
    def perfilModulo(modulo_buscado):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {modulo_buscado.id_modulo}\n"
        retornoPerfil += f"02. NOME: {modulo_buscado.nome_modulo}\n"
        retornoPerfil += f"03. URL IMAGEM: {modulo_buscado.url_imagem_modulo}\n"
        retornoPerfil += f"04. LEVEL: {modulo_buscado.level_modulo}\n"

        retornoPerfil += "05. AULAS: "
        if len(modulo_buscado.aulas_modulo) == 0:
            retornoPerfil += "NENHUMA AULA CADASTRADA\n"
        else:
            for i, aula in enumerate(modulo_buscado.aulas_modulo):
                if (i == 0):
                    retornoPerfil += f"\n 05.{i+1}. ID: {aula.get('id_aula')} | NOME: {aula.get('nome_aula')}\n"
                else:
                    retornoPerfil += f" 05.{i+1}. ID: {aula.get('id_aula')} | NOME: {aula.get('nome_aula')}\n"
        
        retornoPerfil += "06. QUESTÕES: "
        if len(modulo_buscado.questoes_modulo) == 0:
            retornoPerfil += "NENHUMA QUESTÃO CADASTRADA\n"
        else:
            for i, questao in enumerate(modulo_buscado.questoes_modulo):
                if (i == 0):
                    retornoPerfil += f"\n 06.{i+1}. ID: {questao.get('id_questao')} | PERGUNTA: {questao.get('pergunta')}\n"
                else:
                    retornoPerfil += f" 06.{i+1}. ID: {questao.get('id_questao')} | PERGUNTA: {questao.get('pergunta')}\n"

        retornoPerfil += "07. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil
        