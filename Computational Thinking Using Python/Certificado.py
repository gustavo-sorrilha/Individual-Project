from typing import List
from datetime import date
from Funcoes import Funcoes

class Certificado:
    def __init__(self, id_certificado = None, data_certificado = None):
        self._id_certificado = id_certificado
        self._data_certificado = data_certificado
    
    @property
    def id_certificado(self):
        return self._id_certificado

    @id_certificado.setter
    def id_certificado(self, id_certificado):
        self._id_certificado = id_certificado
    
    @property
    def data_certificado(self):
        return self._data_certificado
    
    @data_certificado.setter
    def data_certificado(self, data_certificado):
        self._data_certificado = data_certificado