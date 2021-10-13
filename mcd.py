

while True:
    pregunta = input('Hola!, ¿Desea calcular el MCD de dos valores utilizando el algoritmo de Euclides?: (Si/No)\n')
    if pregunta == 'Si':
        print('Ok, comenzemos!\n')
        x = input('Ingrese el primer numero y presione enter: \n')
        y = input('Ingrese el segundo numero y presione enter: \n')
        try:
            entero_x = int(x)
            entero_y = int(y)
            print('Correcto, son dos numeros enteros.\n')
            x = int(x)
            y = int(y)
        except ValueError or TypeError:
            print('No escribiste numeros enteros.\n')
            continue 
        def mcd(x , y):
            mcd = 1 # Le asignamos por defecto 1 como MCD
            if x % y == 0:
                return y # Me regresa el MCD
            for k in range(int(y/2), 0, -1):
                if x % k == 0 and y % k == 0: # Significa que k es el MCD para x y
                   mcd = k
                   break
            return mcd
        print('El MCD de los valores ' ,x, ' y', y, ' es: ', mcd(x,y), '\n')
        print('Muchas gracias!')
    elif pregunta == 'No':
        print('Muchas gracias!')
        break
    else:
        print('Por favor responder (Si/No)\n')
        
        
        
