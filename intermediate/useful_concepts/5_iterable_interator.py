# Iterável: Item com objetos acessíveis e sequenciais
# Iterator: Tem conhecimento apenas de um valor por vez e sempre o próximo
# Obs: É assim que o for navega pelos objetos iteráveis
# Obs: Similaridade com o Iterator design pattern

iterable = ["Eu", "tenho", "__inter__"] # "__method__ == 'dunder'"
iterator = iter(iterable) # __iter__ e __next__
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator)) # Exceção: Acabou os itens do objeto iterável

# Obs: é assim que o for sabe quando parar o iterator