import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp

# Функция для чтения графа из файла
def read_graph_from_file(filename):
    G = nx.Graph()
    with open(filename, 'r') as file:
        for line in file:
            u, v, weight = map(int, line.split())
            G.add_edge(u, v, weight=weight)
    return G

# Визуализация графа
def draw_graph(G):
    pos = nx.spring_layout(G)  # Расположение узлов
    weights = nx.get_edge_attributes(G, 'weight')

    # Отрисовка
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights, font_size=8)
    plt.title("Граф из файла")
    plt.show()

# Основная часть программы
if __name__ == "__main__":
    filename = "graph_121_vertices.txt"  # Имя файла с графом
    graph = read_graph_from_file(filename)  # Считываем граф
    draw_graph(graph)  # Отрисовываем граф
