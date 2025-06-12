# Forma como referenciamos a função em memória
def saudacao(msg:str, nome:str):
  print(f"{msg}, {nome}!")

def executar_saudacao(funcao, *args):
  funcao(*args)

funcao_memoria = saudacao
print(funcao_memoria)

executar_saudacao(funcao_memoria, "Bom dia", "Gabriel")