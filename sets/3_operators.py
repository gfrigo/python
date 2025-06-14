# Operadores da classe set

set_1 = {1, 2, 3, 4, 5}
set_2 = {2, 3, 4, 5, 6}

# União de 2 conjuntos
# Operadores: | ou set.union(set_2)
set_3 = set_1 | set_2
print(set_3, "\n")

# Intersecção de 2 conjuntos (itens presentes em amobs)
# Operadores: & ou set.intersection(set_2)
set_3 = set_1 & set_2
print(set_3, "\n")

# Diferença entre 2 conjuntos (itens presentes apenas no set da esquerda)
# Operadores: - ou set.difference(set_2)
set_3 = set_1 - set_2
set_4 = set_2 - set_1
print(set_3, set_4, "\n")

# Diferença Simétrica entre 2 conjuntos (itens que não estão em ambos)
# Operadores: ^ ou set.symmetric_difference(set_2)
set_3 = set_1 ^ set_2
print(set_3, "\n")