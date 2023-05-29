import datetime
from typing import List
from Usuario import Usuario
from Produto import Produto

class Movimentacao:
    def __init__(self, id_movimentacao = None, data_movimentacao = None, usuario_movimentacao = None, produto_movimentacao = None, qtd_movimentacao = None):
        self._id_movimentacao = id_movimentacao
        self._data_movimentacao = data_movimentacao
        self._usuario_movimentacao = usuario_movimentacao
        self._produto_movimentacao = produto_movimentacao
        self._qtd_movimentacao = qtd_movimentacao

    @property
    def id_movimentacao(self):
        return self._id_movimentacao
    
    @id_movimentacao.setter
    def id_movimentacao(self, id_movimentacao):
        self._id_movimentacao = id_movimentacao
    
    @property
    def data_movimentacao(self):
        return self._data_movimentacao
    
    @data_movimentacao.setter
    def data_movimentacao(self, data_movimentacao):
        self._data_movimentacao = data_movimentacao

    @property
    def usuario_movimentacao(self):
        return self._usuario_movimentacao
    
    @data_movimentacao.setter
    def usuario_movimentacao(self, usuario_movimentacao):
        self._usuario_movimentacao = usuario_movimentacao

    @property
    def produto_movimentacao(self):
        return self._produto_movimentacao
    
    @produto_movimentacao.setter
    def produto_movimentacao(self, produto_movimentacao):
        self._produto_movimentacao = produto_movimentacao

    @property
    def qtd_movimentacao(self):
        return self._qtd_movimentacao
    
    @qtd_movimentacao.setter
    def qtd_movimentacao(self, qtd_movimentacao):
        self._qtd_movimentacao = qtd_movimentacao

    @staticmethod
    def from_dict(movimentacao_dict: dict) -> 'Movimentacao':
        return Movimentacao(
            movimentacao_dict['id_movimentacao'],
            movimentacao_dict['data_movimentacao'],
            movimentacao_dict['usuario_movimentacao'],
            movimentacao_dict['produto_movimentacao'],
            movimentacao_dict['qtd_movimentacao']
        )

    @staticmethod
    def to_dict(movimentacao: 'Movimentacao') -> dict:
        return {
            'id_movimentacao': movimentacao.id_movimentacao,
            'data_movimentacao': movimentacao.data_movimentacao,
            'usuario_movimentacao': movimentacao.usuario_movimentacao,
            'produto_movimentacao': movimentacao.produto_movimentacao,
            'qtd_movimentacao': movimentacao.qtd_movimentacao
        }

    @staticmethod
    def from_list(movimentacao_list: List[dict]) -> List['Movimentacao']:
        return [Movimentacao.from_dict(mov_dict) for mov_dict in movimentacao_list]

    @staticmethod
    def to_list(movimentacao: List['Movimentacao']) -> List[dict]:
        return [Movimentacao.to_dict(mov) for mov in movimentacao]
