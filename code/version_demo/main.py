import funciones as f

f.presentacion()

# Crear tableros y barcos
tablero_jugador, barcos_jugador_total = f.crear_tablero_jugador()
tablero_rival, barcos_rival_total = f.crear_tablero_rival()
print()
print("Visualización de los barcos y tablero rival para demostración\n")
print(barcos_rival_total)
print()
print(tablero_rival)
print()

# Crear tableros vacíos para registrar los disparos
tablero_jugador_disparos = f.tablero()
tablero_rival_disparos = f.tablero()

# Decidir quién empieza
turno = f.inicio_partida()

# Iniciar la partida
f.jugar_partida(
    turno,
    tablero_jugador,
    tablero_jugador_disparos,
    barcos_jugador_total,
    tablero_rival,
    tablero_rival_disparos,
    barcos_rival_total
)


