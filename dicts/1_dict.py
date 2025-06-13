# Estrutura "chave" e "valor"
# Chaves (imutáveis): str, int, float, bool, tuple e etcc
# Valores (mutáveis): str, int, dict, list e etc

dicionario = {
  "nome" : "Gabriel",
  "sobrenome" : "Frigo",
  "idade" : 20,
  "altura" : 1.74,
  "hobbies" : {
    "esporte" : ["futebol", "vôlei"],
    "jogos" : ["resident evil 4", "spider man 2", "god of war ragnarok"],
    "livros" : ["estrutura de dados e algoritmos", "fundamentos de engenharia de dados"],
  },
}

for chave in dicionario:
  print(f"{chave} : {dicionario[chave]}")