import copy

# Tipos de cópai de tipos mutáveis (listas e dicionários)

dicionario = {
  "chave_1" : 1,
  "chave_2" : 2,
  "lista_1" : [1, 2]
}

# 1- "dicionario_2" aponta para o mesmo lugar na memória que dicionario
dicionario_2 = dicionario
print(dicionario_2)
print(dicionario)
print("\n")

dicionario_2["chave_1"] = 1000
print(dicionario_2)
print(dicionario)
print("\n")

# 2- Método copy() -> Shallow Copy (Cópia Rasa)
# Tipos mutáveis (listas e dicts) dentro do dicionario permanecem como mesma referência na memória
dicionario_copy = dicionario.copy()
dicionario_copy["lista_1"][0] = 1000
print(dicionario_copy)
print(dicionario)
print("\n")

# 3- Método copy.deepcopy() -> Deep Copy (Cópia Profunda)
# Agora sim, dois objetos diferentes na memória
dicionario_deep_copy = copy.deepcopy(dicionario)
dicionario_deep_copy["lista_1"][1] = 2000
dicionario_deep_copy["chave_1"] = 3000

print(dicionario_deep_copy)
print(dicionario)
print("\n")