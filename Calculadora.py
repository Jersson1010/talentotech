import math as m

while True:
    print('\n===== Menú Calculadora =====\n' \
            '1. Suma\n'
            '2. Resta\n'
            '3. Multiplicación\n'
            '4. División\n'
            '5. Potencia\n'
            '6. Raiz Cuadrada\n'
            '7. Factorial\n'
            '8. Seno\n'
            '9. Coseno\n'
            '10. Modulo\n'
            '0. Salir\n')

    opcion = int(input('Escoja una opción: '))

    if opcion == 0:
        break

    if opcion in [1,2,3,4]:
        numero_uno = int(input('Digite el primer número: '))
        numero_dos = int(input('Digite el segundo número: '))
    elif opcion == 5:
        base = int(input('Digite el la base: '))
        exponente = int(input('Digite el exponente: '))
    else:
        numero_uno = int(input('Digite el número: '))
    
    
    # opcion 1 - Suma
    if opcion ==1:
        print('=== Resultado suma ===')
        print(numero_uno, '+', numero_dos, '=', numero_uno+numero_dos)
    # opcion 2 - Resta
    elif opcion == 2:
        print('=== Resultado resta ===')
        print(numero_uno, '-', numero_dos, '=', numero_uno-numero_dos)
    # opcion 3 - multiplicacion
    elif opcion == 3:
        print('=== Resultado multiplicacion ===')
        print(numero_uno, '*', numero_dos, '=', numero_uno*numero_dos)
    elif opcion == 4:
        print('=== Resultado division ===')
        print(numero_uno, '/', numero_dos, '=', numero_uno/numero_dos)

    # opcion 5 - Potencia
    if opcion == 5:
        print('=== Resultado potencia ===')
        print(base, '^', exponente, '=', base**exponente)

    # opcion 6 - Raiz cuadrada
    if opcion == 6:
        print('=== Raiz cuadrada ===')
        print('Raiz cuadrada de: ', numero_uno, '=', m.sqrt(numero_uno))
    # opcion 7 - factorial
    elif opcion == 7:
        print('=== Factorial ===')
        print('Factorial de: ', numero_uno, '=', m.factorial(numero_uno))
    # opcion 8 - seno
    elif opcion == 8:
        print('=== Seno ===')
        num_rad = m.radians(numero_uno)
        print('Seno de: ', numero_uno, '=', m.sin(num_rad))
    # opcion 9 - coseno
    elif opcion == 9:
        print('=== Coseno ===')
        num_rad = m.radians(numero_uno)
        print('Coseno de: ', numero_uno, '=', m.cos(num_rad))
    # opcion 10 - tangente
    elif opcion == 10:
        print('=== Tangente ===')
        print('Tangente de: ', numero_uno, '=', m.tan(numero_uno))
    # opcion 0 - salir
