

nombre = input('Nombre: ')
adivinar = 'pepe'
oportunidades = 6
while nombre != adivinar:
    oportunidades = oportunidades -1
    print('Oportunidades: ' + str(oportunidades))
    adiviniar = input('Adivine el nombre: ')
    if oportunidades == 0:
        print('Perdiste')
        break
else:
    print('Ganaste')
