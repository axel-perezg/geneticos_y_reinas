import random


# INICIALIZACION

# Inicio con miu individuos aleatorios

# Generar una lista de 8 números aleatorios entre 0 y 7 (representando las columnas)
def individuo():
    return random.sample(range(8), 8)


poblacion = []
for i in range(50):
    poblacion.append(individuo())


# FITNESS

def fitness(tablero):
    ataques = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if tablero[i] == tablero[j] or tablero[i] - tablero[j] == i - j:
                ataques += 1
    return ataques


tablero = [1, 3, 0, 2, 5, 7, 6, 4]  # Tablero con una configuración de reinas
fitness = fitness(tablero)
print("Fitness del tablero:", fitness)
