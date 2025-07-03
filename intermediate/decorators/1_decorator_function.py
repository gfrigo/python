"""
Def: Funções que decoram outras funções, ou seja,
adicionam / removem / restrigem / alteram
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

def inverter_string(string:str):
  return string[::-1]

criador_funcao_interna = criar_funcao(inverter_string)
print(criador_funcao_interna("123"))