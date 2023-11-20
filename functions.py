import random

# INICIALIZACIÓN
# Generar una lista de 8 números aleatorios entre 0 y 7 (representando las columnas)
def individuo():
    return random.sample(range(8), 8)

# Población con 50 individuos aleatorios
def pob(n):
    poblacion = []
    for i in range(n):
        poblacion.append(individuo())
    return poblacion


# FITNESS
def fitness(tablero):
    ataques = sum(1 for i in range(8) for j in range(i + 1, 8) if abs(tablero[i] - tablero[j]) == abs(i - j))
    return ataques


# SELECCIÓN DE PADRES UNIVERSAL ESTOCÁSTICA
def proba_ac(pob):
    acum = 0.0
    probabilidades = []
    suma = sum(fitness(i) for i in pob)
    for i in pob:
        proba = fitness(i) / suma
        acum = acum + proba
        probabilidades.append(acum)
    return probabilidades


# SELECCIÓN DE PADRE UNIVERSAL ESTOCÁSTICA
def seleccion_padres(poblacion, lam):
    current_member = 1
    k = 1
    r = random.uniform(0, 1 / lam)
    padres = []
    probabilidades = proba_ac(poblacion)
    while current_member <= lam:
        while r <= probabilidades[k]:
            padres.append(poblacion[current_member])
            r += 1 / lam
            current_member += 1
        k += 1
    return padres


# CRUZA A LOS EXTREMOS
def crear_tabla(papa, mama):
    tabla_extr = []

    for i in range(8):
        # Encuentra los índices correspondientes al elemento i en papa y mama
        indice_papa = papa.index(i)
        indice_mama = mama.index(i)

        # Encuentra los elementos adyacentes basados en los índices encontrados
        elementos_adyacentes = [
            papa[(indice_papa + 1) % 8],
            papa[(indice_papa - 1) % 8],
            mama[(indice_mama + 1) % 8],
            mama[(indice_mama - 1) % 8]
        ]
        tabla_extr.append(elementos_adyacentes)
    return tabla_extr

def cruza_extremos(papa, mama):
    tabla_ex = crear_tabla(papa, mama)

    # Selección del primer elemento aleatorio
    inicio = random.choice(papa)
    hijo = [inicio]
    current_element = inicio

    while len(hijo) < 8:
        # Crear nuevas listas de elementos adyacentes sin current_element
        new_tabla_ex = [elements for elements in tabla_ex]
        for elements in tabla_ex:
            while current_element in elements:
                elements.remove(current_element)
        tabla_ex = new_tabla_ex

        extremos = tabla_ex[current_element]
        lista_extr = []
        for i in extremos:
            lista_extr.append(tabla_ex[i])

        extr_repet = [element for element in extremos if extremos.count(element) > 1]
        if extr_repet:
            # Escoge el elemento que se repite
            next_element = random.choice(extr_repet)
        elif len(tabla_ex[current_element]) == 1:
            # Escoge el elemento si solo contiene un elemento
            next_element = random.choice(tabla_ex[current_element])
        elif lista_extr:
            # Encuentra el siguiente elemento con la lista más corta
            min_len = min(len(element) for element in lista_extr)
            candidates = [element for element in lista_extr if len(element) == min_len]
            next_element = tabla_ex.index(random.choice(candidates))

        hijo.append(next_element)
        current_element = next_element
    return hijo


# MUTACIÓN
def mezcla(individuo):
    # Elegir punto de inicio y final
    punto_1, punto_2 = random.sample(range(8), 2)
    punto_1, punto_2 = min(punto_1, punto_2), max(punto_1, punto_2)

    # Mezclar los elementos entre los puntos inicial y final
    entre_puntos = individuo[punto_1:punto_2 + 1]
    random.shuffle(entre_puntos)

    # Reemplazar los elementos en el individuo original
    individuo[punto_1:punto_2 + 1] = entre_puntos

    return individuo


# REMPLAZO
def brecha_generacional(padres, hijos, lam):
    fitness_padres = [fitness(i) for i in padres]

    indices_eliminar = sorted(range(len(fitness_padres)), key=lambda i: fitness_padres[i])[lam:]
    nuevos_padres = [padres[i] for i in range(len(padres)) if i not in indices_eliminar]
    nuevos_padres.extend(hijos[lam:])

    return nuevos_padres