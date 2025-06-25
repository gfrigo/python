# Raise lança uma exceção personalizda e voluntária de acordo com a lógica de negócio/contexto
# Pode ser ou não utilizado em blocos try except/finally e else
# Muitas vezes, redundante se usado em blocos except

def checar_numero(n:int):
  if not isinstance(n, (int, float)):
    raise ValueError(f'O objeto "{n}" não é um número.')

try:
  checar_numero("Olá, mundo!")
except Exception as e: # Captura da exceção lançada por raise, se usados juntos, seria redundante
  print(e, e.__class__.__name__)