import random

numeroSecreto = random.randint(0, 100)
intentosRestantes = 5
print("Bienvenido al juego de adivinar el número secreto.")
print("Tienes", intentosRestantes, "intentos.")
numeroIngresado = 0
while intentosRestantes > 0:
    numeroIngresado = int(input("Ingresa un número: "))
    if numeroIngresado == numeroSecreto:
        print("¡Felicidades, has acertado!")
        break
    elif numeroIngresado < numeroSecreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
    intentosRestantes -= 1
    if intentosRestantes > 0:
        print("Tienes", intentosRestantes, "intentos restantes.")
    else:
        print("Has agotado tus intentos. El número secreto era", numeroSecreto, ".")
