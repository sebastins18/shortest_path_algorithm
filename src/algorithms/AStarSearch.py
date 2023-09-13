import heapq

class AStarSearch:
    """Clase para implementar el algoritmo de búsqueda A*."""

    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.distance = {}
        self.priority_queue = []
        self.prev = {}

    def initialize(self, grid, start):
        """Inicializa las variables necesarias."""
        self.rows, self.cols = len(grid), len(grid[0])
        self.distance = {(i, j): float('inf') for i in range(self.rows) for j in range(self.cols)}
        self.distance[start] = 0
        self.priority_queue = [(0, start)]
        self.prev = {start: None}

    def heuristic(self, current, end):
        """Función heurística: distancia de Manhattan."""
        return abs(current[0] - end[0]) + abs(current[1] - end[1])

    def find_shortest_path(self, grid, start, end):
        """Encuentra una ruta en una cuadrícula entre un punto de inicio y un punto final."""
        self.initialize(grid, start)

        while self.priority_queue:
            _, current = heapq.heappop(self.priority_queue)
            if current == end:
                return self.reconstruct_path(current)

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dx, dy in directions:
                x, y = current[0] + dx, current[1] + dy
                if 0 <= x < self.rows and 0 <= y < self.cols:
                    if grid[x][y] == 1:
                        continue
                    neighbor = (x, y)
                    tentative_distance = self.distance[current] + 1
                    if tentative_distance < self.distance[neighbor]:
                        self.distance[neighbor] = tentative_distance
                        f_value = tentative_distance + self.heuristic(neighbor, end)
                        heapq.heappush(self.priority_queue, (f_value, neighbor))
                        self.prev[neighbor] = current

        return None

    def reconstruct_path(self, current):
        """Reconstruye la ruta."""
        path = []
        while current is not None:
            path.append(current)
            current = self.prev.get(current, None)
        return path[::-1]
