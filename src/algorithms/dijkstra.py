"""
Este módulo implementa el algoritmo de Dijkstra para encontrar el
camino más corto en una cuadrícula.
"""

import heapq

class Dijkstra:
    """Clase para implementar el algoritmo de Dijkstra."""

    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.distance = {}
        self.priority_queue = []
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.prev = {}

    def initialize(self, grid, start):
        """Inicializa las variables necesarias."""
        self.rows, self.cols = len(grid), len(grid[0])
        self.distance = {(i, j): float('inf') for i in range(self.rows) for j in range(self.cols)}
        self.distance[start] = 0
        self.priority_queue = [(0, start)]
        self.prev = {start: None}

    def find_shortest_path(self, grid, start, end):
        """Encuentra el camino más corto en una cuadrícula entre un punto de inicio y 
        un punto final."""
        self.initialize(grid, start)

        while self.priority_queue:
            dist, current = heapq.heappop(self.priority_queue)
            if current == end:
                return self.reconstruct_path(current)

            self.update_neighbors(grid, current, dist)

        return None

    def update_neighbors(self, grid, current, dist):
        """Actualiza las distancias de los vecinos del nodo actual."""
        for delta_x, delta_y in self.directions:
            new_x, new_y = current[0] + delta_x, current[1] + delta_y
            if 0 <= new_x < self.rows and 0 <= new_y < self.cols:
                if grid[new_x][new_y] == 1:
                    continue
                new_distance = dist + 1
                if new_distance < self.distance[(new_x, new_y)]:
                    self.distance[(new_x, new_y)] = new_distance
                    heapq.heappush(self.priority_queue, (new_distance, (new_x, new_y)))
                    self.prev[(new_x, new_y)] = current

    def reconstruct_path(self, current):
        """Reconstruye el camino más corto."""
        path = []
        while current is not None:
            path.append(current)
            current = self.prev[current]
        return path[::-1]
