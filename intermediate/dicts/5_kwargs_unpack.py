# Desempacotar dicionário e keywords arguments
pessoa = {
  "nome": "Gabriel",
  "sobrenome": "Frigo"
}

pessoa_dados = {
  "idade": 20,
  "altura": 1.74
}

dicionario_completo = {**pessoa, **pessoa_dados} 
print(dicionario_completo, "\n")

def mostrar_argumentos_nomeados(*args, **kwargs):
  print(f"Argumento não nomeados: {args} {type(args)}\n")
  print(f"Argumentos nomeados: {kwargs} {type(kwargs)}")

#mostrar_argumentos_nomeados(1,2,3,4,5, nome="Gabriel", sobrenome="Frigo")
mostrar_argumentos_nomeados(1,2,3,4,5, **dicionario_completo)