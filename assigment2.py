clientes = int(input('ingrese el numero de clientes '))

for i in range(clientes):
    print(i)
    edad = 0
    while edad <=1 and edad <=120:
        edad = int(input('Digame su edad '))
    if edad<18: 
        condicionEdad = 'menor'
        print(condicionEdad)
    elif edad>18:
        conficionEdad = 'mayor' 
        print(condicionEdad)
    elif edad>65: 
        conficionEdad = 'jubilado' 
        print(condicionEdad)
    else:
        conficionEdad = 'cadaver'
        print(condicionEdad)
