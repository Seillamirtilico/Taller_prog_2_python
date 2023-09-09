horas = 0
minutos = 0
duracionTramo = 0
sumaDuracion = 0
numeroTramos = 1
print("Ingresa la duración de cada tramo en minutos. Ingresa 0 para finalizar.")
while True:
    duracionTramo = int(input("Ingresa la duración en minutos del tramo número " + str(numeroTramos)))
    sumaDuracion += duracionTramo
    if duracionTramo == 0:
        horas = sumaDuracion // 60
        minutos = sumaDuracion % 60
        horaFormato = "0" + str(horas) if horas < 10 else str(horas)
        minutosFormato = "0" + str(minutos) if minutos < 10 else str(minutos)
        print("La duración total del recorrido es de " + horaFormato + ":" + minutosFormato)
        break
    numeroTramos += 1
