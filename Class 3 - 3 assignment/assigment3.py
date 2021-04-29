
def calculateAgeRange(age):
    if age < 18:
        ageRange = "menor"
    elif age >= 18 or age<=65:
        ageRange = "mayor"
    elif age >65 or age < 120:
        ageRange = "jubilado"
    return ageRange

def sellForRange(name,lastName,ageRange):
    if ageRange == "menor":
        sellToys(name,lastName,ageRange)
    # elif ageRange == "mayor":
    #     sellClothes(name,lastName,ageRange)
    # elif ageRange == "jubilado":
    #     sellTrip(mame,lastName,ageRange)
    
def isElectric():
    condition = int(input("desea un juguete electronico? - conteste 1 por si por 2 no "))
    if condition == 1:
        isElectric = "Compra de juguete electrónico "
    else:
        isElectric = "Compra de juguete artesanal "
    return isElectric

def doesItWalk():
    condition = int(input("desea un juguete que camina? - conteste 1 por si o 2 por no "))
    if condition == 1:
        doesItWalk = ",es un juguete que camina"
    else:
        doesItWalk = ",es un juguete que no camina"
    return doesItWalk


def selectColor():
    color = input("seleccione el color del juguete ")
    return color

def sellToys(name,lastName,ageRange):
    electric = isElectric()
    walkingToy = doesItWalk()
    color = selectColor()
    print('Bienvenido', name, lastName, 'Usted seleccionó un juguete ', electric, walkingToy, 'de color',color)

        
    


    
people = int(input('Ingrese la cantidad de personas '))
for i in range (people):
    name = input('Ingrese su nombre ')
    lastName = input('Ingrese su apellido ')
    age = int(input('Ingrese cuantos años tiene '))
    ageRange = calculateAgeRange(age)
    sellForRange(name,lastName,ageRange)





