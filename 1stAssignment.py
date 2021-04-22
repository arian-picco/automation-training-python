print('Ingrese nombre, apellido y edad: ')
nombre = input()
apellido = input()
edad = int(input())


if edad<18: 
    condicionEdad = 'menor'
elif edad>18 and edad<65:
    conficionEdad = 'mayor' 
elif edad>65 and edad<120:
    conficionEdad = 'jubilado' 
else:
     conficionEdad = 'cadaver'


print('Su nombre es: ' + nombre + ' ' +  apellido + 'y usted es ' + conficionEdad)
print('Su nombre es: {} {} y usted es {}'.format(nombre, apellido, conficionEdad))
    
