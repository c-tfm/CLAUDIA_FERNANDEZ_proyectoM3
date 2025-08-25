# CLAUDIA_FERNANDEZ_proyectoM3


# - Simulación de la Máquina de Galton

Este proyecto implementa una simulación de la máquina de Galton en Python.  
La máquina de Galton es un dispositivo ideado por Sir Francis Galton que muestra cómo decisiones aleatorias binarias (izquierda/derecha) producen al final una distribución aproximadamente normal con el efecto de la campana de Gauss.

En nuestro caso:

- Simulamos **3000 canicas**.
- Cada canica pasa por **12 niveles de obstáculos**.
- Al final, las canicas caen en 13 contenedores posibles (desde 0 hasta 12 pasos a la derecha).

El programa muestra los resultados en dos formas:

1. Histograma en consola como texto (usando `*`).  
2. Histograma gráfico (usando `matplotlib`).  

---

## Funcionamiento del programa

1. **Librerías usadas**

   
   - `numpy`: para crear y manejar arreglos numéricos de manera eficiente.  
   - `random`: para generar números aleatorios entre 0 y 1, simulando la decisión de cada canica en cada nivel (por la decisiones binarias). 
   - `matplotlib.pyplot`: para graficar el histograma de forma visual y clara.  

2. **Estructura del código**
   
   - `GaltonBoard(N_canicas, N_niveles)`: simula el recorrido de todas las canicas y devuelve cuántas caen en cada contenedor.  
   - `HistogramaConsola(contenedores)`: imprime en la terminal un histograma hecho con `*`, mostrando la distribución de manera textual.  
   - `HistogramaGrafico(contenedores)`: genera un gráfico de barras con `matplotlib`.  

3. **Ejecución**
   
   Al ejecutar el programa:  
   - Se muestra un breve mensaje en consola simulando que están corriendo las canicas y acomodandose.  
   - Luego se muestra el histograma en texto
   - Finalmente, se abre una ventana emergente, con el gráfico en imagen y coordenadas.
  
## **Aprendizaje y sus reflexiones**

- Uso de librerías para manejar datos de forma rápida, modelar procesos aleatorios y convertir datos en gráficas claras.  
- Comprensión de decisiones aleatorias que en realidad forman un patrón que muestra regularidad matemática.  
- Importancia de la visualización doble que ayuda a entender los datos numéricos y observar la forma de campana de Gauss de manera más intuitiva.  
- A su vez he aprendido buenas prácticas como dividir el programa en funciones 
- Hacer el código más ordenado.  
- Poder pensar de manera lógica con mayor claridad a través de breves ejercicios
- Una de las cosas que también he aprendido mucho a trabajar es la investigación para poder a través de documentación encontrar que librería me funciona mejor
- También he leído otros códigos, leyendo sus comentarios para aprender a replicar o entender porque el mío no funciona
- Separar claramente la simulación de la visualización.
- He aprendido a descomponer un problema grande, en pasitos chiquitos para poder solucionar en pasos secuenciales
