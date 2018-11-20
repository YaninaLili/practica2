



while True:
    
    print("Calculando suma diagonal de matriz de orden 3x3")
    print()
    x=int(input("Ingresar numero en la fila 1 y columna 1: "))
    y=int(input("Ingresar numero en la fila 1 y columna 2: "))
    z=int(input("Ingresar numero en la fila 1 y columna 3: "))

    print()

    x1=int(input("Ingresar numero en la fila 2 y columna 1: "))
    y1=int(input("Ingresar numero en la fila 2 y columna 2: "))
    z1=int(input("Ingresar numero en la fila 2 y columna 3: "))

    print()
    x2=int(input("Ingresar numero en la fila 3 y columna 1: "))
    y2=int(input("Ingresar numero en la fila 3 y columna 2: "))
    z2=int(input("Ingresar numero en la fila 3 y columna 3: "))
    
    print()

    print(x,y,z)
    print(x1,y1,z1)
    print(x2,y2,z2)

    sumaDiagonal=(x+y1+z2)
    print()
    print("La suma de la diagonal principal de la matriz  es: ",sumaDiagonal)
    break
