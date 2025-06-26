# Módulos: arquivos.py
# Pacotes: pastas contendo os arquivos.py

# Formas de importar módulos, pacotes e bibliotecas no python
# Obs: Procurar deixar explícito funcionalidades e módulos no código, evitando confusão

"""
- as == alias (apelido)
- Obs: Usar quando for uma convenção da comunidade
- Obs: Não faz tanto sentido usar para funcionalidades criadas por você (causa confusão)
"""
import pandas as pd 

"""
- import lib == Importar biblioteca completa
- from lib import function == importar funcionalidade específica da biblioteca/módulo
- Obs: "read_csv" é como uma variável no código, não pode ser utilizado outro nome,
  pois, irá sobrescrever o "read_csv" do pandas
"""
from pandas import read_csv


"""
- from lib import *
- Obs: Importa tudo da biblioteca/módulo (não é uma boa prática)
"""
from pandas import *

def funcao_teste():
  print("Olá, mundo")
  print(__name__)