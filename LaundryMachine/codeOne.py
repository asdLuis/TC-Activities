tiempo = 0

def obtenerKg(kg):
    litrosAgua = kg * 3
    tiempoTotalLitros = litrosAgua / 10
    return tiempoTotalLitros

def lavadoraFuncional(kg, lavar, enjuagar, exprimir):
    tiempoDeLavado = obtenerKg(kg)
    if tiempoDeLavado > 4.5:
        return 'La cantidad de ropa excede el límite de carga'
    else:
        if lavar == True and enjuagar == True and exprimir == True:             #Todos True
            tiempo = 25 + 10 + 10 + (tiempoDeLavado * 2)
            return "El tiempo de lavado es de ", tiempo ,"minutos"
        elif lavar == True and enjuagar == True and exprimir == False:          #Lavar y enjuagar True
            tiempo = 25 + 10 + tiempoDeLavado 
            return "El tiempo de lavado es de ", tiempo ,"minutos"
        elif lavar == True and enjuagar == False and exprimir == True:          #Lavar y exprimir True
            tiempo = 25 + 10 + tiempoDeLavado
            return "El tiempo de lavado es de ", tiempo ,"minutos"
        elif lavar == True and enjuagar == False and exprimir == False:         #Solo lavar True
            tiempo = 25 + tiempoDeLavado
            return "El tiempo de lavado es de ", tiempo ,"minutos"
        elif lavar == False and enjuagar == True and exprimir == True:          #Enjuagar y exprimir True
            tiempo = 10 + 10 + tiempoDeLavado
            return "El tiempo de lavado es de ", tiempo ,"minutos"
        elif lavar == False and enjuagar == True and exprimir == False:         #Solo enjuagar True  
            tiempo = 10 + tiempoDeLavado
            return "El tiempo de lavado es de ", tiempo ,"minutos"
        elif lavar == False and enjuagar == False and exprimir == True:         #Solo exprimir True
            tiempo = 10 
            return "El tiempo de lavado es de ", tiempo ,"minutos"
        elif lavar == False and enjuagar == False and exprimir == False:        #Todos False
            tiempo = 0
            return "El tiempo de lavado es de ", tiempo ,"minutos"

ejemplo = lavadoraFuncional(8, True, True, True)                       #Imprimir el tiempo de lavado
print(ejemplo)
