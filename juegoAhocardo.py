import time
nombre = input("¿Como te llamas? ")
print("Hola, " + nombre, "es hora de jugar al ahorcado")
time.sleep(1)
print("Comienza a adivinar ")
time.sleep(0.5)
palabra_secreta = "escuela de frontera"
letra_nueva = " "
vidas = 5

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