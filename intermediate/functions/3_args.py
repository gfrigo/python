# Desempacotamento (unpack)
x, y, *rest = [1, 2, 3, 4, 5, 6]
print(f"{x=}, {y=}, {rest=} {type(rest)}\n")

# *args
def soma(x, y, *args):
  print(f"{x=} + {y=} + {args=} {type(args)}")

  soma_args = sum(args)
  print(soma_args)

# Desempacotando tupla para função
numeros = 10, 20, 1, 2, 3, 4, 5, 6
soma(*numeros)