import heapq
import time


def dijkstra_with_min_heap(graph, V, src):
    """
    Алгоритм Дейкстры для лучшего случая с использованием минимальной кучи (min-heap).
    """
    adj = {i: [] for i in range(V)}
    for u, v, w in graph:
        adj[u].append((v, w))
        adj[v].append((u, w))

    distances = [float('inf')] * V
    distances[src] = 0
    min_heap = [(0, src)]  # (расстояние, вершина)

    while min_heap:
        current_distance, current_vertex = heapq.heappop(min_heap)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in adj[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances


def dijkstra_with_binary_heap(graph, V, src):
    """
    Алгоритм Дейкстры для среднего случая с использованием бинарной кучи.
    """
    adj = {i: [] for i in range(V)}
    for u, v, w in graph:
        adj[u].append((v, w))
        adj[v].append((u, w))

    distances = [float('inf')] * V
    distances[src] = 0
    binary_heap = [(0, src)]  # (расстояние, вершина)

    while binary_heap:
        current_distance, current_vertex = heapq.heappop(binary_heap)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in adj[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(binary_heap, (distance, neighbor))

    return distances


def dijkstra_with_array(graph, V, src):
    """
    Алгоритм Дейкстры для худшего случая с использованием обычного массива.
    """
    adj = {i: [] for i in range(V)}
    for u, v, w in graph:
        adj[u].append((v, w))
        adj[v].append((u, w))

    distances = [float('inf')] * V
    distances[src] = 0
    visited = [False] * V

    for _ in range(V):
        min_distance = float('inf')
        min_vertex = -1

        for v in range(V):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                min_vertex = v

        if min_vertex == -1:
            break

        visited[min_vertex] = True

        for neighbor, weight in adj[min_vertex]:
            if not visited[neighbor]:
                distance = distances[min_vertex] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

    return distances


def read_graph_from_file(filename):
    """
    Считывает граф из файла.
    """
    edges = []
    max_vertex = -1

    with open(filename, "r") as file:
        for line in file:
            u, v, w = map(int, line.split())
            edges.append([u, v, w])
            max_vertex = max(max_vertex, u, v)

    return edges, max_vertex + 1


def write_times_to_file(times, filename):
    """
    Записывает массив времени обработки графов в файл.
    """
    with open(filename, "w", encoding="UTF-8") as file:
        for vertices, time_taken in times:
            file.write(f"{vertices} : {time_taken:.6f} секунд\n")


if __name__ == "__main__":
    # Файлы графов
    graph_files_best = [f"best_case_graph_{i * 1000}_vertices.txt" for i in range(1, 11)]
    graph_files_avg = [f"average_case_graph_{i * 1000}_vertices.txt" for i in range(1, 11)]
    graph_files_worst = [f"worst_case_graph_{i * 1000}_vertices.txt" for i in range(1, 11)]

    source_vertex = 0
    best_case_times = []
    avg_case_times = []
    worst_case_times = []

    # Лучший случай
    print("Обработка графов для лучшего случая...")
    for filename in graph_files_best:
        graph, num_vertices = read_graph_from_file(filename)
        print(f"Обработка графа {filename} с {num_vertices} вершинами...")
        start_time = time.time()
        dijkstra_with_min_heap(graph, num_vertices, source_vertex)
        elapsed_time = time.time() - start_time
        best_case_times.append((num_vertices, elapsed_time))
        print(f"Граф {filename} обработан за {elapsed_time:.6f} секунд.")

    # Средний случай
    print("Обработка графов для среднего случая...")
    for filename in graph_files_avg:
        graph, num_vertices = read_graph_from_file(filename)
        print(f"Обработка графа {filename} с {num_vertices} вершинами...")
        start_time = time.time()
        dijkstra_with_binary_heap(graph, num_vertices, source_vertex)
        elapsed_time = time.time() - start_time
        avg_case_times.append((num_vertices, elapsed_time))
        print(f"Граф {filename} обработан за {elapsed_time:.6f} секунд.")

    # Худший случай
    print("Обработка графов для худшего случая...")
    for filename in graph_files_worst:
        graph, num_vertices = read_graph_from_file(filename)
        print(f"Обработка графа {filename} с {num_vertices} вершинами...")
        start_time = time.time()
        dijkstra_with_array(graph, num_vertices, source_vertex)
        elapsed_time = time.time() - start_time
        worst_case_times.append((num_vertices, elapsed_time))
        print(f"Граф {filename} обработан за {elapsed_time:.6f} секунд.")

    # Сохранение времени обработки
    write_times_to_file(best_case_times, "best_case_times.txt")
    write_times_to_file(avg_case_times, "average_case_times.txt")
    write_times_to_file(worst_case_times, "worst_case_times.txt")

    print("Обработка завершена. Результаты записаны в файлы.")
