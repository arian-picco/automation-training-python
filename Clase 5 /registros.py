jugador = {
    'nombre':'Ruben',
    'apellido':'Paz',
    'club' : ['Racing', 'Peñarol']
}

jugador['goles'] = 200

#se pueden concatenar las listas

otros_clubes = {
    'clubes':['Boca', 'River']
}

jugador.update(otros_clubes)

print(jugador)