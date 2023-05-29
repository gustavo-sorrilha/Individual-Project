class Login:
    def __init__(self, email=None, senha=None):
        self.email = email
        self.senha = senha
        
    def efetuarLogin(self):
        self.email = input("DIGITE SEU EMAIL: ")
        self.senha = input("DIGITE SUA SENHA: ")
    
    def validarLogin(self, listaAlunos):
        email_login = self.email
        senha_login = self.senha
        index_aluno = -1
        
        for aluno in listaAlunos:
            if aluno.getEmail_usuario() == email_login:
                index_aluno = listaAlunos.index(aluno)
                break
        
        if index_aluno == -1:
            return False
        else:
            aluno_consultado = listaAlunos[index_aluno]
            email_aluno = aluno_consultado.getEmail_usuario()
            senha_usuario = aluno_consultado.getsenha_usuario()
            
            if email_login == email_aluno and senha_login == senha_usuario:
                return True
            else:
                return False
                
    def mensagemLogin(self, listaAlunos):
        email_login = self.email
        index_aluno = -1
        
        for aluno_logado in listaAlunos:
            if aluno_logado.getEmail_usuario() == email_login:
                index_aluno = listaAlunos.index(aluno_logado)
                break
        
        return "BEM VINDO, " + listaAlunos[index_aluno].getNome_usuario()
        
    def alunoLogado(self, listaAlunos):
        email_login = self.email
        index_aluno = -1
        
        for aluno_logado in listaAlunos:
            if aluno_logado.getEmail_usuario() == email_login:
                index_aluno = listaAlunos.index(aluno_logado)
                break
        
        return index_aluno
        
    def adminLogado(self, listaFuncionarios):
        if self.email == listaFuncionarios[0].getEmail_usuario() and self.senha == listaFuncionarios[0].getsenha_usuario():
            return True
        else:
            return False
