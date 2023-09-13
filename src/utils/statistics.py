import time
import tracemalloc
import psutil


class PerformanceMeasurer:
    def __init__(self):
        self.initial_memory = None
        self.final_memory = None
        self.start_time = None
        self.end_time = None
        self.memory_increment = None
        self.peak_memory = None
        self.elapsed_time = None

    def start(self):
        tracemalloc.start()
        self.initial_memory = psutil.Process().memory_info().rss / 1024  
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()
        self.final_memory = psutil.Process().memory_info().rss / 1024  
        self.memory_increment = self.final_memory - self.initial_memory 
        self.elapsed_time = self.end_time - self.start_time
        current, self.peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

    def measure(self, algorithm, method_name, maze, start, end):
        self.start()
        path = getattr(algorithm, method_name)(maze, start, end)
        self.stop()

        results = {
            'time': self.elapsed_time,
            'memory_increment': self.memory_increment,
            'peak_memory': self.peak_memory / 1024 
        }

        return path, results
