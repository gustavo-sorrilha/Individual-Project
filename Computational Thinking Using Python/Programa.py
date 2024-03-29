# OBSERVAÇÕES
# OS DADOS PARA VALIDAÇÃO DAS ALTERAÇÕES NO BANCO SÃO:  
# dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, sid='ORCL')
# conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
# PARA LOGAR COMO ADMIN, UTILIZAR O EMAIL "ADMIN" E A SENHA "admin"

# IMPORTANDO CLASSES - OK
from Beneficiario import Beneficiario
from Funcionario import Funcionario
from Funcoes import Funcoes
from Movimentacao import Movimentacao
from Produto import Produto
from Mercado import Mercado
from Estabelecimento import Estabelecimento
from Apis import conselhoApi
from Apis import tradutorApi
##import cx_Oracle

# ESTABELECENDO CONEXÃO COM O BANCO DE DADOS
##cx_Oracle.init_oracle_client(lib_dir=r"C:\Program Files\instantclient_21_9")
##dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, sid='ORCL')

# MENSAGEM INICIAL
print("==> Aliment+ <==")
print("------------------------------------------")
print("AGUARDE ENQUANTO O SISTEMA ESTÁ ATUALIZANDO O BANCO DE DADOS")
print("------------------------------------------")

# CRIANDO LISTAS, DICIONÁRIOS, SETS E TUPLAS - OK
dicBeneficiario = Funcoes.buscarBeneficiarioBanco(dsn, Beneficiario)
dicFuncionarios = Funcoes.buscarFuncionariosBanco(dsn, Funcionario)
listaProdutos = Funcoes.buscarProdutosBanco(dsn, Produto)
listaMovimentacoes = Funcoes.buscarMovimentacoesBanco(dsn, Movimentacao)
cpfs_cadastrados = Funcoes.buscarCpfsCadastrados(dsn)
cnpjs_cadastrados = Funcoes.buscarCnpjCadastrados(dsn)
emails_cadastrados = Funcoes.buscarEmailsCadastrados(dsn)

# DECLARANDO VARIÁVEIS INICIAIS - OK
iniciar = 1
id_usuario = Funcoes.buscarIdMax(dsn, "id_usuario", "usuario")
id_produto = Funcoes.buscarIdMax(dsn, "id_produto", "produto")
id_movimentacao = Funcoes.buscarIdMax(dsn, "id_movimentacao", "movimentacao")


while (iniciar == 1):
    # MENU INICIAL - OK
    print("------------------------------------------")
    opcao = int(input(Funcoes.menuInicial()))
    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.menuInicial()))

    if (opcao == 1):
        # (USER) EFETUAR LOGIN - OK
        print("------------------------------------------")
        email_login = input("EMAIL: ")
        senha_login = input("SENHA: ")

        for id_funcionario, funcionario in dicFuncionarios.items():
            # LOGIN DE FUNCIONÁRIO - OK
            if funcionario.email_usuario == email_login and funcionario.senha_funcionario == senha_login:
                admin = 1
                print("------------------------------------------")
                #print(f"BEM VINDO, {funcionario.nome_usuario}. DICA DO DIA: {tradutorApi(conselhoApi())}")

                while (admin == 1):
                    # EXIBIR MENU ADMIN - OK
                    opcao = int(input(Funcoes.menuAdmin()))
                    opcao = Funcoes.validarOpcao(opcao, 1, 8, Funcoes.menuAdmin())
                    
                    if (opcao == 1):
                        # (ADMIN) Beneficiario - OK
                        menuAdminBeneficiario = 1
                    
                        while (menuAdminBeneficiario == 1):
                            opcao = int(input(Funcoes.menuAdminBeneficiario()))
                            opcao = Funcoes.validarOpcao(opcao, 1, 5, Funcoes.menuAdminBeneficiario())

                            if (opcao == 1):
                                # (ADMIN) CADASTRAR Beneficiario - OK
                                Beneficiario.cadastrarBeneficiario(dsn, cpfs_cadastrados, emails_cadastrados, dicBeneficiario, id_usuario)
                                id_usuario = id_usuario + 1

                            elif (opcao == 2):
                                # (ADMIN) EXIBIR Beneficiario - OK
                                Funcoes.exibirUsuariosAdmin(dicBeneficiario)
                                input("TECLE ENTER PARA VOLTAR AO MENU\n")
                            
                            elif (opcao == 3):
                                # (ADMIN) EDITAR Beneficiario - OK
                                Beneficiario_editar = Beneficiario()
                                Beneficiario_editar.editarBeneficiario(dsn, dicBeneficiario, emails_cadastrados)
                            
                            elif (opcao == 4):
                                # (ADMIN) EXCLUIR Beneficiario - OK
                                Funcoes.excluirUsuario(dsn, dicBeneficiario, "Beneficiario")
                            
                            elif (opcao == 5):
                                # (ADMIN) SAIR DO MENU DE Beneficiario - OK
                                menuAdminBeneficiario = 0

                    elif (opcao == 2):
                        # (ADMIN) MERCADOS - OK
                        menuAdminMercados = 1

                        while (menuAdminMercados == 1):
                            opcao = int(input(Funcoes.menuAdminMercados()))
                            opcao = Funcoes.validarOpcao(opcao, 1, 5, Funcoes.menuAdminMercados())

                            if (opcao == 1):
                                # (ADMIN) CADASTRAR MERCADOS - OK
                                Mercado.cadastrarMercado(dsn, dicMercados, id_usuario)
                                id_usuario = id_usuario + 1

                            elif (opcao == 2):
                                # (ADMIN) EXIBIR MERCADOS - OK
                                Funcoes.exibirUsuariosAdmin(dicMercados)
                                input("TECLE ENTER PARA VOLTAR AO MENU\n")
                            
                            elif (opcao == 3):
                                # (ADMIN) EDITAR MERCADOS - OK
                                professor_editar = Mercado()
                                professor_editar.editarMercado(dsn, dicMercados, emails_cadastrados, Beneficiario)
                            
                            elif (opcao == 4):
                                # (ADMIN) EXCLUIR MERCADOS - OK
                                Funcoes.excluirUsuario(dsn, dicMercados, "Mercado")
                            
                            elif (opcao == 5):
                                # (ADMIN) SAIR DO MENU DE MERCADOS - OK
                                menuAdminMercados = 0

                    elif (opcao == 3):
                        # (ADMIN) FUNCIONÁRIOS - OK
                        menuAdminFuncionarios = 1

                        while (menuAdminFuncionarios == 1):
                            opcao = int(input(Funcoes.menuAdminFuncionarios()))
                            opcao = Funcoes.validarOpcao(opcao, 1, 5, Funcoes.menuAdminFuncionarios())

                            if (opcao == 1):
                                # (ADMIN) CADASTRAR FUNCIONÁRIO - OK
                                Funcionario.cadastrarFuncionario(dsn, dicFuncionarios, id_usuario)
                                id_usuario = id_usuario + 1

                            elif (opcao == 2):
                                # (ADMIN) EXIBIR FUNCIONÁRIOS - OK
                                Funcoes.exibirUsuariosAdmin(dicFuncionarios)
                                input("TECLE ENTER PARA VOLTAR AO MENU\n")
                            
                            elif (opcao == 3):
                                # (ADMIN) EDITAR FUNCIONÁRIOS - OK
                                funcionario_editar = Funcionario()
                                funcionario_editar.editarFuncionario(dsn, dicFuncionarios, emails_cadastrados, Beneficiario)
                            
                            elif (opcao == 4):
                                # (ADMIN) EXCLUIR FUNCIONÁRIO - OK
                                Funcoes.excluirUsuario(dsn, dicFuncionarios, "Funcionario")
                            
                            elif (opcao == 5):
                                # (ADMIN) SAIR DO MENU DE FUNCIONÁRIOS - OK
                                menuAdminFuncionarios = 0

                    elif (opcao == 4):
                    # (ADMIN) MÓDULOS - OK
                        menuAdminModulos = 1

                        while (menuAdminModulos == 1):
                            opcao = int(input(Funcoes.menuAdminModulos()))
                            opcao = Funcoes.validarOpcao(opcao, 1, 5, Funcoes.menuAdminModulos())

                            if (opcao == 1):
                                # (ADMIN) CADASTRAR MÓDULO - OK
                                Modulo.cadastrarModulo(dsn, id_modulo, listaModulos, listaAulas, listaQuestoes)
                                id_modulo = id_modulo + 1

                            elif (opcao == 2):
                                # (ADMIN) EXIBIR MÓDULOS - OK
                                Funcoes.exibirModulosAdmin(listaModulos)
                                input("TECLE ENTER PARA VOLTAR AO MENU\n")
                            
                            elif (opcao == 3):
                                # (ADMIN) EDITAR MÓDULO - OK
                                modulo_editar = Modulo()
                                modulo_editar.editarModulo(dsn, listaModulos, listaAulas, listaQuestoes)
                            
                            elif (opcao == 4):
                                # (ADMIN) EXCLUIR MÓDULO - OK
                                Funcoes.excluirModulo(dsn, listaModulos)
                            
                            elif (opcao == 5):
                                # (ADMIN) SAIR DO MENU DE MÓDULOS - OK
                                menuAdminModulos = 0

                    elif (opcao == 5):
                    # (ADMIN) AULAS - OK
                        menuAdminAulas = 1

                        while (menuAdminAulas == 1):
                            opcao = int(input(Funcoes.menuAdminAulas()))
                            opcao = Funcoes.validarOpcao(opcao, 1, 5, Funcoes.menuAdminAulas())

                            if (opcao == 1):
                                # (ADMIN) CADASTRAR AULA - OK
                                Aula.cadastrarAula(dsn, id_aula, listaAulas)
                                id_aula = id_aula + 1

                            elif (opcao == 2):
                                # (ADMIN) EXIBIR AULAS - OK
                                Funcoes.exibirAulasAdmin(listaAulas)
                                input("TECLE ENTER PARA VOLTAR AO MENU\n")
                            
                            elif (opcao == 3):
                                # (ADMIN) EDITAR AULA - OK
                                aula_editar = Aula()
                                aula_editar.editarAula(dsn, listaAulas)
                            
                            elif (opcao == 4):
                                # (ADMIN) EXCLUIR AULA - OK
                                Funcoes.excluirAula(dsn, listaAulas)
                            
                            elif (opcao == 5):
                                # (ADMIN) SAIR DO MENU DE AULAS - OK
                                menuAdminAulas = 0

                    elif (opcao == 6):
                    # (ADMIN) QUESTÕES - OK
                        menuAdminQuestoes = 1

                        while (menuAdminQuestoes == 1):
                            opcao = int(input(Funcoes.menuAdminQuestoes()))
                            opcao = Funcoes.validarOpcao(opcao, 1, 5, Funcoes.menuAdminQuestoes())

                            if (opcao == 1):
                                # (ADMIN) CADASTRAR QUESTÃO - OK
                                Questao.cadastrarQuestao(dsn, id_questao, listaQuestoes)
                                id_questao = id_questao + 1

                            elif (opcao == 2):
                                # (ADMIN) EXIBIR QUESTÕES - OK
                                Funcoes.exibirQuestoesAdmin(listaQuestoes)
                                input("TECLE ENTER PARA VOLTAR AO MENU\n")
                            
                            elif (opcao == 3):
                                # (ADMIN) EDITAR QUESTÃO - OK
                                questao_editar = Questao()
                                questao_editar.editarQuestao(dsn, listaQuestoes)

                            elif (opcao == 4):
                                # (ADMIN) EXCLUIR QUESTÃO - OK
                                Funcoes.excluirQuestao(dsn, listaQuestoes)
                            
                            elif (opcao == 5):
                                # (ADMIN) SAIR DO MENU DE QUESTÕES - OK
                                menuAdminQuestoes = 0
                    
                    elif (opcao == 7):
                        # (ADMIN) PRODUTOS - OK
                        menuAdminProdutos = 1

                        while (menuAdminProdutos == 1):
                            opcao = int(input(Funcoes.menuAdminProdutos()))
                            opcao = Funcoes.validarOpcao(opcao, 1, 5, Funcoes.menuAdminProdutos())

                            if (opcao == 1):
                                # (ADMIN) CADASTRAR PRODUTO - OK
                                Produto.cadastrarProduto(dsn, id_produto, listaProdutos)
                                id_produto = id_produto + 1

                            elif (opcao == 2):
                                # (ADMIN) EXIBIR PRODUTOS - OK
                                Funcoes.exibirProdutosAdmin(listaProdutos)
                                input("TECLE ENTER PARA VOLTAR AO MENU\n")

                            elif (opcao == 3):
                                # (ADMIN) EDITAR PRODUTO - OK
                                produto_editar = Produto()
                                produto_editar.editarProduto(dsn, listaProdutos)

                            elif (opcao == 4):
                                # (ADMIN) EXCLUIR PRODUTO - OK
                                Funcoes.excluirProduto(dsn, listaProdutos)

                            elif (opcao == 5):
                                # (ADMIN) SAIR DO MENU DE PRODUTOS - OK
                                menuAdminProdutos = 0

                    elif (opcao == 8):
                        # (ADMIN) SAIR - OK
                        opcao = int(input(Funcoes.confirmarAcao("SAIR")))
                        opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao("SAIR")))

                        if (opcao == 1):
                            admin = 0

                        elif (opcao == 2):
                            admin = 1

            else:
                # LOGIN INVÁLIDO - OK
                print("USUÁRIO E/OU SENHA INVÁLIDOS.")
                input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")

    elif (opcao == 2):
        # ENCERRAR O PROGRAMA - OK
        opcao = int(input(Funcoes.confirmarAcao("SAIR")))
        opcao = Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao("SAIR"))
        
        if opcao == 1:        
            print("PROGRAMA ENCERRADO.")
            iniciar = 0
            
        elif (opcao == 2):
            input("TECLE ENTER PARA VOLTAR AO MENU")


            
