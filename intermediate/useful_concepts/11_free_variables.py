"""
local(): Retorna variáveis locais de uma função
globals: Referencia uma variável como global no módulo
nonlocals: Referencia uma variável não local e nem global para o módulo e 
permite que eu modifique o valor, diferente de globals que resulta em erro
"""

def concatenador_inicial(str_inicial:str):
  valor_final = str_inicial

  def concatenador_final(str_final:str):
    # O valor de "a" é guardado na memória para ser utilizado nesta execução
    nonlocal valor_final # Não é local da função concatenador_final()
    valor_final += str_final
    return valor_final
  return concatenador_final

concatenador = concatenador_inicial("a")
print(concatenador("b"))