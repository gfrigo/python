# Valores considerados Falsy não ativam um if
# Qualquer coisa diferente dos items abaixo será considerado Truthy

lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ""
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

def verificar(valor):
  return "truthy" if valor else "falsy"

print(lista, verificar(lista))
print(dicionario, verificar(dicionario))
print(conjunto, verificar(conjunto))
print(tupla, verificar(tupla))
print(string, verificar(string))
print(inteiro, verificar(inteiro))
print(flutuante, verificar(flutuante))
print(nada, verificar(nada))
print(falso, verificar(falso))
print(intervalo, verificar(intervalo))