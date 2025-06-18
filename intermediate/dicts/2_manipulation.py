dicionario = {}

# Criar chave e valor
dicionario["nome"] = "Gabriel"
dicionario["sobrenome"] = "Frigo"

# Deletar chave
del dicionario["nome"]

# Atualizar valor da chave
dicionario["sobrenome"] = "Sena"

# Acessar chave e valor
print(f"Dicionário Final: {dicionario}, {dicionario['sobrenome']}")