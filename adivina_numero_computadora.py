import random


def adivina_el_numero_computadora(x):

    print("==========================")
    print("Bienvenido(a) al juego!")
    print("==========================")
    print(f"Selecciona un número entre 1 y {x} para que la computadora intente adivinarlo...")

#Defino límites como variables:
    limite_inferior = 1 #Este es mi límite inferior
    limite_superior = x #Este es mi límite superior que va ser 10

    respuesta = ""
    while respuesta != "c":
        #Generar predicción
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        
        else:
            prediccion = limite_inferior

        #Obtener respuesta del usuario
        respuesta = input(f"Mi predición es {prediccion}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcto, ingresa (C).").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1

        elif respuesta == "b":
            limite_inferior = prediccion + 1

    print(f"La comptutadora adivinó tu número correctamente:{prediccion} ")            

adivina_el_numero_computadora(10)

