import functions
import matplotlib.pyplot as plt


# Generamos la población aleatoria
poblacion = functions.pob(50)

# Fijamos el número de generaciones
num_generaciones = 20
fit_generacion = []

for generacion in range(num_generaciones):
    fitness_poblacion = [functions.fitness(individuo) for individuo in poblacion]
    promedio_fitness = sum(fitness_poblacion) / len(fitness_poblacion)
    # Añadimos el promedio del fitness de la población
    fit_generacion.append(promedio_fitness)

    # Seleccionamos a los padres
    padres = functions.seleccion_padres(poblacion, 25)
    madres = functions.seleccion_padres(poblacion, 25)

    # Creamos a los hijos
    hijos_1 = [functions.cruza_extremos(i, j) for i, j in zip(padres, madres)]
    hijos_2 = [functions.cruza_extremos(i, j) for i, j in zip(madres, padres)]
    hijos = hijos_1 + hijos_2

    # Mutamos a los hijos
    for i in range(50):
        hijos[i] = functions.mezcla(hijos[i])

    # Eliminamos a los 25 peores padres para agregar 25 hijos
    poblacion = functions.brecha_generacional(poblacion, hijos, 25)

    tableros_perf_ind = [i for i, fitness in enumerate(fitness_poblacion) if fitness == 0]
    tableros_perf = [poblacion[i] for i in tableros_perf_ind]
    print(f'En la Generación {generacion + 1} existen {len(tableros_perf)} tableros perfectos y son: {tableros_perf}')



plt.figure(figsize=(10, 6), dpi=300)

plt.plot(range(1, num_generaciones + 1), fit_generacion, marker='o', linestyle='-', color='b', label='Fitness Promedio')


plt.scatter(num_generaciones, fit_generacion[-1], color='r', label='Última Generación', zorder=5)

plt.title('Evolución del Fitness en cada Generación', fontsize=18)
plt.xlabel('Generación', fontsize=14)
plt.ylabel('Fitness Promedio', fontsize=14)
plt.xticks(range(1, num_generaciones + 1))  # Asegurar etiquetas de eje x como enteros
plt.grid(True, linestyle='--', alpha=0.7)

plt.text(num_generaciones + 0.5, fit_generacion[-1], f'{fit_generacion[-1]:.2f}', color='r', fontsize=12)
plt.legend()

plt.savefig('grafica_fitness.svg', bbox_inches='tight')

plt.show()