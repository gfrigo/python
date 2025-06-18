produtos = [
  {"nome": "p1", "preco":10},
  {"nome": "p2", "preco":20},
  {"nome": "p3", "preco":30}
]

# Acrescentar valores em uma lista com laço de repetição de uma linha
produtos_lista = [produto for produto in produtos]
print(produtos_lista, "\n")

# Mapeamento de dados -> Analisar e alterar valores adicionados
# Não há remoção ou adição de novos elementos, o tamanho permanece o mesmo
# Obs: O mapeamento sempre virá na esquerda do for e tem else*
novos_produtos = [
  {**produto, "preco": produto["preco"]*1.05}
  if produto["preco"] > 10 else produto
  for produto in produtos
]
print(novos_produtos, "\n")

# Filtro -> Mediante condição, adicionar ou remove da lista
# Obs: O filtro sempre virá na direita do for e não tem else*
# Obs: Pode ser combinado com Mapeamento
produtos_caros = [
  produto for produto in produtos if produto["preco"] > 10
]
print(produtos_caros, "\n")

# List Comprehension -> laços de repetição aninhados
# Obs: também no lado direito do for*
lista = [
  (x, y)
  for x in range(3)
  for y in range(3)
]
print(lista)