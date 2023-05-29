import cx_Oracle

from typing import List
from Funcoes import Funcoes

class Aula:
    def __init__(self, id_aula=None, nome_aula=None, descricao_aula=None, conteudo_aula=None, url_video_aula=None, url_audio_aula=None):
        self._id_aula = id_aula
        self._nome_aula = nome_aula
        self._descricao_aula = descricao_aula
        self._conteudo_aula = conteudo_aula
        self._url_video_aula = url_video_aula
        self._url_audio_aula = url_audio_aula
        
    @property
    def id_aula(self):
        return self._id_aula
    
    @id_aula.setter
    def id_aula(self, id_aula):
        self._id_aula = id_aula
    
    @property
    def nome_aula(self):
        return self._nome_aula
    
    @nome_aula.setter
    def nome_aula(self, nome_aula):
        self._nome_aula = nome_aula

    @property
    def descricao_aula(self):
        return self._descricao_aula
    
    @descricao_aula.setter
    def descricao_aula(self, descricao_aula):
        self._descricao_aula = descricao_aula
    
    @property
    def conteudo_aula(self):
        return self._conteudo_aula
    
    @conteudo_aula.setter
    def conteudo_aula(self, conteudo_aula):
        self._conteudo_aula = conteudo_aula
    
    @property
    def url_video_aula(self):
        return self._url_video_aula
    
    @url_video_aula.setter
    def url_video_aula(self, url_video_aula):
        self._url_video_aula = url_video_aula

    @property
    def url_audio_aula(self):
        return self._url_audio_aula
    
    @url_audio_aula.setter
    def url_audio_aula(self, url_audio_aula):
        self._url_audio_aula = url_audio_aula

    def cadastrarAula(dsn, id_aula, listaAulas):
        # INSTANCIANDO NOVA AULA - OK
        nova_aula = Aula()

        Funcoes.menuCabecalho

        # SETANDO O ID DA NOVA AULA - OK
        id_aula = id_aula
        nova_aula.id_aula = id_aula

        # SETANDO O NOME DA AULA - OK
        nome_aula = input("DIGITE O NOME DA AULA: ")
        nome_aula = Funcoes.validarPreenchimento("DIGITE O NOME DA AULA: ", nome_aula)
        nova_aula.nome_aula = nome_aula

        # SETANDO A DESCRIÇÃO DA AULA - OK
        descricao_aula = input("DIGITE A DESCRIÇÃO DA AULA: ")
        descricao_aula = Funcoes.validarPreenchimento("DIGITE A DESCRIÇÃO DA AULA: ", descricao_aula)
        nova_aula.descricao_aula = descricao_aula

        # SETANDO O CONTEÚDO DA AULA - OK
        conteudo_aula = input("DIGITE O CONTEÚDO DA AULA: ")
        conteudo_aula = Funcoes.validarPreenchimento("DIGITE O CONTEÚDO DA AULA: ", conteudo_aula)
        nova_aula.conteudo_aula = conteudo_aula

        # SETANDO A URL DE VÍDEO DA AULA - OK
        url_video_aula = input("DIGITE A URL DE VÍDEO DA AULA: ")
        url_video_aula = Funcoes.validarPreenchimento("DIGITE A URL DE VÍDEO DA AULA: ", url_video_aula)
        nova_aula.url_video_aula = url_video_aula

        # SETANDO A URL DE ÁUDIO DA AULA - OK
        url_audio_aula = input("DIGITE A URL DE ÁUDIO DA AULA: ")
        url_audio_aula = Funcoes.validarPreenchimento("DIGITE A URL DE ÁUDIO DA AULA: ", url_audio_aula)
        nova_aula.url_audio_aula = url_audio_aula

        # ADICIONANDO A AULA NA LISTA DE AULAS - OK
        nova_aula = Aula(id_aula = id_aula, descricao_aula = descricao_aula, nome_aula = nome_aula, conteudo_aula = conteudo_aula, url_video_aula = url_video_aula, url_audio_aula = url_audio_aula)
        listaAulas.append(nova_aula)

        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        cursor = conn.cursor()
        Funcoes.connect(dsn)

        # CADASTRANDO NO BANCO DE DADOS
        cursor.execute("INSERT INTO aula (id_aula, nome_aula, descricao_aula, conteudo_aula, url_video_aula, url_audio_aula) VALUES (:1, :2, :3, :4, :5, :6)", (nova_aula.id_aula, nova_aula.nome_aula, nova_aula.descricao_aula, nova_aula.conteudo_aula, nova_aula.url_video_aula, nova_aula.url_audio_aula))
        cursor.connection.commit()

        # FECHANDO CONEXÃO COM O BANCO DE DADOS
        Funcoes.disconnect(conn, cursor)

        print("AULA CADASTRADA COM SUCESSO!")
        input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")

    def editarAula(self, dsn, listaAulas):
        perfilAula = 1
        Funcoes.exibirAulasAdmin(listaAulas)
        id_buscado = int(input("DIGITE O ID DA AULA QUE DESEJA EDITAR: \n"))
        aula_buscada = Funcoes.buscarPorIdAula(id_buscado, listaAulas)
        aula_buscada = Funcoes.validarAulaBuscada(aula_buscada, listaAulas)

        while (perfilAula == 1):
            opcao = int(input(Aula.perfilAula(aula_buscada)))
            opcao = Funcoes.validarOpcao(opcao, 1, 7, Aula.perfilAula(aula_buscada))

            if (opcao == 1):
                # (ADMIN) EDITAR O ID DA AULA  - OK
                input(Funcoes.editarNegativo())
            
            elif (opcao == 2):
                # (ADMIN) EDITAR O NOME DA AULA - OK
                opcao = int(input(Funcoes.confirmarAcao("EDITAR NOME")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao("EDITAR NOME")))
                
                if (opcao == 1):
                    novo_nome = input("DIGITE O NOVO NOME: ")
                    novo_nome = Funcoes.validarPreenchimento("DIGITE O NOVO NOME: ", novo_nome)

                    # CRIANDO CONEXÃO COM O BANCO DE DADOS
                    conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                    cursor = conn.cursor()
                    Funcoes.connect(dsn)

                    # EDITANDO NO BANCO DE DADOS E NO CONSOLE
                    cursor.execute("UPDATE aula SET nome_aula = :novo_nome WHERE id_aula = :id_aula", {"novo_nome": novo_nome, "id_aula": aula_buscada.id_aula})
                    cursor.connection.commit()
                    aula_buscada.nome_aula = novo_nome
                    print("NOME DA AULA EDITADO COM SUCESSO!")
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

                    # FECHANDO CONEXÃO COM O BANCO DE DADOS
                    Funcoes.disconnect(conn, cursor)

                elif (opcao == 2):
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

            elif (opcao == 3):
                # (ADMIN) EDITAR A DESCRIÇÃO DA AULA - OK
                opcao = int(input(Funcoes.confirmarAcao("EDITAR DESCRIÇÃO")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao("EDITAR DESCRIÇÃO")))

                if (opcao == 1):
                    nova_descricao = input("DIGITE A NOVA DESCRIÇÃO: ")
                    nova_descricao = Funcoes.validarPreenchimento("DIGITE A NOVA DESCRIÇÃO: ", nova_descricao)

                    # CRIANDO CONEXÃO COM O BANCO DE DADOS
                    conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                    cursor = conn.cursor()
                    Funcoes.connect(dsn)

                    # EDITANDO NO BANCO DE DADOS E NO CONSOLE
                    cursor.execute("UPDATE aula SET descricao_aula = :nova_descricao WHERE id_aula = :id_aula", {"nova_descricao": nova_descricao, "id_aula": aula_buscada.id_aula})
                    cursor.connection.commit()
                    aula_buscada.descricao_aula = nova_descricao
                    print("DESCRIÇÃO DA AULA EDITADO COM SUCESSO!")
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

                    # FECHANDO CONEXÃO COM O BANCO DE DADOS
                    Funcoes.disconnect(conn, cursor)

                elif (opcao == 2):
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
                
            elif (opcao == 4):
                # (ADMIN) EDITAR O CONTEÚDO DA AULA - OK
                opcao = int(input(Funcoes.confirmarAcao("EDITAR CONTEÚDO")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao("EDITAR CONTEÚDO")))

                if (opcao == 1):
                    novo_conteudo = input("DIGITE O NOVO CONTEÚDO: ")
                    novo_conteudo = Funcoes.validarPreenchimento("DIGITE O NOVO CONTEÚDO: ", novo_conteudo)

                    # CRIANDO CONEXÃO COM O BANCO DE DADOS
                    conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                    cursor = conn.cursor()
                    Funcoes.connect(dsn)

                    # EDITANDO NO BANCO DE DADOS E NO CONSOLE
                    cursor.execute("UPDATE aula SET conteudo_aula = :novo_conteudo WHERE id_aula = :id_aula", {"novo_conteudo": novo_conteudo, "id_aula": aula_buscada.id_aula})
                    cursor.connection.commit()
                    aula_buscada.conteudo_aula = novo_conteudo
                    print("CONTEÚDO DA AULA EDITADO COM SUCESSO!")
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

                    # FECHANDO CONEXÃO COM O BANCO DE DADOS
                    Funcoes.disconnect(conn, cursor)
                
                elif (opcao == 2):
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

            elif (opcao == 5):
                # (ADMIN) EDITAR A URL DE VÍDEO DA AULA - OK
                opcao = int(input(Funcoes.confirmarAcao("EDITAR URL DE VÍDEO")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao("EDITAR URL DE VÍDEO")))
                
                if (opcao == 1):
                    nova_url_video = input("DIGITE A NOVA URL DE VÍDEO: ")
                    nova_url_video = Funcoes.validarPreenchimento("DIGITE A NOVA URL DE VÍDEO: ", nova_url_video)

                    # CRIANDO CONEXÃO COM O BANCO DE DADOS
                    conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                    cursor = conn.cursor()
                    Funcoes.connect(dsn)

                    # EDITANDO NO BANCO DE DADOS E NO CONSOLE
                    cursor.execute("UPDATE aula SET url_video_aula = :nova_url_video WHERE id_aula = :id_aula", {"nova_url_video": nova_url_video, "id_aula": aula_buscada.id_aula})
                    cursor.connection.commit()
                    aula_buscada.url_video_aula = nova_url_video
                    print("URL DE VÍDEO DA AULA EDITADA COM SUCESSO!")
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

                    # FECHANDO CONEXÃO COM O BANCO DE DADOS
                    Funcoes.disconnect(conn, cursor)

                elif (opcao == 2):
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

            elif (opcao == 6):
                # (ADMIN) EDITAR A URL DE ÁUDIO DA AULA - OK
                opcao = int(input(Funcoes.confirmarAcao("EDITAR URL DE ÁUDIO")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao("EDITAR URL DE ÁUDIO")))

                if (opcao == 1):
                    nova_url_audio = input("DIGITE A NOVA URL DE ÁUDIO: ")
                    nova_url_audio = Funcoes.validarPreenchimento("DIGITE A NOVA URL DE ÁUDIO: ", nova_url_audio)

                    # CRIANDO CONEXÃO COM O BANCO DE DADOS
                    conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                    cursor = conn.cursor()
                    Funcoes.connect(dsn)

                    # EDITANDO NO BANCO DE DADOS E NO CONSOLE
                    cursor.execute("UPDATE aula SET url_audio_aula = :nova_url_audio WHERE id_aula = :id_aula", {"nova_url_audio": nova_url_audio, "id_aula": aula_buscada.id_aula})
                    cursor.connection.commit()
                    aula_buscada.nova_url_audio = nova_url_audio
                    print("URL DE ÁUDIO DA AULA EDITADA COM SUCESSO!")
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

                    # FECHANDO CONEXÃO COM O BANCO DE DADOS
                    Funcoes.disconnect(conn, cursor)

                elif (opcao == 2):
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

            elif (opcao == 7):
                # (ADMIN) SAIR DO MENU EDITAR AULA - OK
                perfilAula = 0

    def perfilAula(aula_buscada):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {aula_buscada.id_aula}\n"
        retornoPerfil += f"02. NOME: {aula_buscada.nome_aula}\n"
        retornoPerfil += f"03. DESCRIÇÃO: {aula_buscada.descricao_aula}\n"
        retornoPerfil += f"04. CONTEÚDO: {aula_buscada.conteudo_aula}\n"
        retornoPerfil += f"05. URL DE VÍDEO: {aula_buscada.url_video_aula}\n"
        retornoPerfil += f"06. URL DE ÁUDIO: {aula_buscada.url_audio_aula}\n"
        retornoPerfil += "07. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil
