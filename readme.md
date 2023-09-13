# Programa de Ruta Más Corta

## Descripción

Este proyecto consiste en una aplicación de escritorio desarrollada en Python que utiliza diferentes algoritmos para encontrar la ruta más corta en un laberinto. El laberinto y las rutas son leídos y guardados en archivos CSV.

## 🛠 Requisitos

- Python 3.x
- Bibliotecas adicionales: tkinter, glob, csv

## 🚀 Instalación

1. **Clona el repositorio:**
    ```bash
    git clone https://github.com/sebastins18/shortest_path_algorithm.git
    ```

2. **Cambia al directorio del proyecto:**
    ```bash
    cd ruta-del-proyecto
    ```

3. **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Crea un archivo `.env` en la raíz del proyecto y añade las siguientes variables de entorno:**
    ```env
    BASE_PATH=Tu_Ruta_Base
    SAVE_PATH_1=docs/
    SAVE_PATH=docs/paths/
    SAVE_STATS=docs/stats/
    DATA_PATH=data/
    ```

5. **Ejecuta el programa principal:**
    ```bash
    python main.py
    ```

## 🎨 Características

- Utiliza diferentes algoritmos de búsqueda, incluyendo Dijkstra, Bellman-Ford, DFS, BFS y A*.
- Opción para visualizar el laberinto y la ruta más corta en una interfaz gráfica de usuario.
- Genera estadísticas de rendimiento como tiempo de ejecución y uso de memoria.

## 📝 Uso

1. Al abrir la aplicación, selecciona un archivo CSV que contenga el laberinto.
2. Escoge un algoritmo de búsqueda en la lista desplegable.
3. Haz clic en "Pintar" para visualizar el laberinto.
4. Haz clic en "Ejecutar" para encontrar la ruta más corta.
5. La ruta y las estadísticas se guardarán en archivos CSV separados.

## 🤝 Integrantes

1. Sebastián Long Segura Méndez
2. Mauren Miranda Quesada

## 📊 Análisis y Conclusiones

Este proyecto también sirve como una herramienta de análisis para comparar el rendimiento de diferentes algoritmos de búsqueda de rutas en términos de velocidad y consumo de memoria. Al ejecutar cada algoritmo en varios laberintos, podrás sacar conclusiones sobre:

### ¿Qué algoritmo es más veloz en obtener la mejor ruta?

En laberintos de 200x200 la velocidad de DepthFirstSearch supera por mucho los demas algoritmos. Con la ultima prueba el resultado fue de 0.006 segundos, seguido del algoritmo
BreadthFirstSearch con 0.1028 segundos y el tercero AStar con 0.1503 segundos


### ¿Qué algoritmo consume más memoria?

En labarientos de 200x200 el algoritmo de Dijkstra fue el que mas consumio memoria con 8328 KB, seguido del algoritmo BellmanFord con 6838 KB y por ultimo el algoritmo A Star con 5836 KB

Los resultados serán almacenados en archivos CSV separados, lo que facilita su posterior análisis y comparación.
