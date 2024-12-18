import random


def generate_sparse_graph(n, max_weight):
    """
    Генерирует разреженный связный граф (лучший случай), где каждая вершина имеет 1-3 инцидентных ребра.
    """
    edges = []
    connected = set()

    # Создаем минимальный остов для связности
    for i in range(1, n):
        u = i - 1
        v = i
        w = random.randint(1, max_weight)
        edges.append([u, v, w])
        connected.add((u, v))
        connected.add((v, u))

    # Добавляем дополнительные ребра
    for u in range(n):
        num_edges = random.randint(1, 3)
        count = 0

        while count < num_edges:
            v = random.randint(0, n - 1)
            if u != v and (u, v) not in connected and (v, u) not in connected:
                w = random.randint(1, max_weight)
                edges.append([u, v, w])
                connected.add((u, v))
                connected.add((v, u))
                count += 1

    return edges


def generate_medium_density_graph(n, max_weight):
    """
    Генерирует граф средней плотности (средний случай), где каждая вершина имеет 4-7 инцидентных ребер.
    """
    edges = []
    connected = set()

    # Создаем минимальный остов для связности
    for i in range(1, n):
        u = i - 1
        v = i
        w = random.randint(1, max_weight)
        edges.append([u, v, w])
        connected.add((u, v))
        connected.add((v, u))

    # Добавляем дополнительные ребра
    for u in range(n):
        num_edges = random.randint(4, 7)
        count = 0

        while count < num_edges:
            v = random.randint(0, n - 1)
            if u != v and (u, v) not in connected and (v, u) not in connected:
                w = random.randint(1, max_weight)
                edges.append([u, v, w])
                connected.add((u, v))
                connected.add((v, u))
                count += 1

    return edges


def generate_dense_graph(n, max_weight):
    """
    Генерирует плотный граф (худший случай), где каждая вершина имеет 2-10 инцидентных ребер.
    """
    edges = []
    connected = set()

    # Создаем минимальный остов для связности
    for i in range(1, n):
        u = i - 1
        v = i
        w = random.randint(1, max_weight)
        edges.append([u, v, w])
        connected.add((u, v))
        connected.add((v, u))

    # Добавляем дополнительные ребра
    for u in range(n):
        num_edges = random.randint(2, 10)
        count = 0

        while count < num_edges:
            v = random.randint(0, n - 1)
            if u != v and (u, v) not in connected and (v, u) not in connected:
                w = random.randint(1, max_weight)
                edges.append([u, v, w])
                connected.add((u, v))
                connected.add((v, u))
                count += 1

    return edges


def write_graph_to_file(graph, filename):
    """
    Записывает граф в файл.
    """
    with open(filename, "w") as file:
        for edge in graph:
            file.write(f"{edge[0]} {edge[1]} {edge[2]}\n")


if __name__ == "__main__":
    # Параметры генерации
    max_weight = 1000  # Максимальный вес ребра
    vertex_counts = range(1000, 11000, 1000)  # Количество вершин от 1000 до 10000 с шагом 1000

    # Генерация графов
    for n in vertex_counts:
        # Разреженные графы
        sparse_graph = generate_sparse_graph(n, max_weight)
        sparse_filename = f"best_case_graph_{n}_vertices.txt"
        write_graph_to_file(sparse_graph, sparse_filename)
        print(f"Разреженный граф с {n} вершинами сохранен в файл {sparse_filename}.")

        # Графы средней плотности
        medium_density_graph = generate_medium_density_graph(n, max_weight)
        medium_density_filename = f"average_case_graph_{n}_vertices.txt"
        write_graph_to_file(medium_density_graph, medium_density_filename)
        print(f"Граф средней плотности с {n} вершинами сохранен в файл {medium_density_filename}.")

        # Плотные графы
        dense_graph = generate_dense_graph(n, max_weight)
        dense_filename = f"worst_case_graph_{n}_vertices.txt"
        write_graph_to_file(dense_graph, dense_filename)
        print(f"Плотный граф с {n} вершинами сохранен в файл {dense_filename}.")

    print("Генерация всех графов завершена.")
