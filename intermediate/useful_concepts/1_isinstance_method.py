lista = [
  "a", 1, 1.1, [0, 1], (0, 1),
  {0, 1}, {"nome": "Gabriel"}
]

for item in lista:
  if isinstance(item, (int, float)):
    print(f"Item: {item}, Tipo:{type(item)}, É instância? {isinstance(item, (int, float))}")