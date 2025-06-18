# Acompanhar o Debug e Call Stack

x = 10
y = 10

def somar():
  x = 20
  print(f'{x=}, {y=}')
  
  print("Chamando função secundária...")
  def somar2():
    global x
    print(f'{x=}, {y=}')

  somar2()

somar()