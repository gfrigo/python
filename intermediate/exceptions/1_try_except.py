# Tratamento de exceções com try e except
# Lê-se: Faça algo, se ocorrer um erro, capture-o e informe ao usuário/ação específica

try:
  a = 100
  b = 0
  c = a/b # Erro/Exceção retornada "ZeroDivisionError"
  print(c)
except ZeroDivisionError:
  print("ZeroDivisionError")
except (IndexError, NameError): # Captura de 2 erros possíveis
  print("IndexError ou NameError")
except Exception as e: # Qualquer exceção possível (classe principal)
  print(f"Mensagem {e}")
  print(f"Nome da Exceção:{e.__class__.__name__}")
