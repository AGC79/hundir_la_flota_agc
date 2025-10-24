# Hundir la Flota - Juego en Python

¡Bienvenido a **Hundir la Flota**, una versión en consola del clásico juego de estrategia naval!

## Descripción
Este juego permite al jugador enfrentarse a un rival controlado por la computadora. El objetivo es **hundir todos los barcos del adversario** antes de que tus barcos sean hundidos. Los tableros y los barcos se generan de manera aleatoria, haciendo que cada partida sea diferente.

## Cómo jugar
1. Se muestran las instrucciones al iniciar el juego.
2. Cada jugador (humano y ordenador) lanza los dados para decidir quién comienza.
3. Introduce tus disparos en formato `x,y` (coordenadas de 0 a 9).
4. Los símbolos en el tablero indican:
   - `X` → Acertaste un barco
   - `#` → Agua (fallo)
   - `_` → Casilla sin disparar
5. El juego continúa hasta que todos los barcos de un jugador sean hundidos.

## Requisitos
- Python 3.x
- Librería `numpy`

## Cómo ejecutar
```bash
python main.py
