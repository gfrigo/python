produto = {
  "nome": "lápis",
  "preco": 1.25,
  "categoria": "papelaria"
}

# Uso de Mapping e Filter
dicionario = {
  chave: valor.upper()
  if isinstance(valor, str) else valor # Mapping
  for chave, valor in produto.items()
  if chave != "categoria" # Filter
}

print(dicionario)