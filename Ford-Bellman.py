from sys import maxsize
import time


def bellman_ford_optimized(graph, V, E, src):
    """
    Алгоритм Беллмана-Форда для лучшего случая (с оптимизацией раннего выхода).
    """
    dis = [maxsize] * V
    dis[src] = 0

    for i in range(V - 1):
        changed = False
        for u, v, w in graph:
            if dis[u] != maxsize and dis[u] + w < dis[v]:
                dis[v] = dis[u] + w
                changed = True
        if not changed:  # Если на этой итерации не было изменений, можно выйти раньше
            break

    # Проверка на циклы с отрицательным весом
    for u, v, w in graph:
        if dis[u] != maxsize and dis[u] + w < dis[v]:
            raise ValueError("Граф содержит цикл с отрицательным весом")

    return dis


def bellman_ford_standard(graph, V, E, src):
    """
    Алгоритм Беллмана-Форда для среднего случая (стандартный алгоритм).
    """
    dis = [maxsize] * V
    dis[src] = 0

    for _ in range(V - 1):
        for u, v, w in graph:
            if dis[u] != maxsize and dis[u] + w < dis[v]:
                dis[v] = dis[u] + w

    # Проверка на циклы с отрицательным весом
    for u, v, w in graph:
        if dis[u] != maxsize and dis[u] + w < dis[v]:
            raise ValueError("Граф содержит цикл с отрицательным весом")

    return dis


def bellman_ford_unoptimized(graph, V, E, src):
    """
    Алгоритм Беллмана-Форда для худшего случая (неоптимизированный с избыточными проверками).
    """
    dis = [maxsize] * V
    dis[src] = 0

    for i in range(V - 1):
        for u, v, w in graph:
            if dis[u] != maxsize:
                if dis[u] + w < dis[v]:  # Избыточная проверка
                    dis[v] = dis[u] + w

    # Проверка на циклы с отрицательным весом
    for u, v, w in graph:
        if dis[u] != maxsize and dis[u] + w < dis[v]:
            raise ValueError("Граф содержит цикл с отрицательным весом")

    return dis


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
        bellman_ford_optimized(graph, num_vertices, len(graph), source_vertex)
        elapsed_time = time.time() - start_time
        best_case_times.append((num_vertices, elapsed_time))
        print(f"Граф {filename} обработан за {elapsed_time:.6f} секунд.")

    # Средний случай
    print("Обработка графов для среднего случая...")
    for filename in graph_files_avg:
        graph, num_vertices = read_graph_from_file(filename)
        print(f"Обработка графа {filename} с {num_vertices} вершинами...")
        start_time = time.time()
        bellman_ford_standard(graph, num_vertices, len(graph), source_vertex)
        elapsed_time = time.time() - start_time
        avg_case_times.append((num_vertices, elapsed_time))
        print(f"Граф {filename} обработан за {elapsed_time:.6f} секунд.")

    # Худший случай
    print("Обработка графов для худшего случая...")
    for filename in graph_files_worst:
        graph, num_vertices = read_graph_from_file(filename)
        print(f"Обработка графа {filename} с {num_vertices} вершинами...")
        start_time = time.time()
        bellman_ford_unoptimized(graph, num_vertices, len(graph), source_vertex)
        elapsed_time = time.time() - start_time
        worst_case_times.append((num_vertices, elapsed_time))
        print(f"Граф {filename} обработан за {elapsed_time:.6f} секунд.")

    # Сохранение времени обработки
    write_times_to_file(best_case_times, "best_case_times_bellman_ford.txt")
    write_times_to_file(avg_case_times, "average_case_times_bellman_ford.txt")
    write_times_to_file(worst_case_times, "worst_case_times_bellman_ford.txt")

    print("Обработка завершена. Результаты записаны в файлы.")
