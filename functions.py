import random


# INICIALIZACION

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
    ataques = sum(1 for i in range(8) for j in range(i + 1, 8) if
                  tablero[i] == tablero[j] or abs(tablero[i] - tablero[j]) == abs(i - j))
    return 1 / (ataques + 1)


# ejem = [0, 1, 2, 3, 4, 5, 6, 7]
#
# print(fitness(ejem))


# SELECCION DE PADRES UNIVERSAL ESTOCASTICA

# Probabilidades acumuladas lista

# miu es el numero de poblacion total
# lamnda es el numero de padres que voy a escoher

def proba_ac(pob):
    suma = 0
    acum = 0.0
    probabilidades = []
    suma = sum(fitness(i) for i in pob)
    for i in pob:
        proba = fitness(i) / suma
        acum = acum + proba
        probabilidades.append(acum)
    return probabilidades


# SELECCION DE PADRE UNIVERSAL ESTOCASTICA
# Given the cumulative probability distribution 'ac'
# and assuming we wish to select 'lam' members of the mating pool
current_member = 1
k = 1
lam = 4
r = random.uniform(0, 1 / lam)
padres = []

while current_member <= lam:
    while r <= proba_ac(poblacion)[k]:
        padres.append(poblacion[current_member])
        r += 1 / lam
        current_member += 1
    k += 1


# en ves de guardar una losta de padres seleccionados, guardar una lista con los indices correspondientes en la poblacion

# escojo 25 papas y 25 mamas, luego de cada pareja voy a tener dos hijos 'distinots', ya de ahi la poblacion es de 50 y los 50 hijos que genere


# CRUZA A LOS EXTREMOS


def crear_tabla(papa, mama):
    tabla_extr = {}
    for i in range(8):
        tabla_extr[i] = [
            papa[(i + 1) % 8],
            papa[(i - 1) % 8],
            mama[(i + 1) % 8],
            mama[(i - 1) % 8]
        ]
    return tabla_extr


def cruza_extr(papa, mama):
    tabla = crear_tabla(papa, mama)
    inicial = random.choice(papa)
    hijo = [inicial]
    current_element = inicial
    current_nuevo = None

    while len(hijo) < 8:
        for element in tabla:
            tabla[element] = [m for m in tabla[element] if m != current_element]
            if not tabla[element]:
                del tabla[element]

        vecinos = tabla[current_element]
        for numero in vecinos:
            if vecinos.count(numero) > 1:
                current_nuevo = numero
                break
            elif current_nuevo is None:
                current_nuevo = min(tabla.values())
            else:
                current_nuevo = random.randint(0,7)
        current_element = current_nuevo
    return hijo


tabla = cruza_extr([0,1,2,3,4,5,6,7], [3,7,0,2,6,5,1,4])

print(tabla)





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


