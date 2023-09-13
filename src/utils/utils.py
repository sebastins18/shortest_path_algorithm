"""
Este módulo contiene utilidades para
visualizarla y encontrar el inicio y el final en la cuadrícula.
"""

from collections import defaultdict
from tkinter import Canvas

def find_start_end(grid):
    """Encuentra y devuelve las coordenadas de inicio y fin en la cuadrícula."""
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 2:
                start = (i, j)
            elif cell == 3:
                end = (i, j)
    return start, end

color_map_tkinter = {
    0: 'white',   # Espacio vacío en la cuadrícula
    1: 'black',   # Obstáculo o muro en la cuadrícula
    2: 'green',   # Punto de inicio
    3: 'red',     # Punto final o destino
    4: 'blue',    # Alguna otra característica especial (por definir)
    5: 'yellow',  # Parte de la ruta encontrada
    6: 'magenta', # Otro tipo de punto de interés (por definir)
    7: 'cyan',    # Otro tipo de punto de interés (por definir)
    8: 'grey'     # Tal vez usado para celdas visitadas pero no parte de la ruta
}

def visualize_route(grid, path, route_value, canvas):
    rows, cols = len(grid), len(grid[0])
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    cell_width = canvas_width / cols
    cell_height = canvas_height / rows


    for i in range(rows):
        for j in range(cols):
            color = color_map_tkinter.get(grid[i][j], 'gray')
            x1, y1 = j * cell_width, i * cell_height
            x2, y2 = x1 + cell_width, y1 + cell_height
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
    

    for (x, y) in path:
        x1, y1 = y * cell_width + 1, x * cell_height + 1  
        x2, y2 = x1 + cell_width - 2, y1 + cell_height - 2 
        canvas.create_rectangle(x1, y1, x2, y2, fill=color_map_tkinter.get(route_value), outline="black")


    for i in range(rows):
        for j in range(cols):
            if grid[i][j] in [2, 3]:
                x1, y1 = j * cell_width, i * cell_height
                x2, y2 = x1 + cell_width, y1 + cell_height
                canvas.create_rectangle(x1, y1, x2, y2, fill=color_map_tkinter.get(grid[i][j]), outline="black")

def draw_grid(grid, canvas):
    rows, cols = len(grid), len(grid[0])
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    cell_width = canvas_width / cols
    cell_height = canvas_height / rows

    for i in range(rows):
        for j in range(cols):
            color = color_map_tkinter.get(grid[i][j], 'gray')
            x1, y1 = j * cell_width, i * cell_height
            x2, y2 = x1 + cell_width, y1 + cell_height
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
