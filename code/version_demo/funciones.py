import numpy as np
import random
import time

# Función que presenta el juego
def presentacion():
    print("\t*************************************")
    print("\t*                                   *")
    print("\t*  ¡Bienvenido a Hundir la Flota!   *")
    print("\t*                                   *")
    print("\t*************************************\n")
    print("\t*******Instrucciones básicas:*******")
    print("-" * 65)
    print("- Tu objetivo es hundir todos los barcos de tu rival")
    print("- Introduce las coordenadas para disparar en formato x,y")
    print("- Las coordenadas van de 0 a 9 tanto en filas como en columnas")
    print("- X indica un acierto, # indica agua y '_' un espacio sin disparar\n")
    print("-" * 65)

# Función para crear matriz del tablero
def tablero():
    matriz_tablero = np.full((10,10), "_")
    return matriz_tablero

# Función para crear el tablero del jugador con los barcos colocados de manera aleatroria
def crear_tablero_jugador(): 

    tablero_jugador = tablero()

    barcos_plantilla = [[[0,0], [0,0]], 
                        [[0,0], [0,0], [0,0]]]

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
            solapamiento = False # bandera
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

    barcos_plantilla = [[[0,0], [0,0]], 
                        [[0,0], [0,0], [0,0]]]


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
        input("Pulsa Intro para tirar tus dados...\n" \
        "El jugador con la puntuación mas alta iniciará la partida")

        num_inicio_jugador = random.randint(1, 12)

        print()
        print(f"Has sacado el número {num_inicio_jugador}, espera a que tu rival lance los suyos...")

        time.sleep(4)

        num_inicio_rival = random.randint(1, 12)

        if num_inicio_jugador > num_inicio_rival:
            print()
            print(f"Tu rival ha sacado el número {num_inicio_rival}, empiezas jugando tú.")
            turno = "jugador"
            return turno
        elif num_inicio_jugador < num_inicio_rival:
            print()
            print(f"Tu rival ha sacado el número {num_inicio_rival}, espera a que dispare primero.")
            turno = "rival"
            return turno
        else:
            print()
            print(f"Tu rival ha sacado el número {num_inicio_rival}, es el mismo que el tuyo asi que teneis que lanzar otra vez los dados.")

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
            disparo_jugador = input("Dispara introduciendo coordenadas con formato x,y\n")
            disparo_jugador = disparo_jugador.replace("(", "").replace(")", "").replace(" ", "")

            try:
                x, y = disparo_jugador.split(",")
                x, y = int(x), int(y)
            except:
                print()
                print("Formato de disparo no válido.")
                continue

            resultado, fila, columna = disparar(tablero_rival, tablero_rival_disparos, x, y)

            if resultado == "Tocado":
                disparos_acertados_jugador.append([fila, columna])
                print()
                print("Tu disparo ha tenido éxito, vuelve a disparar.")
                print()
                print(tablero_rival_disparos)

                # Comprobar si algún barco se ha hundido
                # Se recorre la lista de barcos creada al colocar los barcos en el tablero rival
                for barco in barcos_rival_total:
                    hundido = True # bandera, se empieza asumiendo que el barco se ha hundido
                    for coord in barco:
                        # Se comparan los elementos de la lista de barcos rival, con la lista de disparos acertados
                        # Si algno no esta se sale del bucle for
                        if coord not in disparos_acertados_jugador:
                            hundido = False
                            break
                    # Aquí hundido es True y el barco aún no esta en la lista de barcos hundidos
                    # Se revisa que el barco aún no esta porque al hundir un barco se sigue disparando
                    # Entonces se vuelve a revisar la lista y se vuelve a imprimir el mensaje si no se comprueba esta condición         
                    if hundido and barco not in barcos_hundidos_jugador:
                        barcos_hundidos_jugador.append(barco)
                        print()
                        print(f"¡Un barco enemigo de eslora {len(barco)} ha sido hundido!")
                        print()
                        print(tablero_rival_disparos)

                # Comprobar si todos los barcos han sido hundidos
                if len(barcos_hundidos_jugador) == len(barcos_rival_total):
                    print()
                    print("\n¡Todos los barcos enemigos han sido hundidos! ¡Has ganado!")
                    print()
                    print(tablero_rival_disparos)
                    print()
                    break

                continue  # sigue disparando

            elif resultado == "Agua":
                print()
                print("Has fallado. Pasa el turno a tu rival.")
                print()
                print(tablero_rival_disparos)
                turno = "rival"

            else:  # Repetir
                print()
                print("Ya has disparado aquí, vuelve a disparar.")
                print()
                print(tablero_rival_disparos)
                continue

        # TURNO DEL RIVAL (EL ORDENADOR)
        if turno == "rival":
            time.sleep(5)

            print("\n*** Turno de tu rival ***")

            while True:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                if (x, y) not in disparos_acertados_rival:
                    break

            resultado, fila, columna = disparar_automatizado(tablero_jugador, tablero_jugador_disparos, x, y)

            if resultado == "Tocado":
                disparos_acertados_rival.append([fila, columna])
                print()
                print("El disparo de tu rival ha tenido éxito, volverá a disparar.")
                print()
                print(tablero_jugador_disparos)

                # Comprobar si algún barco se ha hundido
                for barco in barcos_jugador_total:
                    hundido = True
                    for coord in barco:
                        if coord not in disparos_acertados_rival:
                            hundido = False
                            break

                    if hundido and barco not in barcos_hundidos_rival:
                        barcos_hundidos_rival.append(barco)
                        print()
                        print("¡Barco hundido de eslora", len(barco), "!")
                        print()
                        print(tablero_jugador_disparos)

                # Comprobar si todos los barcos han sido hundidos
                if len(barcos_hundidos_rival) == len(barcos_jugador_total):
                    print()
                    print("\n¡Todos tus barcos han sido hundidos! ¡Has perdido!")
                    print()
                    print(tablero_jugador_disparos)
                    print()
                    break

                continue  

            elif resultado == "Agua":
                disparos_acertados_rival.append([fila, columna])
                print()
                print("Tu rival ha fallado. Es tu turno.")
                print()
                print(tablero_jugador_disparos)
                turno = "jugador"
    