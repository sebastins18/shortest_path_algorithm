import os
import glob
import tkinter as tk
from tkinter import ttk, messagebox
from algorithms.dijkstra import Dijkstra
from algorithms.BellmanFord import BellmanFord
from algorithms.DepthFirstSearch import DepthFirstSearch
from algorithms.BreadthFirstSearch import BreadthFirstSearch
from algorithms.AStarSearch import AStarSearch
from utils.statistics import PerformanceMeasurer
from utils.utils import draw_grid, find_start_end, visualize_route
from utils.csv_utils import save_to_csv, read_csv
from dotenv import load_dotenv
load_dotenv()

BASE_PATH = os.getenv("BASE_PATH")
SAVE_PATH = os.getenv("SAVE_PATH_1")
FILE_PATH = os.path.join(BASE_PATH, os.getenv("DATA_PATH"))

ALGORITHMS = {
    'Dijkstra': Dijkstra,
    'Bellman-Ford': BellmanFord,
    'DFS': DepthFirstSearch,
    'BFS': BreadthFirstSearch,
    'ASearch': AStarSearch
}

def load_csv_files():
    try:
        return glob.glob(os.path.join(FILE_PATH, '*.csv'))
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while loading CSV files: {e}")
        return []

def update_stats_labels(time_label, memory_increment_label, peak_memory_label, stats):
    time_label["text"] = f"Tiempo: {stats['time']}"
    memory_increment_label["text"] = f"Incremento de memoria: {stats['memory_increment']}"
    peak_memory_label["text"] = f"Pico de memoria: {stats['peak_memory']}"

def run_selected_algorithm(selected_algo, filepath, canvas, update_stats_fn):
    grid = read_csv(filepath)
    start, end = find_start_end(grid)
    algorithm = ALGORITHMS.get(selected_algo)()

    if algorithm:
        measurer = PerformanceMeasurer()
        path, stats = measurer.measure(algorithm, "find_shortest_path", grid, start, end)
        if path is None: 
            messagebox.showwarning('Advertencia', 'No se encontró un camino válido.')
            return        
        draw_grid(grid, canvas)
        visualize_route(grid, path, 4, canvas)
        print("datos:", stats)
        save_to_csv(selected_algo, path, stats)
        update_stats_fn(stats) 

def create_csv_combo(frame, csv_files):
    csv_combo = ttk.Combobox(frame, values=csv_files)
    csv_combo.grid(row=0, column=0, sticky=tk.EW)
    return csv_combo

def create_buttons(frame, on_paint, on_run, on_clear):
    paint_button = ttk.Button(frame, text="Pintar", command=on_paint)
    paint_button.grid(row=0, column=1, sticky=tk.EW)

    run_button = ttk.Button(frame, text="Ejecutar", command=on_run)
    run_button.grid(row=0, column=3, sticky=tk.EW)

    clear_button = ttk.Button(frame, text="Limpiar", command=on_clear)
    clear_button.grid(row=1, column=0, columnspan=4, sticky=tk.EW) 
    
    return run_button  

def create_algorithm_combo(frame, algorithm_names):
    algo_combo = ttk.Combobox(frame, values=algorithm_names)
    algo_combo.grid(row=0, column=2, sticky=tk.EW)
    return algo_combo

def main():
    laberinto_pintado = False 

    root = tk.Tk()
    root.geometry("800x600")
    root.title("Programa de Ruta Más Corta")

    root.grid_rowconfigure(0, weight=1)  
    root.grid_rowconfigure(1, weight=9)  
    root.grid_columnconfigure(0, weight=1)

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    stats_label = ttk.Label(frame, text="Estadísticas:")
    stats_label.grid(row=1, column=0, sticky=tk.W)

    time_label = ttk.Label(frame, text="Tiempo: N/A")
    time_label.grid(row=2, column=0, sticky=tk.W)

    memory_increment_label = ttk.Label(frame, text="Incremento de memoria: N/A")
    memory_increment_label.grid(row=3, column=0, sticky=tk.W)

    peak_memory_label = ttk.Label(frame, text="Pico de memoria: N/A")
    peak_memory_label.grid(row=4, column=0, sticky=tk.W)

    csv_files = load_csv_files()
    algorithm_names = list(ALGORITHMS.keys())
    
    csv_combo = create_csv_combo(frame, [os.path.basename(f) for f in csv_files])
    algorithm_combo = create_algorithm_combo(frame, algorithm_names)
    
    run_button = create_buttons(
        frame,
        on_paint=lambda: on_paint(),
        on_run=lambda: on_run(),
        on_clear=lambda: on_clear()
    )

    canvas = tk.Canvas(root, bg="white")
    canvas.grid(row=1, column=0, sticky="nsew")

    def on_run():
        nonlocal laberinto_pintado
        if not laberinto_pintado:
            messagebox.showwarning('Advertencia', 'Primero pinta el laberinto.')
            return
        selected_algo = algorithm_combo.get()
        selected_csv = csv_combo.get()
        if not selected_algo or not selected_csv:
            messagebox.showwarning('Advertencia', 'Por favor, selecciona un algoritmo y un archivo CSV.')
            return
        run_selected_algorithm(
            selected_algo,
            os.path.join(FILE_PATH, selected_csv),
            canvas,
            lambda stats: update_stats_labels(time_label, memory_increment_label, peak_memory_label, stats)
        )

    def on_paint():
        nonlocal laberinto_pintado
        selected_csv = csv_combo.get()
        if not selected_csv:
            messagebox.showwarning('Advertencia', 'Por favor, selecciona un archivo CSV.')
            return
        grid = read_csv(os.path.join(FILE_PATH, selected_csv))
        draw_grid(grid, canvas)
        laberinto_pintado = True 

    def on_clear():
        nonlocal laberinto_pintado
        canvas.delete("all")
        laberinto_pintado = False 
        time_label["text"] = "Tiempo: N/A"
        memory_increment_label["text"] = "Incremento de memoria: N/A"
        peak_memory_label["text"] = "Pico de memoria: N/A"

    def update_run_button_status():
        nonlocal laberinto_pintado
        run_button['state'] = 'normal' if laberinto_pintado else 'disabled'
        run_button.after(100, update_run_button_status)

    update_run_button_status()

    root.mainloop()

if __name__ == "__main__":
    main()