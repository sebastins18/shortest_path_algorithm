class BellmanFord:
    """Clase para implementar el algoritmo de Bellman-Ford."""

    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.distance = {}
        self.prev = {}

    def initialize(self, grid, start):
        """Inicializa las variables necesarias."""
        self.rows, self.cols = len(grid), len(grid[0])
        self.distance = {(i, j): float('inf') for i in range(self.rows) for j in range(self.cols)}
        self.distance[start] = 0
        self.prev = {start: None}

    def find_shortest_path(self, grid, start, end):
        """Encuentra el camino más corto en una cuadrícula entre un punto de inicio y un punto final."""
        self.initialize(grid, start)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        no_update = False  # A flag for early exit

        for _ in range(self.rows * self.cols - 1):
            no_update = True
            for i in range(self.rows):
                for j in range(self.cols):
                    current = (i, j)
                    if self.distance[current] == float('inf'):
                        continue
                    for dx, dy in directions:
                        x, y = i + dx, j + dy
                        if 0 <= x < self.rows and 0 <= y < self.cols:
                            neighbor = (x, y)
                            if grid[x][y] == 1:
                                continue
                            new_distance = self.distance[current] + 1
                            if new_distance < self.distance[neighbor]:
                                self.distance[neighbor] = new_distance
                                self.prev[neighbor] = current
                                no_update = False  # A distance was updated

            if no_update:
                break

        if self.distance[end] == float('inf'):
            return None

        return self.reconstruct_path(end)

    def reconstruct_path(self, end):
        """Reconstruye el camino más corto."""
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = self.prev.get(current, None)
        return path[::-1] if path[0] == end else None
