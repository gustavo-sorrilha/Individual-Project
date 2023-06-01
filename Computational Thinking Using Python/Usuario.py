class Usuario:
    def __init__(self, id_usuario=None, cpf_usuario=None, cnpj_usuario=None, nome_usuario=None, email_usuario=None):
        self._id_usuario = id_usuario
        self._cpf_usuario = cpf_usuario
        self._cnpj_usuario = cnpj_usuario
        self._nome_usuario = nome_usuario
        self._email_usuario = email_usuario

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    @property
    def cpf_usuario(self):
        return self._cpf_usuario

    @cpf_usuario.setter
    def cpf_usuario(self, cpf_usuario):
        self._cpf_usuario = cpf_usuario
    
    @property
    def cnpj_usuario(self):
        return self._cnpj_usuario

    @cpf_usuario.setter
    def cnpj_usuario(self, cnpj_usuario):
        self._cnpj_usuario = cnpj_usuario

    @property
    def nome_usuario(self):
        return self._nome_usuario

    @nome_usuario.setter
    def nome_usuario(self, nome_usuario):
        self._nome_usuario = nome_usuario

    @property
    def email_usuario(self):
        return self._email_usuario

    @email_usuario.setter
    def email_usuario(self, email_usuario):
        self._email_usuario = email_usuario
