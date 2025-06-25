# Else será executado sempre que o try executar cocm sucesso
# Obs: Não é possível usar apenas try com else, é necessário o uso de except ou finally

try:
  print("Olá, mundo!")
except Exception as e:
  print("Ocorreu um erro.")
else:
  print("Else foi acionado!\n")

try:
  a = "Olá, mundo!"
  b = False
  c = a+b
except Exception as e:
  print(f"Ocorreu um erro: {e}")
  print(f"Tipo da exceção: {e.__class__.__name__}")
else:
  print("Else não será acionado!")