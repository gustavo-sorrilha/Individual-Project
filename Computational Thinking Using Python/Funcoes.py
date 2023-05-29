from datetime import datetime
import time
from tqdm import tqdm
import cx_Oracle

class Funcoes:

    # MENUS - OK
    def menuCabecalho():
        return ("==> STOCKWAVE - CHALLENGE B3 - CURSO DE IPO <==\n"
        "------------------------------------------\n")

    def menuRodape():
        return ("------------------------------------------\n"
        "DIGITE A OPÇÃO DESEJADA: \n")

    def menuInicial(): 
        return (Funcoes.menuCabecalho() + 
            "01. LOGIN ADMIN\n"
            "02. SAIR\n" +
            Funcoes.menuRodape())

    def menuAdmin():
        return (Funcoes.menuCabecalho() +
        "01. ALUNOS\n"
        "02. PROFESSORES\n"
        "03. FUNCIONÁRIOS\n"
        "04. MÓDULOS\n"
        "05. AULAS\n"
        "06. QUESTÕES\n"
        "07. PRODUTOS\n"
        "08. SAIR\n" +
        Funcoes.menuRodape())

    def menuAdminAlunos():
        return (Funcoes.menuCabecalho() +
        "01. CADASTRAR ALUNO\n"
        "02. EXIBIR ALUNOS\n"
        "03. EDITAR ALUNO\n"
        "04. EXCLUIR ALUNO\n"
        "05. SAIR\n" +
        Funcoes.menuRodape())

    def menuAdminProfessores():
        return (Funcoes.menuCabecalho() +
        "01. CADASTRAR PROFESSOR\n"
        "02. EXIBIR PROFESSORES\n"
        "03. EDITAR PROFESSOR\n"
        "04. EXCLUIR PROFESSOR\n"
        "05. SAIR\n" +
        Funcoes.menuRodape())

    def menuAdminFuncionarios():
        return (Funcoes.menuCabecalho() +
        "01. CADASTRAR FUNCIONÁRIO\n"
        "02. EXIBIR FUNCIONÁRIOS\n"
        "03. EDITAR FUNCIONÁRIO\n"
        "04. EXCLUIR FUNCIONÁRIO\n"
        "05. SAIR\n" +
        Funcoes.menuRodape())

    def menuAdminModulos():
        return (Funcoes.menuCabecalho() +
        "01. CADASTRAR MÓDULO\n"
        "02. EXIBIR MÓDULOS\n"
        "03. EDITAR MÓDULO\n"
        "04. EXCLUIR MÓDULO\n"
        "05. SAIR\n" +
        Funcoes.menuRodape())

    def menuAdminAulas():
        return (Funcoes.menuCabecalho() +
        "01. CADASTRAR AULA\n"
        "02. EXIBIR AULAS\n"
        "03. EDITAR AULA\n"
        "04. EXCLUIR AULA\n"
        "05. SAIR\n" +
        Funcoes.menuRodape())

    def menuAdminQuestoes():
        return (Funcoes.menuCabecalho() +
        "01. CADASTRAR QUESTÃO\n"
        "02. EXIBIR QUESTÕES\n"
        "03. EDITAR QUESTÃO\n"
        "04. EXCLUIR QUESTÃO\n"
        "05. SAIR\n" +
        Funcoes.menuRodape())

    def menuAdminRespostas():
        return (Funcoes.menuCabecalho() +
        "ALTERNATIVAS:\n"
        "01. A\n"
        "02. AB\n"
        "03. AC\n"
        "04. AD\n"
        "05. AE\n"
        "06. B\n"
        "07. BA\n"
        "08. BC\n"
        "09. BD\n"
        "10. BE\n"
        "11. C\n"
        "12. CA\n"
        "13. CB\n"
        "14. CD\n"
        "15. CE\n"
        "16. D\n"
        "17. DA\n"
        "18. DB\n"
        "19. DC\n"
        "20. DE\n"
        "21. E\n"
        "22. EA\n"
        "23. EB\n"
        "24. EC\n"
        "25. ED\n" +
        Funcoes.menuRodape())

    def menuAdminProdutos(): 
        return (Funcoes.menuCabecalho() +
        "01. CADASTRAR PRODUTO\n"
        "02. EXIBIR PRODUTOS\n"
        "03. EDITAR PRODUTO\n"
        "04. EXCLUIR PRODUTO\n"
        "05. SAIR\n" +
        Funcoes.menuRodape())

    def menuAdminCertificados():
        return (Funcoes.menuCabecalho() +
        "01. CADASTRAR CERTIFICADO\n"
        "02. EXIBIR CERTIFICADOS\n"
        "03. EDITAR CERTIFICADO\n"
        "04. EXCLUIR CERTIFICADO\n"
        "05. SAIR\n" +
        Funcoes.menuRodape())

    def menuAluno():
        return (Funcoes.menuCabecalho() +
        "01. MEU PERFIL\n"
        "02. APRENDER\n"
        "03. RANKING\n"
        "04. LOJA\n"
        "05. SAIR\n" +
        Funcoes.menuRodape())

    def menuAlunoAprenderIniciante():
        return (Funcoes.menuCabecalho() +
        "01. Iniciante\n"
        "02. SAIR\n" +
        Funcoes.menuRodape())

    def menuAlunoAprenderIntermediario():
        return (Funcoes.menuCabecalho() +
        "01. Iniciante\n"
        "02. Intermediário\n"
        "03. SAIR\n" +
        Funcoes.menuRodape())

    def menuAlunoAprenderAvancado():
        return (Funcoes.menuCabecalho() +
        "01. Iniciante\n"
        "02. Intermediário\n"
        "03. Avançado\n"
        "04. SAIR\n" +
        Funcoes.menuRodape())

    def menuRanking():
        return (Funcoes.menuCabecalho() +
        "01. ALUNO 01 - MOEDAS 09\n"
        "02. ALUNO 02 - MOEDAS 06\n"
        "03. ALUNO 03 - MOEDAS 02\n" +
        Funcoes.menuRodape())

    def menuLoja():
        return (Funcoes.menuCabecalho() +
        "01. IPO NUBANK - VALOR: 3 MOEDAS - QUANTIDADE: 10\n"
        "02. IPO VALE - VALOR: 100 MOEDAS - QUANTIDADE: 5\n"
        "03. IPO PETROBRAS - VALOR: 1 MOEDAS - QUANTIDADE: 0\n"
        "04. SAIR\n" +
        Funcoes.menuRodape())

    # CONFIRMAR - OK
    def confirmarAcao(acao):
        return ("TEM CERTEZA QUE DESEJA " + acao + "?\n"
        "01. SIM\n"
        "02. NÃO\n"
        "------------------------------------------\n"
        "DIGITE A OPÇÃO DESEJADA: \n")
    
    # VALIDAR E VERIFICAR - OK
    def validarCPF(cpf_usuario):
        if (cpf_usuario == "00000000000" or cpf_usuario == "11111111111" or cpf_usuario == "22222222222" or cpf_usuario == "33333333333" or cpf_usuario == "44444444444" or cpf_usuario == "55555555555" or cpf_usuario == "66666666666" or cpf_usuario == "77777777777" or cpf_usuario == "88888888888" or cpf_usuario == "99999999999" or (len(cpf_usuario) != 11)):
            return False

        dig10, dig11 = '', ''
        sm, r, peso = 0, 0, 0
        for i in range(9):
            num = int(cpf_usuario[i])
            sm += num * (10 - i)
        r = 11 - sm % 11
        if (r == 10 or r == 11):
            dig10 = '0'
        else:
            dig10 = str(r)

        sm = 0
        peso = 11
        for i in range(10):
            num = int(cpf_usuario[i])
            sm += num * peso
            peso -= 1
        r = 11 - sm % 11
        if (r == 10 or r == 11):
            dig11 = '0'
        else:
            dig11 = str(r)

        if (dig10 == cpf_usuario[9] and dig11 == cpf_usuario[10]):
            return True
        else:
            return False
    
    def validarOpcao(opcao, opcao_min, opcao_max, menu):
        while opcao is None or opcao < opcao_min or opcao > opcao_max:
            print("OPÇÃO INVÁLIDA! DIGITE UM NÚMERO ENTRE {} E {}.".format(opcao_min, opcao_max))
            input("TECLE ENTER PARA VOLTAR AO MENU.")
            try:
                opcao = int(input(menu))
            except ValueError:
                print("ERRO: DIGITE UM NÚMERO INTEIRO VÁLIDO!")
        return opcao

    def validarPreenchimento(stringRepeticao, campopreenchido) -> str:
        while (len(str(campopreenchido)) == 0) or (str(campopreenchido) == "") or (str(campopreenchido) == None) or (str(campopreenchido) == "\r"):
            print("O PREENCHIMENTO DO CAMPO É OBRIGATÓRIO.")
            campopreenchido = input(stringRepeticao)
            
        return str(campopreenchido) if isinstance(campopreenchido, str) else campopreenchido

    def validarSenha(senha_usuario, conf_senha):
        while ((senha_usuario != conf_senha) or (len(senha_usuario) == 0) or (senha_usuario == "") or (senha_usuario == None) or (senha_usuario == "\r")):
            input("SENHAS NÃO CONFEREM OU SENHA INVÁLIDA. TECLE ENTER PARA CADASTRAR NOVA SENHA")
            senha_usuario = input("DIGITE A SUA SENHA: ")
            conf_senha = input("CONFIRME A SUA SENHA: ")
        return senha_usuario

    def validarUsuarioBuscado(usuario_buscado, lista):
        while (usuario_buscado == None):
            input("ID INVÁLIDO. TECLE ENTER PARA VOLTAR AO MENU")
            Funcoes.exibirUsuariosAdmin(lista)
            id_buscado = int(input("DIGITE O ID DO USUÁRIO NOVAMENTE: \n"))
            usuario_buscado = Funcoes.buscarPorIdUsuario(id_buscado, lista)
        
        return usuario_buscado

    def validarModuloBuscado(modulo_buscado, listaModulos):
        while (modulo_buscado == None):
            input("ID INVÁLIDO. TECLE ENTER PARA VOLTAR AO MENU")
            Funcoes.exibirModulosAdmin(listaModulos)
            id_buscado = int(input("DIGITE O ID DO MÓDULO NOVAMENTE: \n"))
            modulo_buscado = Funcoes.buscarPorIdModulo(id_buscado, listaModulos)
        
        return modulo_buscado

    def validarAulaBuscada(aula_buscada, listaAulas):
        while (aula_buscada == None):
            input("ID INVÁLIDO. TECLE ENTER PARA VOLTAR AO MENU")
            Funcoes.exibirAulasAdmin(listaAulas)
            id_buscado = int(input("DIGITE O ID DA AULA NOVAMENTE: \n"))
            aula_buscada = Funcoes.buscarPorIdAula(id_buscado, listaAulas)
        
        return aula_buscada

    def validarQuestaoBuscada(questao_buscada, listaQuestoes):
        while (questao_buscada == None):
            input("ID INVÁLIDO. TECLE ENTER PARA VOLTAR AO MENU")
            Funcoes.exibirQuestoesAdmin(listaQuestoes)
            id_buscado = int(input("DIGITE O ID DA QUESTÃO NOVAMENTE: \n"))
            questao_buscada = Funcoes.buscarPorIdQuestao(id_buscado, listaQuestoes)
        
        return questao_buscada

    def validarProdutoBuscado(produto_buscado, listaProdutos):
        while (produto_buscado == None):
            input("ID INVÁLIDO. TECLE ENTER PARA VOLTAR AO MENU")
            Funcoes.exibirProdutosAdmin(listaProdutos)
            id_buscado = int(input("DIGITE O ID DO PRODUTO NOVAMENTE: \n"))
            produto_buscado = Funcoes.buscarPorIdProduto(id_buscado, listaProdutos)
        
        return produto_buscado

    def verificarCPF(cpf_usuario, cpfs_cadastrados):
        while (cpf_usuario in cpfs_cadastrados or Funcoes.validarCPF(cpf_usuario) == False):
            print("CPF INVÁLIDO OU JÁ CADASTRADO.")
            cpf_usuario = input("DIGITE O SEU CPF (APENAS NÚMEROS, EXEMPLO: 43102154278): ")
        
        return cpf_usuario

    def verificarEmail(email_usuario, emails_cadastrados):
        while (email_usuario in emails_cadastrados or email_usuario == ""):
            print("EMAIL INVÁLIDO OU JÁ CADASTRADO.")
            email_usuario = input("DIGITE O SEU EMAIL: ")
        
        return email_usuario

    # FORMATAR - OK
    def formatarCpf(cpf_usuario):
        cpf_usuario_formatado = '{}.{}.{}-{}'.format(cpf_usuario[:3], cpf_usuario[3:6], cpf_usuario[6:9], cpf_usuario[9:])
        return cpf_usuario_formatado

    def formatarData(data):
        if isinstance(data, str):
            data = datetime.strptime(data, "%d/%m/%Y")
        data_formatada = data.strftime("%d/%m/%Y")
        return data_formatada

    # BUSCAR - OK
    def buscarPorIdUsuario(id_buscado, lista):
        objeto_buscado = lista.get(id_buscado)
        if objeto_buscado is None:
            return None
        return objeto_buscado
    
    def buscarPorIdModulo(id_buscado, lista):
        for modulo in lista:
            if modulo.id_modulo == id_buscado:
                return modulo
        return None

    def buscarPorIdAula(id_buscado, lista):
        for aula in lista:
            if aula.id_aula == id_buscado:
                return aula
        return None

    def buscarPorIdQuestao(id_buscado, lista):
        for questao in lista:
            if questao.id_questao == id_buscado:
                return questao
        return None

    def buscarPorIdProduto(id_buscado, lista):
        for produto in lista:
            if produto.id_produto == id_buscado:
                return produto
        return None

    # EDITAR - OK
    def editarNegativo():
        return("NÃO É POSSÍVEL EDITAR ESTA OPÇÃO.\n"
            "TECLE ENTER PARA VOLTAR AO MENU")

    def editarNome(dsn, usuario_buscado):
        novo_nome = input("DIGITE O NOVO NOME: ")
        novo_nome = Funcoes.validarPreenchimento("DIGITE O NOVO NOME: ", novo_nome)
        usuario_buscado.nome_usuario = novo_nome

        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        cursor = conn.cursor()
        Funcoes.connect(dsn)

        cursor.execute("UPDATE usuario SET nome_usuario = :novo_nome WHERE id_usuario = :id_usuario", {"novo_nome": novo_nome, "id_usuario": usuario_buscado.id_usuario})
        cursor.connection.commit()
        print("NOME DO USUÁRIO EDITADO COM SUCESSO!")

        # FECHANDO CONEXÃO COM O BANCO DE DADOS
        Funcoes.disconnect(conn, cursor)

    def editarEmail(dsn, usuario_buscado, emails_cadastrados, Aluno):
        novo_email = input("DIGITE O NOVO EMAIL: ")
        novo_email = Funcoes.validarPreenchimento("DIGITE O NOVO EMAIL: ", novo_email)
        novo_email = Funcoes.verificarEmail(novo_email, emails_cadastrados)
        if isinstance(usuario_buscado, Aluno):
            emails_cadastrados.remove(usuario_buscado.email_usuario)
            emails_cadastrados.add(novo_email)
        usuario_buscado.email_usuario = novo_email

        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        cursor = conn.cursor()
        Funcoes.connect(dsn)

        cursor.execute("UPDATE usuario SET email_usuario = :novo_email WHERE id_usuario = :id_usuario", {"novo_email": novo_email, "id_usuario": usuario_buscado.id_usuario})
        cursor.connection.commit()

        # FECHANDO CONEXÃO COM O BANCO DE DADOS
        Funcoes.disconnect(conn, cursor)

        print("EMAIL DO USUÁRIO EDITADO COM SUCESSO!")

    def editarDataNasc(dsn, usuario_buscado):
        nova_data_nasc = input("DIGITE A NOVA DATA DE NASCIMENTO DO USUÁRIO (DD/MM/YYYY, EXEMPLO: 22/06/1993): ")
        nova_data_nasc = Funcoes.validarPreenchimento("DIGITE A NOVA DATA DE NASCIMENTO DO USUÁRIO (DD/MM/YYYY, EXEMPLO: 22/06/1993): ", nova_data_nasc)
        data_formatada = datetime.strptime(nova_data_nasc, '%d/%m/%Y')
        data_formatada = data_formatada.strftime("%d/%m/%Y")
        usuario_buscado.data_nasc_aluno = data_formatada
        
        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        cursor = conn.cursor()
        Funcoes.connect(dsn)
        
        cursor.execute("UPDATE aluno SET dt_nasc_aluno = TO_DATE(:nova_data, 'DD/MM/YYYY') WHERE id_usuario = :id_usuario", {"nova_data": data_formatada, "id_usuario": usuario_buscado.id_usuario})
        cursor.connection.commit()
        
        # FECHANDO CONEXÃO COM O BANCO DE DADOS
        Funcoes.disconnect(conn, cursor)

        print("DATA DE NASCIMENTO DO USUÁRIO EDITADO COM SUCESSO!")

    def editarMoedas(dsn, usuario_buscado):
        try:
            moedas_adicionar = int(input(f"QUANTAS MOEDAS DESEJA ADICIONAR/SUBTRAIR DO USUÁRIO {usuario_buscado.nome_usuario}? "))
        except ValueError:
            print("POR FAVOR, DIGITE UM NÚMERO INTEIRO VÁLIDO.")
            return
        moedas_adicionar = int(Funcoes.validarPreenchimento("QUANTAS MOEDAS DESEJA ADICIONAR/SUBTRAIR DO USUÁRIO " + usuario_buscado.nome_usuario + "?", str(moedas_adicionar)))
        novas_moedas = moedas_adicionar + usuario_buscado.moedas_aluno
        usuario_buscado.moedas_aluno = novas_moedas

        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        cursor = conn.cursor()
        Funcoes.connect(dsn)

        cursor.execute("UPDATE aluno SET moedas_aluno = :novas_moedas WHERE id_usuario = :id_usuario", {"novas_moedas": novas_moedas, "id_usuario": usuario_buscado.id_usuario})
        cursor.connection.commit()

         # FECHANDO CONEXÃO COM O BANCO DE DADOS
        Funcoes.disconnect(conn, cursor)

        print("MOEDAS DO USUÁRIO ATUALIZADAS COM SUCESSO!")

    def editarLevel(dsn, usuario_buscado):
        novo_level = ("QUAL O NOVO LEVEL DO USUÁRIO {usuario_buscado['nome_usuario']}?" + "\n" +
                        "01. Iniciante" + "\n" +
                        "02. Intermediário" + "\n" + 
                        "03. Avançado" + "\n" +
                        "04. CURSO CONCLUÍDO" + "\n" + 
                        Funcoes.menuRodape())
        
        opcao = int(input(novo_level))

        opcao = int(Funcoes.validarOpcao(opcao, 1, 4, novo_level))

        if (opcao == 1):
            usuario_buscado.level_aluno = "Iniciante"

        elif (opcao == 2):
            usuario_buscado.level_aluno = "Intermediário"
        
        elif (opcao == 3):
            usuario_buscado.level_aluno = "Avançado"

        elif (opcao == 4):
            usuario_buscado.level_aluno = "CURSO CONCLUÍDO"

        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        cursor = conn.cursor()
        Funcoes.connect(dsn)
        
        cursor.execute("UPDATE aluno SET nivel_aluno = :novo_nivel WHERE id_usuario = :id_usuario", {"novo_nivel": usuario_buscado.level_aluno, "id_usuario": usuario_buscado.id_usuario})
        cursor.connection.commit()

         # FECHANDO CONEXÃO COM O BANCO DE DADOS
        Funcoes.disconnect(conn, cursor)

        print("LEVEL DO USUÁRIO ATUALIZADO COM SUCESSO!")

    def editarSenha(dsn, usuario_buscado, StringClasse):
        nova_senha_usuario = input("DIGITE A NOVA SENHA: ")
        conf_senha = input("CONFIRME A NOVA SENHA: ")
        nova_senha_usuario = Funcoes.validarSenha(nova_senha_usuario, conf_senha)

         # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        cursor = conn.cursor()
        Funcoes.connect(dsn)

        if StringClasse == "Aluno":
            usuario_buscado.senha_aluno = nova_senha_usuario
            cursor.execute("UPDATE aluno SET senha_aluno = :nova_senha_usuario WHERE id_usuario = :id_usuario", {"nova_senha_usuario": nova_senha_usuario, "id_usuario": usuario_buscado.id_usuario})
            cursor.connection.commit()
        
        elif StringClasse == "Funcionario":
            usuario_buscado.senha_funcionario = nova_senha_usuario
            cursor.execute("UPDATE funcionario SET senha_funcionario = :nova_senha_usuario WHERE id_usuario = :id_usuario", {"nova_senha_usuario": nova_senha_usuario, "id_usuario": usuario_buscado.id_usuario})
            cursor.connection.commit()
        
        # FECHANDO CONEXÃO COM O BANCO DE DADOS
        Funcoes.disconnect(conn, cursor)

        print("SENHA DO USUÁRIO EDITADA COM SUCESSO!")

    def editarCargo(dsn, usuario_buscado):
        novo_cargo = input("DIGITE O NOVO CARGO: ")
        novo_cargo = Funcoes.validarPreenchimento("DIGITE O NOVO CARGO: ", novo_cargo)
        usuario_buscado.cargo_funcionario = novo_cargo

        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        cursor = conn.cursor()
        Funcoes.connect(dsn)

        cursor.execute("UPDATE funcionario SET cargo_funcionario = :novo_cargo WHERE id_usuario = :id_usuario", {"novo_cargo": novo_cargo, "id_usuario": usuario_buscado.id_usuario})
        cursor.connection.commit()

        # FECHANDO CONEXÃO COM O BANCO DE DADOS
        Funcoes.disconnect(conn, cursor)

        print("CARGO DO FUNCIONÁRIO EDITADO COM SUCESSO!")

    # EXCLUIR - OK
    def excluirUsuario(dsn, lista, StringClasse):
        Funcoes.exibirUsuariosAdmin(lista)
        id_buscado = int(input("DIGITE O ID DO USUÁRIO QUE DESEJA EXCLUIR: \n"))
        usuario_buscado = Funcoes.buscarPorIdUsuario(id_buscado, lista)
        usuario_buscado = Funcoes.validarUsuarioBuscado(usuario_buscado, lista)
        opcao = int(input(Funcoes.confirmarAcao(f"EXCLUIR O USUÁRIO {usuario_buscado.nome_usuario}")))
        opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EXCLUIR O USUÁRIO {usuario_buscado.nome_usuario}")))
        
        if (opcao == 1):
            del lista[id_buscado]

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            cursor = conn.cursor()
            Funcoes.connect(dsn)

            if (StringClasse == "Aluno"):
                cursor.execute("DELETE FROM aluno WHERE id_usuario = :id_usuario", {"id_usuario": usuario_buscado.id_usuario})
                cursor.execute("DELETE FROM usuario WHERE id_usuario = :id_usuario", {"id_usuario": usuario_buscado.id_usuario})
                cursor.connection.commit()

            elif (StringClasse == "Professor"):
                cursor.execute("DELETE FROM professor WHERE id_usuario = :id_usuario", {"id_usuario": usuario_buscado.id_usuario})
                cursor.execute("DELETE FROM usuario WHERE id_usuario = :id_usuario", {"id_usuario": usuario_buscado.id_usuario})
                cursor.connection.commit()

            elif (StringClasse == "Funcionario"):
                cursor.execute("DELETE FROM funcionario WHERE id_usuario = :id_usuario", {"id_usuario": usuario_buscado.id_usuario})
                cursor.execute("DELETE FROM usuario WHERE id_usuario = :id_usuario", {"id_usuario": usuario_buscado.id_usuario})
                cursor.connection.commit()
            
            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

            print("USUÁRIO EXCLUÍDO COM SUCESSO!")
            input("TECLE ENTER PARA VOLTAR AO MENU.")
        
        elif (opcao == 2):
            input("TECLE ENTER PARA VOLTAR AO MENU.")

    def excluirModulo(dsn, listaModulos):
        if len(listaModulos) == 0:
            print("NÃO EXISTEM MÓDULOS CADASTRADOS. TECLE ENTER PARA VOLTAR AO MENU")
        
        else:
            Funcoes.exibirModulosAdmin(listaModulos)
            id_buscado = int(input("DIGITE O ID DO MÓDULO QUE DESEJA EXCLUIR: \n"))
            modulo_buscado = Funcoes.buscarPorIdModulo(id_buscado, listaModulos)
            modulo_buscado = Funcoes.validarModuloBuscado(modulo_buscado, listaModulos)
            opcao = int(input(Funcoes.confirmarAcao(f"EXCLUIR O MÓDULO")))
            opcao = Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EXCLUIR O MÓDULO"))
            
            if opcao == 1:
                for i in range(len(listaModulos)):
                    if listaModulos[i].id_modulo == id_buscado:
                        # CRIANDO CONEXÃO COM O BANCO DE DADOS
                        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                        cursor = conn.cursor()
                        Funcoes.connect(dsn)

                        # EXCLUINDO DO BANCO DE DADOS E DA LISTA
                        cursor.execute("DELETE FROM modulo_aula WHERE id_modulo = :1", (listaModulos[i].id_modulo,))
                        cursor.connection.commit()

                        cursor.execute("DELETE FROM modulo_questao WHERE id_modulo = :1", (listaModulos[i].id_modulo,))
                        cursor.connection.commit()

                        cursor.execute("DELETE FROM modulo WHERE id_modulo = :1", (listaModulos[i].id_modulo,))
                        cursor.connection.commit()

                        del listaModulos[i]

                        # FECHANDO CONEXÃO COM O BANCO DE DADOS
                        Funcoes.disconnect(conn, cursor)

                        print("MÓDULO EXCLUÍDO COM SUCESSO!")
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                        break
                
            elif opcao == 2:
                input("TECLE ENTER PARA VOLTAR AO MENU.")
    
    def excluirAula(dsn, listaAulas):
        if len(listaAulas) == 0:
            print("NÃO EXISTEM AULAS CADASTRADOS. TECLE ENTER PARA VOLTAR AO MENU")
        
        else:
            Funcoes.exibirAulasAdmin(listaAulas)
            id_buscado = int(input("DIGITE O ID DA AULA QUE DESEJA EXCLUIR: \n"))
            aula_buscada = Funcoes.buscarPorIdAula(id_buscado, listaAulas)
            aula_buscada = Funcoes.validarAulaBuscada(aula_buscada, listaAulas)
            opcao = int(input(Funcoes.confirmarAcao(f"EXCLUIR A AULA")))
            opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EXCLUIR A AULA")))
            
            if (opcao == 1):
                for i in range(len(listaAulas)):
                    if listaAulas[i].id_aula == id_buscado:
                        # CRIANDO CONEXÃO COM O BANCO DE DADOS
                        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                        cursor = conn.cursor()
                        Funcoes.connect(dsn)

                        # EXCLUINDO DO BANCO DE DADOS E DA LISTA
                        cursor.execute("DELETE FROM modulo_aula WHERE id_aula = :1", (listaAulas[i].id_aula,))
                        cursor.connection.commit()

                        cursor.execute("DELETE FROM aula WHERE id_aula = :1", (listaAulas[i].id_aula,))
                        cursor.connection.commit()

                        del listaAulas[i]

                        # FECHANDO CONEXÃO COM O BANCO DE DADOS
                        Funcoes.disconnect(conn, cursor)

                        print("AULA EXCLUÍDA COM SUCESSO!")
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
            
            elif (opcao == 2):
                input("TECLE ENTER PARA VOLTAR AO MENU.")
    
    def excluirQuestao(dsn, listaQuestoes):
        if len(listaQuestoes) == 0:
            print("NÃO EXISTEM QUESTÕES CADASTRADAS. TECLE ENTER PARA VOLTAR AO MENU")
        
        else:
            Funcoes.exibirQuestoesAdmin(listaQuestoes)
            id_buscado = int(input("DIGITE O ID DA QUESTÃO QUE DESEJA EXCLUIR: \n"))
            questao_buscada = Funcoes.buscarPorIdQuestao(id_buscado, listaQuestoes)
            questao_buscada = Funcoes.validarQuestaoBuscada(questao_buscada, listaQuestoes)
            opcao = int(input(Funcoes.confirmarAcao(f"EXCLUIR A QUESTÃO")))
            opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EXCLUIR A QUESTÃO")))
            
            if (opcao == 1):
                for i in range(len(listaQuestoes)):
                    if listaQuestoes[i].id_questao == id_buscado:
                        # CRIANDO CONEXÃO COM O BANCO DE DADOS
                        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                        cursor = conn.cursor()
                        Funcoes.connect(dsn)

                        # EXCLUINDO DO BANCO DE DADOS E DA LISTA
                        cursor.execute("DELETE FROM modulo_questao WHERE id_questao = :1", (listaQuestoes[i].id_questao,))
                        cursor.connection.commit()

                        cursor.execute("DELETE FROM questao WHERE id_questao = :1", (listaQuestoes[i].id_questao,))
                        cursor.connection.commit()

                        del listaQuestoes[i]

                        # FECHANDO CONEXÃO COM O BANCO DE DADOS
                        Funcoes.disconnect(conn, cursor)

                        print("QUESTÃO EXCLUÍDA COM SUCESSO!")
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                        
            elif (opcao == 2):
                input("TECLE ENTER PARA VOLTAR AO MENU.")

    def excluirProduto(dsn, listaProdutos):
        if len(listaProdutos) == 0:
            print("NÃO EXISTEM PRODUTOS CADASTRADOS. TECLE ENTER PARA VOLTAR AO MENU")
        
        else:
            Funcoes.exibirProdutosAdmin(listaProdutos)
            id_buscado = int(input("DIGITE O ID DO PRODUTO QUE DESEJA EXCLUIR: \n"))
            produto_buscado = Funcoes.buscarPorIdProduto(id_buscado, listaProdutos)
            produto_buscado = Funcoes.validarAulaBuscada(produto_buscado, listaProdutos)
            opcao = int(input(Funcoes.confirmarAcao(f"EXCLUIR O PRODUTO")))
            opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EXCLUIR O PRODUTO")))
            
            if (opcao == 1):
                for i in range(len(listaProdutos)):
                    if listaProdutos[i].id_produto == id_buscado:
                        # CRIANDO CONEXÃO COM O BANCO DE DADOS
                        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                        cursor = conn.cursor()
                        Funcoes.connect(dsn)

                        # EXCLUINDO DO BANCO DE DADOS E DA LISTA
                        cursor.execute("DELETE FROM produto WHERE id_produto = :1", (listaProdutos[i].id_produto,))
                        cursor.connection.commit()

                        del listaProdutos[i]

                        # FECHANDO CONEXÃO COM O BANCO DE DADOS
                        Funcoes.disconnect(conn, cursor)

                        print("PRODUTO EXCLUÍDO COM SUCESSO!")
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
            
            elif (opcao == 2):
                input("TECLE ENTER PARA VOLTAR AO MENU.")
    
    # EXIBIR - OK
    def exibirUsuariosAdmin(dicionario):
        Funcoes.menuCabecalho()

        if len(dicionario) == 0:
            print("NÃO EXISTEM USUÁRIOS CADASTRADOS.")
        else:
            for id_usuario, usuario in dicionario.items():
                print(f"ID: {id_usuario} | CPF: {Funcoes.formatarCpf(usuario.cpf_usuario)} | NOME: {usuario.nome_usuario}")
                print("------------------------------------------")

    def exibirModulosAdmin(listaModulos):
        Funcoes.menuCabecalho()

        if len(listaModulos) == 0:
            print("NÃO EXISTEM MÓDULOS CADASTRADOS.")
        else:
            for modulo in listaModulos:
                print(f"ID: {modulo.id_modulo} | NOME DO MÓDULO: {modulo.nome_modulo}")
                print(f"------------------------------------------")

    def exibirAulasAdmin(listaAulas):

        Funcoes.menuCabecalho

        if len(listaAulas) == 0:
            print("NÃO EXISTEM AULAS CADASTRADAS.")
        else:
            for aula in listaAulas:
                print(f"ID: {aula.id_aula} | NOME DA AULA: {aula.nome_aula}") 
                print(f"------------------------------------------")
    
    def exibirQuestoesAdmin(listaQuestoes):
        
        Funcoes.menuCabecalho

        if len(listaQuestoes) == 0:
            print("NÃO EXISTEM QUESTÕES CADASTRADAS.")
        else:
            for questao in listaQuestoes:
                print(f"ID: {questao.id_questao} | PERGUNTA DA QUESTÃO: {questao.pergunta}") 
                print(f"------------------------------------------")

    def exibirProdutosAdmin(listaProdutos):

        Funcoes.menuCabecalho

        if len(listaProdutos) == 0:
            print("NÃO EXISTEM PRODUTOS CADASTRADOS.")
        else:
            for produto in listaProdutos:
                print(f"ID: {produto.id_produto} | NOME: {produto.nome_produto}") 
                print(f"------------------------------------------")

    # BANCO DE DADOS
    def connect(dsn):
        try:
            conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            return conn
        except cx_Oracle.Error as e:
            print(f"ERRO AO CONECTAR COM O BANCO DE DADOS: {e}")

    def disconnect(conn, cursor):
        try:
            if not conn.close:
                conn.close()
            if not cursor.close:
                cursor.close()
        except cx_Oracle.Error as e:
            print(f"ERRO AO DESCONECTAR DO BANCO DE DADOS: {e}")

    def buscarIdMax(dsn, coluna_tabela, nome_tabela):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            cursor = conn.cursor()
            Funcoes.connect(dsn)

            cursor.execute(f"SELECT MAX({coluna_tabela}) FROM {nome_tabela}")
            result = cursor.fetchone()
            if result[0] is None:
                id_max = 1
            else:
                id_max = result[0] + 1
            
            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)
            return id_max
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None

    def contarAulas(dsn, nivel_modulo):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            cursor = conn.cursor()
            Funcoes.connect(dsn)

            cursor.execute(f"SELECT COUNT(*) FROM aula_modulo JOIN modulo ON aula_modulo.id_modulo = modulo.id_modulo WHERE nivel_modulo = '{nivel_modulo}'")
            result = cursor.fetchone()
            if result[0] is None:
                qtd_aulas = 1
            else:
                qtd_aulas = result[0] + 1
            
            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)
            return qtd_aulas
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None

    def buscarCpfsCadastrados(dsn):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            cursor = conn.cursor()
            Funcoes.connect(dsn)

            cpfs_cadastrados = set()
            cursor.execute("SELECT cpf_usuario FROM usuario")
            results = cursor.fetchall()
            for row in results:
                cpfs_cadastrados.add(row[0])

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)
            return cpfs_cadastrados
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None

    def buscarEmailsCadastrados(dsn):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            cursor = conn.cursor()
            Funcoes.connect(dsn)

            emails_cadastrados = set()
            cursor.execute("SELECT email_usuario FROM usuario")
            results = cursor.fetchall()
            for row in results:
                emails_cadastrados.add(row[0])
            
            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)
            return emails_cadastrados
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None
    
    def buscarAlunosBanco(dsn, Aluno):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            cursor = conn.cursor()
            Funcoes.connect(dsn)

            dicAlunos = {}
            cursor.execute("""
                SELECT 
                    u.id_usuario, 
                    u.cpf_usuario, 
                    u.nome_usuario, 
                    u.email_usuario, 
                    a.dt_nasc_aluno AS data_nasc_aluno, 
                    a.dt_reg_aluno AS data_registro_aluno, 
                    a.senha_aluno AS senha_aluno, 
                    a.moedas_aluno, 
                    a.nivel_aluno 
                    FROM usuario u 
                    INNER JOIN aluno a ON a.id_usuario = u.id_usuario
                    ORDER BY u.id_usuario
            """)

            for row in cursor:
                aluno_banco = Aluno(
                    id_usuario = row[0],
                    cpf_usuario = row[1],
                    nome_usuario = row[2],
                    email_usuario = row[3],
                    data_nasc_aluno = row[4],
                    data_registro_aluno = row[5],
                    senha_aluno = row[6],
                    moedas_aluno = row[7],
                    level_aluno = row[8],
                    produtos_aluno = [],
                    certificados_aluno = []
                )

                cursor_produtos = cursor.connection.cursor()
                cursor_produtos.execute("""
                    SELECT 
                        p.nome_produto,
                        m.qtd_movimentacao 
                    FROM movimentacao m
                    INNER JOIN produto p ON p.id_produto = m.produto_movimentacao
                    WHERE m.usuario_movimentacao = :1
                    ORDER BY m.dt_movimentacao
                """, (aluno_banco.id_usuario,))

                for produto_row in cursor_produtos:
                    produto = {
                        'nome_produto': produto_row[0],
                        'qtd_produto': produto_row[1]
                    }

                    aluno_banco.produtos_aluno.append(produto)

                cursor_produtos.close()

                cursor_certificados = cursor.connection.cursor()
                cursor_certificados.execute("""
                    SELECT 
                        ac.id_certificado,
                        c.dt_certificado
                    FROM aluno_certificado ac
                    INNER JOIN certificado c ON c.id_certificado = ac.id_certificado
                    WHERE ac.id_usuario = :1
                    ORDER BY ac.id_certificado
                """, (aluno_banco.id_usuario,))

                for certificado_row in cursor_certificados:
                    certificado = {
                        'id_certificado': certificado_row[0],
                        'data_certificado': certificado_row[1]
                    }

                    aluno_banco.certificados_aluno.append(certificado)

                cursor_certificados.close()

                dicAlunos[aluno_banco.id_usuario] = aluno_banco
            
            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(dicAlunos)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE ALUNOS: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

            return dicAlunos
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None

    def buscarProfessoresBanco(dsn, Professor):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            cursor = conn.cursor()
            Funcoes.connect(dsn)

            dicProfessores = {}
            cursor.execute("""
                SELECT u.id_usuario, u.cpf_usuario, u.nome_usuario, u.email_usuario
                FROM usuario u
                INNER JOIN professor p ON u.id_usuario = p.id_usuario
                ORDER BY u.id_usuario
            """)

            for row in cursor:
                professor_banco = Professor(
                    id_usuario = row[0],
                    cpf_usuario = row[1],
                    nome_usuario = row[2],
                    email_usuario = row[3],
                )

                dicProfessores[professor_banco.id_usuario] = professor_banco
            
            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(dicProfessores)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE PROFESSORES: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

            return dicProfessores
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None

    def buscarFuncionariosBanco(dsn, Funcionario):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            cursor = conn.cursor()
            Funcoes.connect(dsn)

            dicFuncionarios = {}
            cursor.execute("""
                SELECT u.id_usuario, u.cpf_usuario, u.nome_usuario, u.email_usuario, f.senha_funcionario, f.cargo_funcionario
                FROM usuario u
                INNER JOIN funcionario f ON u.id_usuario = f.id_usuario
                ORDER BY u.id_usuario
            """)
            for row in cursor:
                funcionario_banco = Funcionario(
                    id_usuario = row[0],
                    cpf_usuario = row[1],
                    nome_usuario = row[2],
                    email_usuario = row[3],
                    senha_funcionario = row[4],
                    cargo_funcionario = row[5]
                )

                dicFuncionarios[funcionario_banco.id_usuario] = funcionario_banco
            
            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(dicFuncionarios)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE FUNCIONÁRIOS: ')
                
            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

            return dicFuncionarios
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None
        
    def buscarModulosBanco(dsn, Modulo):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            cursor = conn.cursor()
            Funcoes.connect(dsn)

            listaModulos = []
            cursor.execute("""
                SELECT * FROM modulo ORDER BY id_modulo
            """)
            
            for row in cursor:
                modulo_banco = Modulo(
                    id_modulo = row[0],
                    nome_modulo = row[1],
                    url_imagem_modulo = row[2],
                    level_modulo = row[3],
                    aulas_modulo = [],
                    questoes_modulo = []
                )

                cursor_aulas = cursor.connection.cursor()
                cursor_aulas.execute(f"""
                SELECT a.id_aula, a.nome_aula, a.descricao_aula, a.conteudo_aula, a.url_video_aula, a.url_audio_aula                
                FROM modulo m
                JOIN modulo_aula ma ON m.id_modulo = ma.id_modulo
                JOIN aula a ON a.id_aula = ma.id_aula
                JOIN nivel n ON m.nivel_modulo = n.nome_nivel
                WHERE m.id_modulo = :1
                """, (modulo_banco.id_modulo,))

                for aula_row in cursor_aulas:
                    aula = {
                        'id_aula': aula_row[0],
                        'nome_aula': aula_row[1],
                        'descricao_aula': aula_row[2],
                        'conteudo_aula': aula_row[3],
                        'url_video_aula': aula_row[4],
                        'url_audio_aula': aula_row[5]
                    }

                    modulo_banco.aulas_modulo.append(aula)

                cursor_aulas.close()

                cursor_questoes = cursor.connection.cursor()
                cursor_questoes.execute(f"""
                SELECT q.id_questao, q.pergunta_questao, q.alt_a_questao, q.alt_b_questao, q.alt_c_questao, q.alt_d_questao, q.alt_e_questao, q.resposta_questao
                FROM modulo m
                JOIN modulo_questao mq ON m.id_modulo = mq.id_modulo
                JOIN questao q ON q.id_questao = mq.id_questao
                JOIN nivel n ON m.nivel_modulo = n.nome_nivel
                JOIN resposta r ON q.resposta_questao = r.resposta
                WHERE m.id_modulo = :1
                """, (modulo_banco.id_modulo,))

                for questao_row in cursor_questoes:
                    questao = {
                        'id_questao': questao_row[0],
                        'pergunta': questao_row[1],
                        'altA': questao_row[2],
                        'altB': questao_row[3],
                        'altC': questao_row[4],
                        'altD': questao_row[5],
                        'altE': questao_row[6],
                        'resposta': questao_row[7]
                    }

                    modulo_banco.questoes_modulo.append(questao)

                cursor_questoes.close()

                listaModulos.append(modulo_banco)

            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(listaModulos)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE MÓDULOS: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

            return listaModulos
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None
    
    def buscarAulasBanco(dsn, Aula):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            cursor = conn.cursor()
            Funcoes.connect(dsn)

            listaAulas = []
            cursor.execute("""
                SELECT * FROM aula ORDER BY id_aula
            """)
            
            for row in cursor:
                aula_banco = Aula(
                    id_aula = row[0],
                    nome_aula = row[1],
                    descricao_aula = row[2],
                    conteudo_aula = row[3],
                    url_video_aula = row[4],
                    url_audio_aula = row[5]
                )

                listaAulas.append(aula_banco)

            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(listaAulas)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE AULAS: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

            return listaAulas
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None
        
    def buscarQuestoesBanco(dsn, Questao):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            cursor = conn.cursor()
            Funcoes.connect(dsn)

            listaQuestoes = []
            cursor.execute("""
                SELECT * FROM questao ORDER BY id_questao
            """)

            for row in cursor:
                questao_banco = Questao(
                    id_questao = row[0],
                    pergunta = row[1],
                    altA = row[2],
                    altB = row[3],
                    altC = row[4],
                    altD = row[5],
                    altE = row[6],
                    resposta = row[7]
                )

                listaQuestoes.append(questao_banco)

            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(listaQuestoes)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE QUESTÕES: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

            return listaQuestoes
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None

    def buscarProdutosBanco(dsn, Produto):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            cursor = conn.cursor()
            Funcoes.connect(dsn)

            listaProdutos = []
            cursor.execute("""
                SELECT * FROM produto ORDER BY id_produto
            """)
            
            for row in cursor:
                produto_banco = Produto(
                    id_produto = row[0],
                    nome_produto = row[1],
                    valor_produto = row[2],
                    qtd_produto = row[3],
                    imagem_produto = row[4]
                )

                listaProdutos.append(produto_banco)

            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(listaProdutos)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE PRODUTOS: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

            return listaProdutos
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None

    def buscarCertificadosBanco(dsn, Certificado):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            cursor = conn.cursor()
            Funcoes.connect(dsn)

            listaCertificados = []
            cursor.execute("""
                SELECT * FROM certificado ORDER BY id_certificado
            """)
            
            for row in cursor:
                certificado_banco = Certificado(
                    id_certificado = row[0],
                    data_certificado = row[1]
                )

                listaCertificados.append(certificado_banco)

            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(listaCertificados)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE CERTIFICADOS: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

            return listaCertificados
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None

    def buscarMovimentacoesBanco(dsn, Movimentacao):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            cursor = conn.cursor()
            Funcoes.connect(dsn)

            listaMovimentacoes = []
            cursor.execute("""
                SELECT * FROM movimentacao ORDER BY id_movimentacao
            """)
            
            for row in cursor:
                movimentacao_banco = Movimentacao(
                    id_movimentacao = row[0],
                    data_movimentacao = row[1],
                    usuario_movimentacao = row[2],
                    produto_movimentacao = row[3],
                    qtd_movimentacao = row[4]
                )

                listaMovimentacoes.append(movimentacao_banco)

            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(listaMovimentacoes)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE MOVIMENTAÇÕES: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

            return listaMovimentacoes
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None