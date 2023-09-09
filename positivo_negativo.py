positivos = 0
negativos = 0
print("Ingresa varios números enteros (ingresa 0 para finalizar):")
while True:
    numero = int(input())
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    if numero == 0:
        break
print("Cantidad de números positivos: ", end="")
for i in range(positivos):
    print("*", end="")
print()
print("Cantidad de números negativos: ", end="")
for i in range(negativos):
    print("*", end="")
