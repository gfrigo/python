# Método set() aceita apenas 1 argumento
set_1 = set(("Gabriel", 1, 2, 3, 4)) 
print(set_1, "\n")

# Método add() e update() -> Adicionar valores
set_1.add("Olá Mundo")
set_1.update(("Paula",)) # -> Ambos adicionam o objeto completo

set_1.add("Gabriel") # Valor único, não irá repetir
set_1.update("Giovanna") # Objeto passado como iterável (string separada por caractere)

print(set_1, "\n")

# Método discard() -> Descartar um determinado valor referenciando-o
set_1.discard("Gabriel")
print(set_1, "\n")

# Método clear() -> Limpar todos os valores
set_1.clear()
print(set_1, "\n")