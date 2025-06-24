import sys

# Funções que sabem pausar
# Todo generator é um iterator

lista = [n for n in range(100)]
generator = (n for n in range(100))
# print(lista)  List comprehension salva os valores na memória direto
print(generator) # Generator não salva valores na memória e sim, te entrega um valor por vez
print()
print(sys.getsizeof(lista)) # Mais pesado na memória
print(sys.getsizeof(generator)) # Mais leve na memória

# Os valores do generator não foram entregues à memória, está esperando você pedir pelos valores
# Você pode acessá-los (um por vez) com o next()
print()
for i in range(10):
  print(next(generator))