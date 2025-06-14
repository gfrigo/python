"""
Def: Simboliza o "Conjunto" matemático, representado pelo diagrama de Venn:
  1- Não aceita tipos mutáveis (listas e dicionários)
  2- Valores únicos
  3- Sem index
  4- Não garante ordem
"""

# Inicializar um set com string
set_str = set("Gabriel")
print(set_str, type(set_str))

# Inicializar um set com int
lista_int = [1, 2, 3, 4, 4, 4, 5, 5, 6, 7, 8, 9, 10, 10]
set_int = set(lista_int)
print(set_int)