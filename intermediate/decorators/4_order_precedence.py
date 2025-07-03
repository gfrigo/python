def parametros_decorador(nome:str):
  def decorador(func):
    print('Decorador:', nome)

    def sua_nova_funcao(*args, **kwargs):
      resultado = func(*args, **kwargs)
      resultado_final = f'{resultado} {nome}'
      return resultado_final
    return sua_nova_funcao
  return decorador

@parametros_decorador(nome='Terceiro')
@parametros_decorador(nome='Segundo')
@parametros_decorador(nome='Primeiro')
def soma(x, y):
    return x + y

resultado_final = soma(10, 5)
print(resultado_final)