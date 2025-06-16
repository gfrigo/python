# Funções anônimas (sem nome)
# Apenas 1 linha de código

# list.sort() -> ordenação profunda de uma lista original
# sorted(list) -> faz uma cópia rasa de uma lista e ordena

lista = [
  {"nome": "Gabriel", "sobrenome": "Frigo"},
  {"nome": "Ana", "sobrenome": "Paula"},
  {"nome": "José", "sobrenome": "Roberto"},
  {"nome": "Giovanna", "sobrenome": "Santos"},
]

lista.sort(key=lambda lista: lista["nome"])
print(lista)

print()

# Necessário copy.deepcopy(lista_2)
lista_2 = sorted(lista, key=lambda lista: lista["sobrenome"])
print(lista_2)