import random

def crear_tablero(filas, columnas, bombas):
    # Crear un tablero vacío
    tablero = [[0 for _ in range(columnas)] for _ in range(filas)]

    # Colocar las bombas aleatoriamente
    bombas_colocadas = 0
    while bombas_colocadas < bombas:
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)

        if tablero[fila][columna] != -1:
            tablero[fila][columna] = -1
            bombas_colocadas += 1

    # Calcular los números alrededor de las bombas
    for fila in range(filas):
        for columna in range(columnas):
            if tablero[fila][columna] != -1:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (0 <= fila + i < filas and 0 <= columna + j < columnas
                                and tablero[fila + i][columna + j] == -1):
                            tablero[fila][columna] += 1

    return tablero

def mostrar_tablero(tablero, mostrar_bombas=False):
    filas = len(tablero)
    columnas = len(tablero[0])

    for fila in range(filas):
        for columna in range(columnas):
            if mostrar_bombas and tablero[fila][columna] == -1:
                print("*", end=" ")
            elif tablero[fila][columna] == -2:
                print("F", end=" ")
            elif tablero[fila][columna] == -3:
                print("?", end=" ")
            else:
                print(tablero[fila][columna], end=" ")

        print()

def destapar_casilla(tablero, destapado, fila, columna):
    if fila < 0 or fila >= len(tablero) or columna < 0 or columna >= len(tablero[0]):
        return

    if destapado[fila][columna]:
        return

    destapado[fila][columna] = True

    if tablero[fila][columna] == 0:
        for i in range(-1, 2):
            for j in range(-1, 2):
                destapar_casilla(tablero, destapado, fila + i, columna + j)

def jugar():
    print("¡Bienvenido al Buscaminas!")
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    bombas = int(input("Ingrese el número de bombas: "))

    tablero = crear_tablero(filas, columnas, bombas)
    destapado = [[False for _ in range(columnas)] for _ in range(filas)]

    while True:
        mostrar_tablero(destapado)

        fila = int(input("Ingrese la fila: "))
        columna = int(input("Ingrese la columna: "))

        if tablero[fila][columna] == -1:
            print("¡Perdiste! Has encontrado una bomba.")
            mostrar_tablero(tablero, mostrar_bombas=True)
            break
        elif tablero[fila][columna] != 0:
            destapado[fila][columna] = True
       
