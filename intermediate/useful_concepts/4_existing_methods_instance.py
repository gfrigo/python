# hasattr e getattr
string = "Gabriel"
metodo = "upper"

# Verificar existência de atributos e métodos a serem executados em uma instância
if hasattr(string, metodo):
  print(f"{string} possui o atribuito {metodo}")
  print(getattr(string, metodo)())

"""
 Obs: Para testar o "dir", abra um break point em linhas que definem variáveis, 
 abra o "Debug Console" do Visual Studio Code e digite (durante debug):
 "dir(variável)" e verá todos os atributos daquela variável definida.
"""