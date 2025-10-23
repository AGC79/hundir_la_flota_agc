import numpy as np
import random
import time

# Función para crear matriz del tablero
def tablero():
    matriz_tablero = np.full((10,10), "_")
    return matriz_tablero

# Función para crear el tablero del jugador con los barcos colocados de manera aleatroria
def crear_tablero_jugador(): 

    tablero_jugador = tablero()

    barcos_plantilla = [
        [[0,0], [0,0]], 
        [[0,0], [0,0]]
    ]

    barcos_jugador_total = []

    for i in range(len(barcos_plantilla)): # i es el indice de cada barco iterado
        eslora = len(barcos_plantilla[i])
        orientacion = random.choice(["N", "S", "E", "W"])
        
        while True:

            # Lista para guardar coordenadas. Si hay solapamiento, se reinicia el while y se vuelve a generar otra
            barcos_jugador = []

            # Límites en la matriz para colocar la primera casilla de los barcos. Se establecen a la hora de generar las coordenadas aleatorias
            if orientacion == "N":
                # eslora -1, es la casilla inicial hacia arriba, contando desde la posición 0 hacia abajo
                fila = random.randint(eslora - 1, 9) # [3,5]
                columna = random.randint(0, 9)
            elif orientacion == "S":
                # 10 - eslora, es la casilla inicial hacia abajo, contando desde la posición 0 hacia abajo
                fila = random.randint(0, 10 - eslora)
                columna = random.randint(0, 9)
                # 10 - eslora, es la casilla inicial hacia la derecha, contando desde la posicion 0 hacia la izquierda
            elif orientacion == "E":
                fila = random.randint(0, 9)
                columna = random.randint(0, 10 - eslora)
            else:  # W
                # eslora - 1, es la casilla inicial hacia la izquierda, contando desde la posicion 0 hacia la izquierda
                fila = random.randint(0, 9)
                columna = random.randint(eslora - 1, 9)
            
            barcos_jugador.append([fila, columna])
            
            # Resto de casillas según la orientación
            # j es el elemento de la eslora iterado
            # el elemento de la posición 0 de la eslora de los barcos ya se ha asignado, la iteración se realiza sobre el rango entre el elemento 1 de la eslora de cada barco
            # i longitud de la eslora (sin contar el ultimo numero)
            for j in range(1, eslora): 
                if orientacion == "N":
                    fila_o = fila - j # [2,5][1,5][0,5]
                    columna_o = columna
                elif orientacion == "S":
                    fila_o = fila + j
                    columna_o = columna
                elif orientacion == "E":
                    fila_o = fila
                    columna_o = columna + j
                else:  # "O"
                    fila_o = fila
                    columna_o = columna - j
                barcos_jugador.append([fila_o, columna_o])

            # print(barcos_jugador)
            solapamiento = False
            for fila, columna in barcos_jugador:
                if tablero_jugador[fila, columna] == "O":
                    solapamiento= True # Como se encuentra solapamiento, se sale del bucle for y se comienza de nuevo el while
                    break 
            if not solapamiento:
                for fila, columna in barcos_jugador:
                    tablero_jugador[fila, columna] = "O"
                barcos_jugador_total.append(barcos_jugador)
                break # si no hay solapamiento, se ponen los barcos y se sale del bucle while

    return tablero_jugador, barcos_jugador_total


# Función para crear el tablero del rival (el ordenador) con los barcos colocados de manera aleatroria
def crear_tablero_rival():
    tablero_rival = tablero()

    barcos_plantilla = [
        [[0,0], [0,0]], 
        [[0,0], [0,0]]
    ]

    barcos_rival_total = []

    for i in range(len(barcos_plantilla)): # i es el indice de cada barco iterado
        eslora = len(barcos_plantilla[i])
        orientacion = random.choice(["N", "S", "E", "W"])
        
        while True:

            # Lista para guardar coordenadas. Si hay solapamiento, se reinicia el while y se vuelve a generar otra
            barcos_rival = []

            # Límites en la matriz para colocar la primera casilla de los barcos. Se establecen a la hora de generar las coordenadas aleatorias
            if orientacion == "N":
                # eslora -1, es la casilla inicial hacia arriba, contando desde la posición 0 hacia abajo
                fila = random.randint(eslora - 1, 9)
                columna = random.randint(0, 9)
            elif orientacion == "S":
                # 10 - eslora, es la casilla inicial hacia abajo, contando desde la posición 0 hacia abajo
                fila = random.randint(0, 10 - eslora)
                columna = random.randint(0, 9)
                # 10 - eslora, es la casilla inicial hacia la derecha, contando desde la posicion 0 hacia la izquierda
            elif orientacion == "E":
                fila = random.randint(0, 9)
                columna = random.randint(0, 10 - eslora)
            else:  # W
                # eslora - 1, es la casilla inicial hacia la izquierda, contando desde la posicion 0 hacia la izquierda
                fila = random.randint(0, 9)
                columna = random.randint(eslora - 1, 9)
            
            barcos_rival.append([fila, columna])
            
            # Resto de casillas según la orientación
            # j es el elemento de la eslora iterado
            # el elemento de la posición 0 de la eslora de los barcos ya se ha asignado, la iteración se realiza sobre el rango entre el elemento 1 de la eslora de cada barco
            # i longitud de la eslora (sin contar el ultimo numero)
            for j in range(1, eslora): 
                if orientacion == "N":
                    fila_o = fila - j # [2,5][1,5][0,5]
                    columna_o = columna
                elif orientacion == "S":
                    fila_o = fila + j
                    columna_o = columna
                elif orientacion == "E":
                    fila_o = fila
                    columna_o = columna + j
                else:  # "O"
                    fila_o = fila
                    columna_o = columna - j
                barcos_rival.append([fila_o, columna_o])

            # print(barcos_jugador)
            solapamiento = False
            for fila, columna in barcos_rival:
                if tablero_rival[fila, columna] == "O":
                    solapamiento= True # Como se encuentra solapamiento, se sale del bucle for y se comienza de nuevo el while
                    break 
            if not solapamiento:
                for fila, columna in barcos_rival:
                    tablero_rival[fila, columna] = "O"
                barcos_rival_total.append(barcos_rival)
                break # si no hay solapamiento, se ponen los barcos y se sale del bucle while

    return tablero_rival, barcos_rival_total

# Función que gestiona los disparos manuales del jugador
def disparar(tablero_rival_01, tablero_rival_02, fila, columna):
    if tablero_rival_01[fila, columna] == "O":
        print("Tocado")
        tablero_rival_02[fila, columna] = "X"
        return "Tocado", fila, columna
    elif tablero_rival_02[fila, columna] in ("X", "#"):
        return "Repetir", None, None
    else:
        print("Agua")
        tablero_rival_02[fila, columna] = "#"
        return "Agua", fila, columna
    
# Función que gestiona los disparos automatizados del rival (el ordenador)
def disparar_automatizado(tablero_jugador_01, tablero_jugador_02, fila, columna):
    if tablero_jugador_01[fila, columna] == "O":
        print("Tocado")
        tablero_jugador_02[fila, columna] = "X"
        return "Tocado", fila, columna
    else:
        print("Agua")
        tablero_jugador_02[fila, columna] = "#"
        return "Agua", fila, columna
    
# Función que gestiona el inicio de la partida
def inicio_partida():
    while True:
        input("Pulsa Intro para tirar tus dados...")

        num_inicio_jugador = random.randint(1, 101)

        print("Has sacado el número", num_inicio_jugador, "espera a que tu rival lance los suyos...")

        time.sleep(4)

        num_inicio_rival = random.randint(1, 101)

        if num_inicio_jugador > num_inicio_rival:
            print("Tu rival ha sacado el número ", num_inicio_rival, ", empiezas jugando tú.")
            turno = "jugador"
            return turno
        elif num_inicio_jugador < num_inicio_rival:
            print("Tu rival ha sacado el número ", num_inicio_rival, ", espera a que dispare primero.")
            turno = "rival"
            return turno
        else:
            print("Tu rival ha sacado el número ", num_inicio_rival, ", es el mismo que el tuyo asi que teneis que lanzar otra vez los dados.")

# Función que gestiona el desarrollo de la partida
def jugar_partida(
    turno, 
    tablero_jugador, 
    tablero_jugador_disparos, 
    barcos_jugador_total,
    tablero_rival, 
    tablero_rival_disparos, 
    barcos_rival_total
):
    disparos_acertados_jugador = []
    barcos_hundidos_jugador = []
    disparos_acertados_rival = []
    barcos_hundidos_rival = []

    while True:

        # TURNO DEL JUGADOR
        if turno == "jugador":
            print("\n*** Tu turno ***")
            disparo_jugador = input("Dispara introduciendo coordenadas en el siguiente formato (x, y)...")
            disparo_jugador = disparo_jugador.replace("(", "").replace(")", "").replace(" ", "")

            try:
                x, y = disparo_jugador.split(",")
                x, y = int(x), int(y)
            except:
                print("Formato de disparo no válido.")
                continue

            resultado, fila, columna = disparar(tablero_rival, tablero_rival_disparos, x, y)

            if resultado == "Tocado":
                disparos_acertados_jugador.append((fila, columna))
                print("Tu disparo ha tenido éxito, vuelve a disparar.")
                print()
                print(tablero_rival_disparos)

                # Comprobar si algún barco se ha hundido
                for barco in barcos_rival_total:
                    coords_barco = []
                    for coordenada in barco:
                        coords_barco.append(tuple(coordenada))

                    hundido = True
                    for c in coords_barco:
                        if c not in disparos_acertados_jugador:
                            hundido = False
                            break

                    if hundido and barco not in barcos_hundidos_jugador:
                        barcos_hundidos_jugador.append(barco)
                        print("¡Un barco enemigo de eslora", len(barco), " ha sido hundido!")
                        print()
                        print(tablero_rival_disparos)

                # Comprobar si todos los barcos han sido hundidos
                if len(barcos_hundidos_jugador) == len(barcos_rival_total):
                    print("\n¡Todos los barcos enemigos han sido hundidos! ¡Has ganado!")
                    print()
                    print(tablero_rival_disparos)
                    break

                continue  # sigue disparando

            elif resultado == "Agua":
                print("Has fallado. Pasa el turno a tu rival.")
                print()
                print(tablero_rival_disparos)
                turno = "rival"

            else:  # Repetir
                print("Ya has disparado aquí, vuelve a disparar.")
                print()
                print(tablero_rival_disparos)
                continue

        # TURNO DEL RIVAL (EL ORDENADOR)
        if turno == "rival":
            print("\n*** Turno de tu rival ***")

            while True:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                if (x, y) not in disparos_acertados_rival:
                    break

            resultado, fila, columna = disparar_automatizado(tablero_jugador, tablero_jugador_disparos, x, y)

            if resultado == "Tocado":
                disparos_acertados_rival.append((fila, columna))
                print("El disparo de tu rival ha tenido éxito, volverá a disparar.")
                print()
                print(tablero_jugador_disparos)

                # Comprobar si algún barco se ha hundido
                for barco in barcos_jugador_total:
                    coords_barco = []
                    for coordenada in barco:
                        coords_barco.append(tuple(coordenada))

                    hundido = True
                    for c in coords_barco:
                        if c not in disparos_acertados_rival:
                            hundido = False
                            break

                    if hundido and barco not in barcos_hundidos_rival:
                        barcos_hundidos_rival.append(barco)
                        print("¡Barco hundido de eslora", len(barco), "!")
                        print()
                        print(tablero_jugador_disparos)

                # Comprobar si todos los barcos han sido hundidos
                if len(barcos_hundidos_rival) == len(barcos_jugador_total):
                    print("\n¡Todos tus barcos han sido hundidos! ¡Has perdido!")
                    print()
                    print(tablero_jugador_disparos)
                    break

                continue  

            elif resultado == "Agua":
                disparos_acertados_rival.append((fila, columna))
                print("Tu rival ha fallado. Es tu turno.")
                print()
                print(tablero_jugador_disparos)
                turno = "jugador"
    