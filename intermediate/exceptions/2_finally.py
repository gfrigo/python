# Finally acionará independente de uma exceção ser levantada

# Uso de try com exceção sendo levantada
try:
  lista = [1, 2, 3, 4]
  print(lista[10]) # IndexError
except Exception as e:
  print(f"Mensagem: {e}")
  print(f"Tipo da Exceção: {e.__class__.__name__}")
finally:
  print("O código foi encerrado.\n")

# Uso de try apenas com finally
try:
  print("Try correto acionado!")
finally:
  print("Finally acionado!")