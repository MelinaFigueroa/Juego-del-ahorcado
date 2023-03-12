import time
palabra_secreta = "ahorcado"
nombre = input("Bienvenido al juego del ahorcado!!! \n" +
               "¿Como es tu nombre?\n")
print("Hola, " + nombre, "es hora de jugar al ahorcado")
time.sleep(1)
letra_nueva = " "
vidas = 5
contador = 0
for i in palabra_secreta:
    contador += 1
print("*-*-* Palabra de ", +contador, " Letras *-*-*\n" +
      "*-*-* Comienza a adivinar *-*-*",)
time.sleep(0.5)
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

    tu_letra = input("\nIntroduce una letra\n")
    letra_nueva += tu_letra

    if tu_letra not in palabra_secreta:
        vidas -= 1
        print("Intento fallido ")
        print("Te quedan ", +vidas, " vidas")
    if vidas == 0:
        print("Lo siento, has perdido!")
else:
    print("Gracias por participar")
