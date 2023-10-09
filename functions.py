import random

# INICIALIZACION}

# Generar una lista de 8 números aleatorios entre 0 y 7 (representando las columnas)
def individuo():
    return random.sample(range(8), 8)

# Inicio con 50 individuos aleatorios
poblacion = []
for i in range(50):
    poblacion.append(individuo())

# FITNESS
def fitness(tablero):
    ataques = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if tablero[i] == tablero[j] or abs(tablero[i] - tablero[j]) == abs(i - j):
                ataques += 1
    return 28 - ataques





# SELECCION DE PADRES UNIVERSAL ESTOCASTICA

# Probabilidades acumuladas lista
def proba_ac(pob):
    suma = 0
    acum = 0.0
    probabilidades = []
    for i in pob:
        suma = suma + fitness(i)
    for i in pob:
        proba = fitness(i) / suma
        acum = acum + proba
        probabilidades.append(acum)
    return probabilidades




# Seleccion de padres universal estocastica

# k = 1
# lam = len(poblacion)
# r = random.uniform(0, 1/lam )
# while k <= lam:
#     while r <= ac[k]:
#         poblacion[k]

# CRUZA


# MUTACION
def mezcla(individuo):
    # Elegir punto de inicio y final
    punto_1, punto_2 = random.sample(range(8), 2)
    punto_1, punto_2 = min(punto_1, punto_2), max(punto_1, punto_2)

    # Mezclar los elementos entre los puntos de corte
    entre_puntos = individuo[punto_1:punto_2 + 1]
    random.shuffle(entre_puntos)

    # Reemplazar los elementos en el individuo original
    individuo[punto_1:punto_2 + 1] = entre_puntos

    return individuo


tabbb = [0, 1, 2, 3, 4, 5, 6, 7]
tabbb_m = mezcla(tabbb)
print(fitness(tabbb))

