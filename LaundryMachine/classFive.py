time = 0
kg = int(input('Ingrese la cantidad de ropa en kg: '))
lavar = input('¿Desea lavar la ropa? (s/n): ')
enjuagar = input('¿Desea enjuagar la ropa? (s/n): ')
exprimir = input('¿Desea exprimir la ropa? (s/n): ')

if kg > 15:
    print('La cantidad de ropa excede el límite de carga')
else:   
    if lavar == 's':
        time += 25
    if enjuagar == 's':
        time += 10
    if exprimir == 's':
        time += 10

    if lavar == 's' and enjuagar == 's':
        time += (kg * 3 / 10) * 2
    elif (lavar == 's' and enjuagar == 'n') or (lavar == 'n' and enjuagar == 's'):
        time += kg * 3 / 10
    else:
        time += 0

print(time)
