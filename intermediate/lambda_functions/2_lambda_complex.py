# As funções lambda não devem ser usadas para tarefas complexas

def executa(funcao, *args):
  return funcao(*args)

def cria_multiplicador(multiplicador):
  def multiplica(numero):
    return numero * multiplicador
  return multiplica

# Traduzindo para lambda functions
duplicador  = executa(
    lambda m: lambda n: n*m,
    2
  )
print(duplicador(3))