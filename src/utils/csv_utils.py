"""Módulo con funciones para leer y escribir archivos CSV."""
import os
import csv
from dotenv import load_dotenv


load_dotenv()


BASE_PATH = os.getenv("BASE_PATH")
SAVE_PATH = os.getenv("SAVE_PATH")
SAVE_STATS = os.getenv("SAVE_STATS")

def read_csv(file_path):
    """Lee una cuadrícula desde un archivo CSV y la devuelve como una lista de listas."""
    grid = []
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            grid.append(list(map(int, row)))
    return grid

def save_to_csv(algorithm_name, path, stats):
    """Guarda la ruta encontrada y las estadísticas en archivos CSV."""
    lab_number = 1

    # Guardar la ruta
    file_name_path = f"{algorithm_name}_laberinto_{lab_number}_path.csv"
    full_save_path = os.path.join(BASE_PATH, SAVE_PATH, file_name_path)

    while os.path.exists(full_save_path):
        lab_number += 1
        file_name_path = f"{algorithm_name}_laberinto_{lab_number}_path.csv"
        full_save_path = os.path.join(BASE_PATH, SAVE_PATH, file_name_path)

    with open(full_save_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Ruta Encontrada"])
        writer.writerow(path)

    # Restablecer el número de laboratorio si es necesario
    lab_number = 1

    # Guardar estadísticas
    file_name_stats = f"{algorithm_name}_laberinto_{lab_number}_stats.csv"
    full_save_stats_path = os.path.join(BASE_PATH, SAVE_STATS, file_name_stats)

    while os.path.exists(full_save_stats_path):
        lab_number += 1
        file_name_stats = f"{algorithm_name}_laberinto_{lab_number}_stats.csv"
        full_save_stats_path = os.path.join(BASE_PATH, SAVE_STATS, file_name_stats)

    with open(full_save_stats_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([f"Resultados y Estadísticas para {algorithm_name}"])
        writer.writerow([])
        writer.writerow(["---- Estadísticas ----"])
        writer.writerow(["Categoría", "Valor"])
        writer.writerow(["Tiempo (s)", stats['time']])
        writer.writerow(["Incremento de memoria (KB)", stats['memory_increment']])
        writer.writerow(["Memoria máxima (KB)", stats['peak_memory']])
