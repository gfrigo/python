# Métodos de objetos do tipo dicionário

dicionario = {
  "nome" : "Gabriel",
  "sobrenome" : "Frigo",
  "sobrenome" : "Sena" # Sobrescreve o valor anterior
}

# Obter tamanho do dicionário
print(len(dicionario), "\n")

# Obter as chaves do dicionário
print(dicionario.keys())
print(list(dicionario.keys()), "\n")

# Obter os valores do dicionário
print(dicionario.values())
print(list(dicionario.values()), "\n")

# Obter as chaves e os valores do dicionário
print(dicionario.items())
print(list(dicionario.items()), "\n")

# Inserir valor padrão para uma chave
dicionario.setdefault("idade", None)
print(dicionario, "\n")

# Obter valor específico
print(dicionario.get("nome", None))
print(dicionario.get("altura", None), "\n")

# Inserção de valores e chaves de um dicionário
dicionario.update({
  "jogos" : ["residente evil 4", "spider man"]
})

dicionario.update(trabalho="data engineer")

tupla = (("altura", 1.8),)
dicionario.update(tupla)

lista = [["idade", 40],]
dicionario.update(lista)

dicionario["hobbies"] = ["academia", "video-game"]

print(dicionario, "\n")

# Deletar item específico
idade = dicionario.pop("idade")
print(f"Valor excluído: {idade}")

del dicionario["trabalho"]

print(dicionario, "\n")

# Deletar último item
ultima_chave = dicionario.popitem()
print(f"Última chave excluída: {ultima_chave}")
print(dicionario)