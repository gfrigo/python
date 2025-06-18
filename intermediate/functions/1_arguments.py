def somar(x:int=None, y:int=None) -> int:
  print(f"Soma:\n{x=}\n{y=}\n{x} + {y} = {x+y}\n")
  return x+y

# Argumentos posicionais
result = somar(5, 5)
print(result)

# Argumentos nomeados
result = somar(x=5, y=5)
print(result)