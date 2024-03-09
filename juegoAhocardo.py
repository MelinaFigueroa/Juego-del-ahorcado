import time

# Definir la palabra secreta
palabra_secreta = "ahorcado"

# Solicitar el nombre del jugador
nombre = input("Bienvenido al juego del ahorcado!!! \n" +
               "¿Cómo te llamas?\n")

# Mensaje de bienvenida
print("Hola, " + nombre, "es hora de jugar al ahorcado")

# Inicialización de variables
time.sleep(1)
letra_nueva = " "
vidas = 5
contador = 0

# Contar la cantidad de letras en la palabra secreta
for i in palabra_secreta:
    contador += 1

# Mostrar la cantidad de letras de la palabra secreta
print("*-*-* Palabra de ", +contador, " Letras *-*-*\n" +
      "*-*-* Comienza a adivinar *-*-*",)
time.sleep(0.5)

# Iniciar el bucle del juego
while vidas > 0:
    fallas = 0
    for letra in palabra_secreta:
        if letra in letra_nueva:
            print(letra, end=" ")
        else:
            print("_", end="")
            fallas += 1
    if fallas == 0:
        print("\nFELICIDADES HAS GANADO, la palabra secreta es: \n", palabra_secreta)
        break

    # Solicitar una letra al jugador
    tu_letra = input("\nIntroduce una letra\n")
    letra_nueva += tu_letra

    # Verificar si la letra ingresada está en la palabra secreta
    if tu_letra not in palabra_secreta:
        vidas -= 1
        print("Intento fallido ")
        print("Te quedan ", +vidas, " vidas")

    # Verificar si el jugador ha perdido todas sus vidas
    if vidas == 0:
        print("Lo siento, has perdido!")
else:
    print("Gracias por participar")
