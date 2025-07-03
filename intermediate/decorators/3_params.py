"""
As funções decoradoras também possuem parâmetros
"""

def fabrica_decoradores(a=None, b=None, c=None): # Parâmetros do decorador
  def fabrica_funcoes(func): # Função decoradora == Criadora de funções
    print("Decoradora 1")
    def aninhada(*args, **kwargs): # Função a ser utilizada, ou seja, soma()
      print("Função aninhada:")  
      print(f"Parâmetros do decorador: {a}, {b} e {c}") # Tem conhecimento de 3 escopos
      resultado = func(*args, **kwargs)
      return resultado
    return aninhada
  return fabrica_funcoes

@fabrica_decoradores(1, 2, 3)
def soma(x, y):
  return x + y

decoradora = fabrica_decoradores(4, 5, 6)
resultado = decoradora(soma)
print(resultado(5, 5))