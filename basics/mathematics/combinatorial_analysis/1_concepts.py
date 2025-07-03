"""
Combinação: seleção de elementos sem se importar com a ordem.
Permutação: ordenação de elementos.
Produto: multiplicação de possibilidades em etapas sucessivas.
"""

from itertools import combinations, permutations, product

pessoas = ["João", "Joana", "Luiz", "Letícia"]

camisetas = [["preta", "branca"], ["p", "m"]]

print("=========Combinação=========")
print(*list(combinations(pessoas, 2)), sep="\n")

print("\n=========Permutação=========")
print(*list(permutations(pessoas, 2)), sep="\n")

print("\n=========Produto=========")
print(*list(product(*camisetas)), sep="\n")