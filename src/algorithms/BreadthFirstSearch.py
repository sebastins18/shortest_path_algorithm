from collections import deque

class BreadthFirstSearch:
    """Clase para implementar el algoritmo de búsqueda en anchura (BFS)."""

    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.visited = set()
        self.prev = {}

    def initialize(self, grid):
        """Inicializa las variables necesarias."""
        self.rows, self.cols = len(grid), len(grid[0])
        self.visited = set()
        self.prev = {}

    def find_shortest_path(self, grid, start, end):
        """Encuentra una ruta en una cuadrícula entre un punto de inicio y un punto final."""
        self.initialize(grid)
        return self.bfs(grid, start, end)

    def bfs(self, grid, start, end):
        """Realiza la búsqueda en anchura."""
        queue = deque([start])
        self.visited.add(start)
        self.prev[start] = None

        while queue:
            current = queue.popleft()
            if current == end:
                return self.reconstruct_path(current)

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dx, dy in directions:
                x, y = current[0] + dx, current[1] + dy
                if 0 <= x < self.rows and 0 <= y < self.cols:
                    neighbor = (x, y)
                    if neighbor in self.visited or grid[x][y] == 1:
                        continue
                    queue.append(neighbor)
                    self.visited.add(neighbor)
                    self.prev[neighbor] = current

        return None

    def reconstruct_path(self, current):
        """Reconstruye la ruta."""
        path = []
        while current is not None:
            path.append(current)
            current = self.prev.get(current, None)
        return path[::-1]
