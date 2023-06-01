SELECT * FROM aluno;
SELECT * FROM aluno_certificado;
SELECT * FROM aula;
SELECT * FROM certificado;
SELECT * FROM funcionario;
SELECT * FROM modulo;
SELECT * FROM modulo_aula;
SELECT * FROM modulo_questao;
SELECT * FROM movimentacao;
SELECT * FROM nivel;
SELECT * FROM produto;
SELECT * FROM professor;
SELECT * FROM questao;
SELECT * FROM resposta;
SELECT * FROM usuario;

----------------------------------------------------------------

-- SELECTS PARA VALIDA��O DE ALTERA��ES NO PYTHON:
-- 01. ALUNO
SELECT usuario.id_usuario, usuario.cpf_usuario, usuario.nome_usuario, usuario.email_usuario, aluno.dt_nasc_aluno, aluno.dt_reg_aluno, aluno.senha_aluno, aluno.moedas_aluno, aluno.nivel_aluno FROM usuario INNER JOIN aluno ON usuario.id_usuario = aluno.id_usuario;

-- 02. PROFESSOR
SELECT usuario.id_usuario, usuario.cpf_usuario, usuario.nome_usuario, usuario.email_usuario FROM usuario INNER JOIN professor ON usuario.id_usuario = professor.id_usuario;

-- 03. FUNCION�RIO
SELECT usuario.id_usuario, usuario.cpf_usuario, usuario.nome_usuario, usuario.email_usuario, funcionario.senha_funcionario, funcionario.cargo_funcionario FROM usuario INNER JOIN funcionario ON usuario.id_usuario = funcionario.id_usuario;

-- 04. MÓDULO
SELECT * FROM modulo ORDER BY id_modulo;

-- 05. AULAS
SELECT * FROM aula ORDER BY id_aula;

-- 05.01. AULAS DO MÓDULO
SELECT * FROM modulo_aula WHERE id_modulo = ?;

-- 06. QUESTÕES
SELECT * FROM questao ORDER BY id_questao;

-- 0601. QUESTÕES DO MÓDULO
SELECT * FROM modulo_questao WHERE id_modulo = ?;