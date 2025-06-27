"""
- Módulos: arquivos.py
- Pacotes: pastas contendo os arquivos.py
- Obs: O arquivo executado sempre será o "__main__" e ele enxergará apenas os
  módulos e pacotes irmãos (memso nível de pasta) ou filhos/netos (níveis inferiores)
"""

"""
- Importação de mesmo nível
- Obs: import_8 não printará __main__ e sim o próprio nome do arquivo
"""
import import_8 

# Este presente arquivo se chamará __main__
print(f"Este arquivo tem o __name__ igual a {__name__}")