class DepthFirstSearch:
    """Clase para implementar el algoritmo de búsqueda en profundidad (DFS)."""

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
        return self.dfs(grid, start, end)

    def dfs(self, grid, current, end):
        """Realiza la búsqueda en profundidad."""
        if current == end:
            return self.reconstruct_path(current)

        self.visited.add(current)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dx, dy in directions:
            x, y = current[0] + dx, current[1] + dy
            if 0 <= x < self.rows and 0 <= y < self.cols:
                neighbor = (x, y)
                if neighbor in self.visited or grid[x][y] == 1:
                    continue
                self.prev[neighbor] = current
                path = self.dfs(grid, neighbor, end)
                if path:
                    return path

        return None

    def reconstruct_path(self, current):
        """Reconstruye la ruta."""
        path = []
        while current is not None:
            path.append(current)
            current = self.prev.get(current, None)
        return path[::-1]
