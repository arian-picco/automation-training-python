color1 = 'azul'
color2 = 'verde'
color3 = 'rojo'

colores = ['azul','verde','rojo']
print(colores)
print(colores[1])

cosas = [1,False,'amarillo',5.24,['hola','chau']]
print(cosas)

for i in range(0,len(colores)):
    print(colores[i])

#por cada iteracion me guarda colores en color
for color in colores:
    print('color: ' + color)

#agregar cosas a la lista
colores.append('rosa')
print(colores)

colores.insert(2,'celeste')
print(colores)

#sacar el último elemento
colores.pop()
print(colores)

#sacar una posicion
colores.pop(2)
print(colores)

#dar vuelta un elemento
colores.reverse()
print(colores)

#ordenar por orden alfabético
colores.sort()
print(colores)