# Funções personalizadas que pausam
# Uso de yield

def generator():
  print("A função será pausada...")
  yield 1
  print("Continuando para o próximo...")
  yield 2
  print("Mais uma vez...")
  yield 3
  return "ACABOU" # Se o método next() alcançar a exceção, acionará o return

gen = generator()
print(gen) # A variável "gen" não armazena "ACABOU" e sim o objeto generator
print(f"Primeira execução: {next(gen)}")
print(f"Segunda execução: {next(gen)}")
print(f"Terceira execução: {next(gen)}\n\n")
# print(f'Exceção retornada ("ACABOU"): {next(gen)}\n\n')

# Uso do yield from
# Generator functions como dependência sequencial

def gen1():
  yield 1
  yield 2
  yield 3

def gen2():
  yield from gen1()
  yield 4
  yield 5
  yield 6
  return "ACABOU"

gen = gen2()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(f'Exceção retornada ("ACABOU"): {next(gen)}\n\n')