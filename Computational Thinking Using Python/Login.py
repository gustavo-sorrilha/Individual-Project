class Login:
    def __init__(self, email=None, senha=None):
        self.email = email
        self.senha = senha
        
    def efetuarLogin(self):
        self.email = input("DIGITE SEU EMAIL: ")
        self.senha = input("DIGITE SUA SENHA: ")
    
    def validarLogin(self, listaBeneficiario):
        email_login = self.email
        senha_login = self.senha
        index_beneficiario = -1
        
        for beneficiario in listaBeneficiario:
            if beneficiario.getEmail_usuario() == email_login:
                index_beneficiario = listaBeneficiario.index(beneficiario)
                break
        
        if index_beneficiario == -1:
            return False
        else:
            beneficiario_consultado = listaBeneficiario[index_beneficiario]
            email_beneficiario = beneficiario_consultado.getEmail_usuario()
            senha_usuario = beneficiario_consultado.getsenha_usuario()
            
            if email_login == email_beneficiario and senha_login == senha_usuario:
                return True
            else:
                return False
                
    def mensagemLogin(self, listaBeneficiario):
        email_login = self.email
        index_beneficiario = -1
        
        for beneficiario_logado in listaBeneficiario:
            if beneficiario_logado.getEmail_usuario() == email_login:
                index_beneficiario = listaBeneficiario.index(beneficiario_logado)
                break
        
        return "BEM VINDO, " + listaBeneficiario[index_beneficiario].getNome_usuario()
        
    def beneficiarioLogado(self, listaBeneficiario):
        email_login = self.email
        index_beneficiario = -1
        
        for beneficiario_logado in listaBeneficiario:
            if beneficiario_logado.getEmail_usuario() == email_login:
                index_beneficiario = listaBeneficiario.index(beneficiario_logado)
                break
        
        return index_beneficiario
        
    def adminLogado(self, listaFuncionarios):
        if self.email == listaFuncionarios[0].getEmail_usuario() and self.senha == listaFuncionarios[0].getsenha_usuario():
            return True
        else:
            return False
