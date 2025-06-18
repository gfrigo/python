# Closure e funções que retornam outras funções
# Acompanhar o Debug e Call Stack

def executar_saudacao(msg):
  def saudacao(nome):
    return f"{msg}, {nome}!"
  return saudacao
  
# Função 'saudacao()' e parâmetro 'msg' salvos na memória
funcao_memoria = executar_saudacao("Bom dia") 
print(funcao_memoria)

# A execução da função 'saudacao()' foi adiada. Será executada abaixo somenta agora:
print(funcao_memoria("Gabriel")) 