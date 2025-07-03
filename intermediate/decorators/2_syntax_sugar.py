"""
Decoradores são os "syntax sugar", ou seja, formas de facilitar o
processo de funções decoradoras (arquivo 1_decorator_function.py)
"""

def criar_funcao(funcao):
  def criador_funcao_interna(*args):
    print("Decorando...")
    for arg in args:
      verificador_string(arg)
    resultado = funcao(*args)
    print("Decorada!") 
    return resultado
  return criador_funcao_interna

def verificador_string(string:str):
  if not isinstance(string, str):
    raise ValueError(f'"{string}" deve ser do tipo "str"')

@criar_funcao
def inverter_string(string:str):
  return string[::-1]

string_invertida = inverter_string("123")
print(string_invertida)