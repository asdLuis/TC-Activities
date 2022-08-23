def main():
    counter = 0
    n = int(input('Ingrese un número: '))
    number = n
    print('El numbero actual es', number)
    while number < 1000:
        n = int(input('Ingrese un número: '))
        counter += 1
        number += n
        print('La suma actual es: ', number)
    print('La sumatoria total una vez alcanzado el 1000 es:', number, 'y la cantidad de números ingresados es:', counter)

main()


