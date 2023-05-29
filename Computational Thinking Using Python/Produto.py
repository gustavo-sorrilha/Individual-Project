import cx_Oracle

from typing import List
from Funcoes import Funcoes

class Produto:
    def __init__(self, id_produto=None, nome_produto=None, valor_produto=None, qtd_produto=None, imagem_produto=None):
        self._id_produto = id_produto
        self._nome_produto = nome_produto
        self._valor_produto = valor_produto
        self._qtd_produto = qtd_produto
        self._imagem_produto = imagem_produto

    @property
    def id_produto(self):
        return self._id_produto

    @id_produto.setter
    def id_produto(self, id_produto):
        self._id_produto = id_produto

    @property
    def nome_produto(self):
        return self._nome_produto

    @nome_produto.setter
    def nome_produto(self, nome_produto):
        self._nome_produto = nome_produto

    @property
    def valor_produto(self):
        return self._valor_produto

    @valor_produto.setter
    def valor_produto(self, valor_produto):
        self._valor_produto = valor_produto

    @property
    def qtd_produto(self):
        return self._qtd_produto

    @qtd_produto.setter
    def qtd_produto(self, qtd_produto):
        self._qtd_produto = qtd_produto

    @property
    def imagem_produto(self):
        return self._imagem_produto

    @imagem_produto.setter
    def imagem_produto(self, imagem_produto):
        self._imagem_produto = imagem_produto

    @staticmethod
    def from_dict(produto_dict: dict) -> 'Produto':
        return Produto(
            produto_dict['id_produto'],
            produto_dict['nome_produto'],
            produto_dict['valor_produto'],
            produto_dict['qtd_produto'],
            produto_dict['imagem_produto']
        )

    @staticmethod
    def to_dict(produto: 'Produto') -> dict:
        return {
            'id_produto': produto.id_produto,
            'nome_produto': produto.nome_produto,
            'valor_produto': produto.valor_produto,
            'qtd_produto': produto.qtd_produto,
            'imagem_produto': produto.imagem_produto
        }

    @staticmethod
    def from_list(produto_list: List[dict]) -> List['Produto']:
        return [Produto.from_dict(prod_dict) for prod_dict in produto_list]

    @staticmethod
    def to_list(produto: List['Produto']) -> List[dict]:
        return [Produto.to_dict(prod) for prod in produto]


    def cadastrarProduto(dsn, id_produto, listaProdutos):
        # INSTANCIANDO NOVO PRODUTO - OK
        novo_produto = Produto()

        Funcoes.menuCabecalho

        # SETANDO O ID DO NOVO PRODUTO - OK
        id_produto = id_produto
        novo_produto.id_produto = id_produto

        # SETANDO O NOME DO PRODUTO - OK
        nome_produto = input("DIGITE O NOME DO PRODUTO: ")
        nome_produto = Funcoes.validarPreenchimento("DIGITE O NOME DO PRODUTO: ", nome_produto)
        novo_produto.nome_produto = nome_produto

        # SETANDO O VALOR DO PRODUTO - OK
        valor_produto = float(input("DIGITE O VALOR DO PRODUTO: "))
        valor_produto = Funcoes.validarPreenchimento("DIGITE O VALOR DO PRODUTO: ", valor_produto)
        novo_produto.valor_produto = valor_produto

        # SETANDO A QUANTIDADE DO PRODUTO - OK
        qtd_produto = int(input("DIGITE A QUANTIDADE DO PRODUTO: "))
        qtd_produto = Funcoes.validarPreenchimento("DIGITE A QUANTIDADE DO PRODUTO: ", qtd_produto)
        novo_produto.qtd_produto = qtd_produto

        # SETANDO A URL DE IMAGEM DO PRODUTO - OK
        imagem_produto = input("DIGITE A URL DA IMAGEM DO PRODUTO: ")
        imagem_produto = Funcoes.validarPreenchimento("DIGITE A URL DA IMAGEM DO PRODUTO: ", imagem_produto)
        novo_produto.imagem_produto = imagem_produto

        # ADICIONANDO O PRODUTO NA LISTA DE PRODUTOS - OK
        novo_produto = Produto(id_produto = id_produto, nome_produto = nome_produto, valor_produto = valor_produto, qtd_produto = qtd_produto, imagem_produto = imagem_produto)
        listaProdutos.append(novo_produto)

        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        cursor = conn.cursor()
        Funcoes.connect(dsn)

        # CADASTRANDO NO BANCO DE DADOS
        cursor.execute("INSERT INTO produto (id_produto, nome_produto, valor_produto, qtd_produto, imagem_produto) VALUES (:1, :2, :3, :4, :5)", (novo_produto.id_produto, novo_produto.nome_produto, novo_produto.valor_produto, novo_produto.qtd_produto, novo_produto.imagem_produto))
        cursor.connection.commit()

        # FECHANDO CONEXÃO COM O BANCO DE DADOS
        Funcoes.disconnect(conn, cursor)

        print("PRODUTO CADASTRADO COM SUCESSO!")
        input("TECLE ENTER PARA VOLTAR AO MENU INICIAL\n")

    def editarProduto(self, dsn, listaProdutos):
        perfilProduto = 1
        Funcoes.exibirProdutosAdmin(listaProdutos)
        id_buscado = int(input("DIGITE O ID DO PRODUTO QUE DESEJA EDITAR: \n"))
        produto_buscado = Funcoes.buscarPorIdProduto(id_buscado, listaProdutos)
        produto_buscado = Funcoes.validarProdutoBuscado(produto_buscado, listaProdutos)

        while (perfilProduto == 1):
            opcao = int(input(Produto.perfilProduto(produto_buscado)))
            opcao = Funcoes.validarOpcao(opcao, 1, 6, Produto.perfilProduto(produto_buscado))

            if (opcao == 1):
                # (ADMIN) EDITAR O ID DO PRODUTO  - OK
                input(Funcoes.editarNegativo())
            
            elif (opcao == 2):
                # (ADMIN) EDITAR O NOME DO PRODUTO - OK
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
                    cursor.execute("UPDATE produto SET nome_produto = :novo_nome WHERE id_produto = :id_produto", {"novo_nome": novo_nome, "id_produto": produto_buscado.id_produto})
                    cursor.connection.commit()
                    produto_buscado.nome_produto = novo_nome
                    print("NOME DO PRODUTO EDITADO COM SUCESSO!")
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

                    # FECHANDO CONEXÃO COM O BANCO DE DADOS
                    Funcoes.disconnect(conn, cursor)

                elif (opcao == 2):
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

            elif (opcao == 3):
                # (ADMIN) EDITAR O VALOR DO PRODUTO - OK
                opcao = int(input(Funcoes.confirmarAcao("EDITAR VALOR")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao("EDITAR VALOR")))

                if (opcao == 1):
                    novo_valor = float(input("DIGITE O NOVO VALOR: "))
                    novo_valor = Funcoes.validarPreenchimento("DIGITE O NOVO VALOR: ", novo_valor)

                    # CRIANDO CONEXÃO COM O BANCO DE DADOS
                    conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                    cursor = conn.cursor()
                    Funcoes.connect(dsn)

                    # EDITANDO NO BANCO DE DADOS E NO CONSOLE
                    cursor.execute("UPDATE produto SET valor_produto = :novo_valor WHERE id_produto = :id_produto", {"novo_valor": novo_valor, "id_produto": produto_buscado.id_produto})
                    cursor.connection.commit()
                    produto_buscado.valor_produto = novo_valor
                    print("VALOR DO PRODUTO EDITADO COM SUCESSO!")
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

                    # FECHANDO CONEXÃO COM O BANCO DE DADOS
                    Funcoes.disconnect(conn, cursor)

                elif (opcao == 2):
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
                
            elif (opcao == 4):
                # (ADMIN) EDITAR A QUANTIDADE DO PRODUTO - OK
                opcao = int(input(Funcoes.confirmarAcao("EDITAR QUANTIDADE")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao("EDITAR QUANTIDADE")))

                if (opcao == 1):
                    nova_quantidade = int(input("DIGITE A NOVA QUANTIDADE: "))
                    nova_quantidade = Funcoes.validarPreenchimento("DIGITE A NOVA QUANTIDADE: ", nova_quantidade)

                    # CRIANDO CONEXÃO COM O BANCO DE DADOS
                    conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                    cursor = conn.cursor()
                    Funcoes.connect(dsn)

                    # EDITANDO NO BANCO DE DADOS E NO CONSOLE
                    cursor.execute("UPDATE produto SET qtd_produto = :nova_quantidade WHERE id_produto = :id_produto", {"nova_quantidade": nova_quantidade, "id_produto": produto_buscado.id_produto})
                    cursor.connection.commit()
                    produto_buscado.qtd_produto = nova_quantidade
                    print("QUANTIDADE DO PRODUTO EDITADA COM SUCESSO!")
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

                    # FECHANDO CONEXÃO COM O BANCO DE DADOS
                    Funcoes.disconnect(conn, cursor)
                
                elif (opcao == 2):
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

            elif (opcao == 5):
                # (ADMIN) EDITAR A URL DE IMAGEM DO PRODUTO - OK
                opcao = int(input(Funcoes.confirmarAcao("EDITAR URL DE IMAGEM")))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao("EDITAR URL DE IMAGEM")))
                
                if (opcao == 1):
                    nova_imagem_produto = input("DIGITE A NOVA URL DE IMAGEM: ")
                    nova_imagem_produto = Funcoes.validarPreenchimento("DIGITE A NOVA URL DE IMAGEM: ", nova_imagem_produto)

                    # CRIANDO CONEXÃO COM O BANCO DE DADOS
                    conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                    cursor = conn.cursor()
                    Funcoes.connect(dsn)

                    # EDITANDO NO BANCO DE DADOS E NO CONSOLE
                    cursor.execute("UPDATE produto SET imagem_produto = :nova_imagem_produto WHERE id_produto = :id_produto", {"nova_imagem_produto": nova_imagem_produto, "id_produto": produto_buscado.id_produto})
                    cursor.connection.commit()
                    produto_buscado.imagem_produto = nova_imagem_produto
                    print("URL DE IMAGEM DO PRODUTO EDITADA COM SUCESSO!")
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

                    # FECHANDO CONEXÃO COM O BANCO DE DADOS
                    Funcoes.disconnect(conn, cursor)

                elif (opcao == 2):
                    input("TECLE ENTER PARA VOLTAR AO MENU.")

            elif (opcao == 6):
                # (ADMIN) SAIR DO MENU EDITAR PRODUTO - OK
                perfilProduto = 0

    def perfilProduto(produto_buscado):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {produto_buscado.id_produto}\n"
        retornoPerfil += f"02. NOME: {produto_buscado.nome_produto}\n"
        retornoPerfil += f"03. VALOR: {produto_buscado.valor_produto}\n"
        retornoPerfil += f"04. QUANTIDADE: {produto_buscado.qtd_produto}\n"
        retornoPerfil += f"05. URL DE IMAGEM: {produto_buscado.imagem_produto}\n"
        retornoPerfil += "06. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil
