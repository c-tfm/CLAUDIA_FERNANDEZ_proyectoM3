#Simulación de una máquina de Galton con salida en texto en la consola y como imagen con el uso de matplotlib

import numpy as np #maneja arreglos númericos
import random #esto es lo que asigna "aleatoriamente" pero siguiendo la estructura de la máquina de galton (forma de campana)
from matplotlib import pyplot as plt #nuestro graficador

N_canicas = 3000 #número de cánicas
N_niveles = 12 #niveles asignados

#Simulación de la caída de las canicas para devolver un resultado con el número de canicas en cada contenedor

def GaltonBoard(N_canicas, N_niveles):

#Aquí se crean 13 contenedores, porque así habrán 12 posibles posiciones
#También es donde se guarda el total de veces que fue a la derecha y en que contenedor cayó
#y el arreglo contenedores guarda cuantas cayeron en cada cual

    contenedores = np.zeros(N_niveles + 1, dtype=int)

    for _ in range(N_canicas):
        derecha = 0
        for _ in range(N_niveles):
            test = random.random()
            if test >= 0.5:
                derecha += 1
        contenedores[derecha] += 1

    return contenedores

#Este será el histograma en forma de texto usando "*"

def HistogramaConsola(contenedores):

    max_val = max(contenedores)
    escala = max_val / 50  
#Dejamos un máximo de 50 asteriscos a dibujar

    print("\n=== Resultados en Consola ===")
    print("Contenedor | Canicas | Histograma")
    print("----------------------------------")
    for i, val in enumerate(contenedores):
        num_asteriscos = int(val / escala)
        barra = '*' * num_asteriscos
        print(f"{i:10} | {val:7} | {barra}")
#Esto es lo que dibuja nuestro gráfico en la consola con texto

#Histograma gráfico de simulación con el uso de matplotlib
def HistogramaGrafico(contenedores):

    plt.bar(range(len(contenedores)), contenedores,
            color='skyblue', edgecolor='black')
    plt.xlabel("Contenedores")
    plt.ylabel("Cantidad de Canicas")
    plt.title(f"Máquina de Galton ({N_canicas} canicas, {N_niveles} niveles)")
    plt.show()
#Esta parte del código es la que dibuja el gráfico de barras en nuestra simulación

#Quise agregar algo de texto para que no fuera solo el programa "en blanco"
print("Bienvenido a la Máquina de Galton.")
print(f"Estamos dejando caer {N_canicas} canicas a través de {N_niveles} niveles...\n")
print("Tus canicas están corriendo, espera un momento...\n")
print()

resultados = GaltonBoard(N_canicas, N_niveles)
HistogramaConsola(resultados)
HistogramaGrafico(resultados)