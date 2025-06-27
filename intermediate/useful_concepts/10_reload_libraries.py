"""
- Singleton: Uma biblioteca é carregada apenas uma vez, por padrão no python,
 evitando processamento desnecessário.
- é possível recarregar uma biblioteca em algum momento do código.
"""

import importlib
import pandas

for i in range(10):
  print(f"Recarregando o módulo pela {i}x")
  importlib.reload(pandas)
