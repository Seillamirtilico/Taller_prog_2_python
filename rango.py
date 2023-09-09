cantidadDatos = int(input("Introduce la cantidad de datos que deseas analizar: "))
if cantidadDatos <= 0:
    print("La cantidad de datos debe ser un número positivo.")
    exit()
datos = []
valorMaximo = float('-inf')
valorMinimo = float('inf')
for i in range(cantidadDatos):
    valor = float(input("Ingresa el valor número " + str(i + 1) + ": "))
    datos.append(valor)
    if valor > valorMaximo:
        valorMaximo = valor
    if valor < valorMinimo:
        valorMinimo = valor
rango = valorMaximo - valorMinimo
print("El rango de los datos es: " + str(rango))
