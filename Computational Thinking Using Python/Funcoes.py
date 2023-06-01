from datetime import datetime
import time
from tqdm import tqdm
import Mercado
import cx_Oracle

class Funcoes:

    # MENUS - OK
    def menuCabecalho():
        return ("==> Alimente+ <==\n"
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
        "01. Beneficiarios\n"
        "02. Mercados\n"
        "03. Restaurantes\n"
        "04. Funcionarios\n"
        "05. PRODUTOS\n"
        "06. SAIR\n" +
        Funcoes.menuRodape())

    def menuAdminBeneficiario():
        return (Funcoes.menuCabecalho() +
        "01. CADASTRAR BENEFICIARIO\n"
        "02. EXIBIR Beneficiario\n"
        "03. EDITAR BENEFICIARIO\n"
        "04. EXCLUIR BENEFICIARIO\n"
        "05. SAIR\n" +
        Funcoes.menuRodape())

    def menuAdminMercados():
        return (Funcoes.menuCabecalho() +
        "01. CADASTRAR MERCADO\n"
        "02. EXIBIR MERCADOS\n"
        "03. EDITAR MERCADOS\n"
        "04. EXCLUIR MERCADOS\n"
        "05. EDITAR PRODUTOS\n"
        "06. SAIR\n" +
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

    def menuAdminProdutos(): 
        return (Funcoes.menuCabecalho() +
        "01. CADASTRAR PRODUTO\n"
        "02. EXIBIR PRODUTOS\n"
        "03. EDITAR PRODUTO\n"
        "04. EXCLUIR PRODUTO\n"
        "05. SAIR\n" +
        Funcoes.menuRodape())

    def menuBENEFICIARIO():
        return (Funcoes.menuCabecalho() +
        "01. MEU PERFIL\n"
        "02. APRENDER\n"
        "03. RANKING\n"
        "04. LOJA\n"
        "05. SAIR\n" +
        Funcoes.menuRodape())

    # CONFIRMAR - 
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
        
    def validarCNPJ(cnpj):
        if len(cnpj) != 14:
            return False

        if cnpj == cnpj[0] * 14:
            return False

        soma = 0
        peso = 5
        for i in range(12):
            soma += int(cnpj[i]) * peso
            peso -= 1
            if peso == 1:
                peso = 9
        digito1 = soma % 11
        digito1 = 0 if digito1 < 2 else 11 - digito1

        soma = 0
        peso = 6
        for i in range(13):
            soma += int(cnpj[i]) * peso
            peso -= 1
            if peso == 1:
                peso = 9
        digito2 = soma % 11
        digito2 = 0 if digito2 < 2 else 11 - digito2

        if int(cnpj[12]) == digito1 and int(cnpj[13]) == digito2:
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
    
    def verificarCNPJ(cnpj_usuario, cnpjs_cadastrados):
        while (cnpj_usuario in cnpjs_cadastrados or Funcoes.validarCNPJ(cnpj_usuario) == False):
            print("CNPJ INVÁLIDO OU JÁ CADASTRADO.")
            cnpj_usuario = input("DIGITE O SEU CNPJ (APENAS NÚMEROS, EXEMPLO: 12345678000200): ")
    
        return cnpj_usuario


    def verificarEmail(email_usuario, emails_cadastrados):
        while (email_usuario in emails_cadastrados or email_usuario == ""):
            print("EMAIL INVÁLIDO OU JÁ CADASTRADO.")
            email_usuario = input("DIGITE O SEU EMAIL: ")
        
        return email_usuario

    # FORMATAR - OK
    def formatarCpf(cpf_usuario):
        cpf_usuario_formatado = '{}.{}.{}-{}'.format(cpf_usuario[:3], cpf_usuario[3:6], cpf_usuario[6:9], cpf_usuario[9:])
        return cpf_usuario_formatado
    
    def formatarCNPJ(cnpj_usuario):
        cnpj_usuario_formatado = '{}.{}.{}/{}-{}'.format(cnpj_usuario[:2], cnpj_usuario[2:5], cnpj_usuario[5:8], cnpj_usuario[8:12], cnpj_usuario[12:])
        return cnpj_usuario_formatado

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
        ####conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        ####cursor = conn.cursor()
        ####Funcoes.connect(dsn)

        ##cursor.execute("UPDATE usuario SET nome_usuario = :novo_nome WHERE id_usuario = :id_usuario", {"novo_nome": novo_nome, "id_usuario": usuario_buscado.id_usuario})
        ####cursor.connection.commit()
        ##print("NOME DO USUÁRIO EDITADO COM SUCESSO!")

        # FECHANDO CONEXÃO COM O BANCO DE DADOS
        ####Funcoes.disconnect(conn, cursor)

    def editarEmail(dsn, usuario_buscado, emails_cadastrados, BENEFICIARIO):
        novo_email = input("DIGITE O NOVO EMAIL: ")
        novo_email = Funcoes.validarPreenchimento("DIGITE O NOVO EMAIL: ", novo_email)
        novo_email = Funcoes.verificarEmail(novo_email, emails_cadastrados)
        if isinstance(usuario_buscado, BENEFICIARIO):
            emails_cadastrados.remove(usuario_buscado.email_usuario)
            emails_cadastrados.add(novo_email)
        usuario_buscado.email_usuario = novo_email

        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        ####conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        ####cursor = conn.cursor()
        ####Funcoes.connect(dsn)

        ##cursor.execute("UPDATE usuario SET email_usuario = :novo_email WHERE id_usuario = :id_usuario", {"novo_email": novo_email, "id_usuario": usuario_buscado.id_usuario})
        ####cursor.connection.commit()

        # FECHANDO CONEXÃO COM O BANCO DE DADOS
        ######Funcoes.disconnect(conn, cursor)

        ##print("EMAIL DO USUÁRIO EDITADO COM SUCESSO!")

    def editarDataNasc(dsn, usuario_buscado):
        nova_data_nasc = input("DIGITE A NOVA DATA DE NASCIMENTO DO USUÁRIO (DD/MM/YYYY, EXEMPLO: 22/06/1993): ")
        nova_data_nasc = Funcoes.validarPreenchimento("DIGITE A NOVA DATA DE NASCIMENTO DO USUÁRIO (DD/MM/YYYY, EXEMPLO: 22/06/1993): ", nova_data_nasc)
        data_formatada = datetime.strptime(nova_data_nasc, '%d/%m/%Y')
        data_formatada = data_formatada.strftime("%d/%m/%Y")
        usuario_buscado.data_nasc_BENEFICIARIO = data_formatada
        
        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        ##conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        ##cursor = conn.cursor()
        ##Funcoes.connect(dsn)
        
       ##cursor.execute("UPDATE BENEFICIARIO SET dt_nasc_BENEFICIARIO = TO_DATE(:nova_data, 'DD/MM/YYYY') WHERE id_usuario = :id_usuario", {"nova_data": data_formatada, "id_usuario": usuario_buscado.id_usuario})
        ##cursor.connection.commit()
        
        # FECHANDO CONEXÃO COM O BANCO DE DADOS
        ####Funcoes.disconnect(conn, cursor)

        print("DATA DE NASCIMENTO DO USUÁRIO EDITADO COM SUCESSO!")

    def editarSenha(dsn, usuario_buscado, StringClasse):
        nova_senha_usuario = input("DIGITE A NOVA SENHA: ")
        conf_senha = input("CONFIRME A NOVA SENHA: ")
        nova_senha_usuario = Funcoes.validarSenha(nova_senha_usuario, conf_senha)

         # CRIANDO CONEXÃO COM O BANCO DE DADOS
        ##conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        ##cursor = conn.cursor()
        ##Funcoes.connect(dsn)

        if StringClasse == "BENEFICIARIO":
            usuario_buscado.senha_BENEFICIARIO = nova_senha_usuario
           ##cursor.execute("UPDATE BENEFICIARIO SET senha_BENEFICIARIO = :nova_senha_usuario WHERE id_usuario = :id_usuario", {"nova_senha_usuario": nova_senha_usuario, "id_usuario": usuario_buscado.id_usuario})
            ##cursor.connection.commit()
        
        elif StringClasse == "Funcionario":
            usuario_buscado.senha_funcionario = nova_senha_usuario
            cursor.execute("UPDATE funcionario SET senha_funcionario = :nova_senha_usuario WHERE id_usuario = :id_usuario", {"nova_senha_usuario": nova_senha_usuario, "id_usuario": usuario_buscado.id_usuario})
            ##cursor.connection.commit()
        
        # FECHANDO CONEXÃO COM O BANCO DE DADOS
        ####Funcoes.disconnect(conn, cursor)

        print("SENHA DO USUÁRIO EDITADA COM SUCESSO!")

    def editarCargo(dsn, usuario_buscado):
        novo_cargo = input("DIGITE O NOVO CARGO: ")
        novo_cargo = Funcoes.validarPreenchimento("DIGITE O NOVO CARGO: ", novo_cargo)
        usuario_buscado.cargo_funcionario = novo_cargo

        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        ##conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        ##cursor = conn.cursor()
        ##Funcoes.connect(dsn)

        cursor.execute("UPDATE funcionario SET cargo_funcionario = :novo_cargo WHERE id_usuario = :id_usuario", {"novo_cargo": novo_cargo, "id_usuario": usuario_buscado.id_usuario})
        ##cursor.connection.commit()

        # FECHANDO CONEXÃO COM O BANCO DE DADOS
        ####Funcoes.disconnect(conn, cursor)

        print("CARGO DO FUNCIONÁRIO EDITADO COM SUCESSO!")

    # EXCLUIR - 
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
            ##conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            ##cursor = conn.cursor()
            ##Funcoes.connect(dsn)

            if (StringClasse == "Beneficiario"):
                cursor.execute("DELETE FROM BENEFICIARIO WHERE id_usuario = :id_usuario", {"id_usuario": usuario_buscado.id_usuario})
                cursor.execute("DELETE FROM usuario WHERE id_usuario = :id_usuario", {"id_usuario": usuario_buscado.id_usuario})
                ##cursor.connection.commit()

            elif (StringClasse == "Mercado"):
                cursor.execute("DELETE FROM estabelecimento WHERE id_usuario = :id_usuario", {"id_usuario": usuario_buscado.id_usuario})
                cursor.execute("DELETE FROM usuario WHERE id_usuario = :id_usuario", {"id_usuario": usuario_buscado.id_usuario})
                ##cursor.connection.commit()

            elif (StringClasse == "Funcionario"):
                cursor.execute("DELETE FROM funcionario WHERE id_usuario = :id_usuario", {"id_usuario": usuario_buscado.id_usuario})
                cursor.execute("DELETE FROM usuario WHERE id_usuario = :id_usuario", {"id_usuario": usuario_buscado.id_usuario})
                ##cursor.connection.commit()

            elif (StringClasse == "Restaurante"):
                cursor.execute("DELETE FROM funcionario WHERE id_usuario = :id_usuario", {"id_usuario": usuario_buscado.id_usuario})
                cursor.execute("DELETE FROM usuario WHERE id_usuario = :id_usuario", {"id_usuario": usuario_buscado.id_usuario})
                ##cursor.connection.commit()    
            
            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            ####Funcoes.disconnect(conn, cursor)

            print("USUÁRIO EXCLUÍDO COM SUCESSO!")
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
                        ##conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                        ##cursor = conn.cursor()
                        ##Funcoes.connect(dsn)

                        # EXCLUINDO DO BANCO DE DADOS E DA LISTA
                        cursor.execute("DELETE FROM produto WHERE id_produto = :1", (listaProdutos[i].id_produto,))
                        ##cursor.connection.commit()

                        del listaProdutos[i]

                        # FECHANDO CONEXÃO COM O BANCO DE DADOS
                        ####Funcoes.disconnect(conn, cursor)

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
            ##conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
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
            ##conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            ##cursor = conn.cursor()
            ##Funcoes.connect(dsn)

            cursor.execute(f"SELECT MAX({coluna_tabela}) FROM {nome_tabela}")
            result = cursor.fetchone()
            if result[0] is None:
                id_max = 1
            else:
                id_max = result[0] + 1
            
            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            ####Funcoes.disconnect(conn, cursor)
            return id_max
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None

    def buscarCpfsCadastrados(dsn):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            ##conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            ##cursor = conn.cursor()
            ##Funcoes.connect(dsn)

            cpfs_cadastrados = set()
            cursor.execute("SELECT cpf_usuario FROM usuario")
            results = cursor.fetchall()
            for row in results:
                cpfs_cadastrados.add(row[0])

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            ####Funcoes.disconnect(conn, cursor)
            return cpfs_cadastrados
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None
    def buscarCnpjsCadastrados(dsn):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            ##conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            ##cursor = conn.cursor()
            ##Funcoes.connect(dsn)

            cnpjs_cadastrados = set()
            cursor.execute("SELECT cnpj_usuario FROM usuario")
            results = cursor.fetchall()
            for row in results:
                cnpjs_cadastrados.add(row[0])

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            ####Funcoes.disconnect(conn, cursor)
            return cnpjs_cadastrados
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None


    def buscarEmailsCadastrados(dsn):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            ##conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            ##cursor = conn.cursor()
            ##Funcoes.connect(dsn)

            emails_cadastrados = set()
            cursor.execute("SELECT email_usuario FROM usuario")
            results = cursor.fetchall()
            for row in results:
                emails_cadastrados.add(row[0])
            
            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            ####Funcoes.disconnect(conn, cursor)
            return emails_cadastrados
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None
    
    def buscarBeneficiarioBanco(dsn, BENEFICIARIO):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            ##conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            ##cursor = conn.cursor()
            ##Funcoes.connect(dsn)

            dicBeneficiario = {}
            cursor.execute("""
                SELECT 
                    u.id_usuario, 
                    u.cpf_usuario, 
                    u.nome_usuario, 
                    u.email_usuario, 
                    a.dt_nasc_BENEFICIARIO AS data_nasc_BENEFICIARIO, 
                    a.dt_reg_BENEFICIARIO AS data_registro_BENEFICIARIO, 
                    a.senha_BENEFICIARIO AS senha_BENEFICIARIO,  
                    FROM usuario u 
                    INNER JOIN BENEFICIARIO a ON a.id_usuario = u.id_usuario
                    ORDER BY u.id_usuario
            """)

            for row in cursor:
                BENEFICIARIO_banco = BENEFICIARIO(
                    id_usuario = row[0],
                    cpf_usuario = row[1],
                    nome_usuario = row[2],
                    email_usuario = row[3],
                    data_nasc_BENEFICIARIO = row[4],
                    data_registro_BENEFICIARIO = row[5],
                    senha_BENEFICIARIO = row[6],
                    produtos_BENEFICIARIO = [],
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
                """, (BENEFICIARIO_banco.id_usuario,))

                for produto_row in cursor_produtos:
                    produto = {
                        'nome_produto': produto_row[0],
                        'qtd_produto': produto_row[1]
                    }

                    BENEFICIARIO_banco.produtos_BENEFICIARIO.append(produto)

                cursor_produtos.close()

                for selo_row in cursor_selos:
                    selo = {
                        'id_selo': selo_row[0],
                        'data_selo': selo_row[1]
                    }

                    BENEFICIARIO_banco.selos_BENEFICIARIO.append(selo)

                ##cursor_selos.close()

                dicBeneficiario[BENEFICIARIO_banco.id_usuario] = BENEFICIARIO_banco
            
            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(dicBeneficiario)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE Beneficiario: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            ####Funcoes.disconnect(conn, cursor)

            return dicBeneficiario
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None

    def buscarEstabelecimentoBanco(dsn, Estabelecimento):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            ##conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            ##cursor = conn.cursor()
            ##Funcoes.connect(dsn)

            dicEstabelecimento = {}
            cursor.execute("""
                SELECT u.id_usuario, u.cpf_usuario, u.nome_usuario, u.email_usuario
                FROM usuario u
                INNER JOIN estabelecimento p ON u.id_usuario = p.id_usuario
                ORDER BY u.id_usuario
            """)

            for row in cursor:
                estabelecimento_banco = Estabelecimento(
                    id_usuario = row[0],
                    cnpj_usuario = row[1],
                    nome_usuario = row[2],
                    email_usuario = row[3],
                )

                dicEstabelecimento[estabelecimento_banco.id_usuario] = estabelecimento_banco
            
            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(dicEstabelecimento)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE PROFESSORES: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            ####Funcoes.disconnect(conn, cursor)

            return dicEstabelecimento
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None

    def buscarFuncionariosBanco(dsn, Funcionario):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            ##conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            ##cursor = conn.cursor()
            ##Funcoes.connect(dsn)

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
            ####Funcoes.disconnect(conn, cursor)

            return dicFuncionarios
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None

    def buscarProdutosBanco(dsn, Produto):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            ##conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            ##cursor = conn.cursor()
            ##Funcoes.connect(dsn)

            listaProdutos = []
            cursor.execute("""
                SELECT * FROM produto ORDER BY id_produto
            """)
            
            for row in cursor:
                produto_banco = Produto(
                    id_produto = row[0],
                    nome_produto = row[1],
                    tipo_produto = row[2],
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
            ####Funcoes.disconnect(conn, cursor)

            return listaProdutos
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None

    ##def buscarCertificadosBanco(dsn, Certificado):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            ##conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            ##cursor = conn.cursor()
            ##Funcoes.connect(dsn)

            listaCertificados = []
            cursor.execute("""
                SELECT * FROM selo ORDER BY id_selo
            """)
            
            for row in cursor:
                selo_banco = Certificado(
                    id_selo = row[0],
                    data_selo = row[1]
                )

                listaCertificados.append(selo_banco)

            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(listaCertificados)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE CERTIFICADOS: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            ####Funcoes.disconnect(conn, cursor)

            return listaCertificados
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None

    def buscarMovimentacoesBanco(dsn, Movimentacao):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            ##conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            ##cursor = conn.cursor()
            ##Funcoes.connect(dsn)

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
            ####Funcoes.disconnect(conn, cursor)

            return listaMovimentacoes
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None
