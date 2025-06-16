# Funções lambdas podem receber infinitos argumentos com *args

def executa(funcao, *args):
  return funcao(*args)

print(
  executa(
    lambda *args: sum(args),
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10
  )
)