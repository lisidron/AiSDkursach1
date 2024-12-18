import matplotlib.pyplot as plt
import numpy as np

# Параметры для алгоритмов
V_values = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000])  # количество вершин

# Алгоритм Дейкстры
# Худший случай
E_values_worst_dijkstra = V_values**2  # плотный граф
T_values_worst_dijkstra = V_values**2  # O(V²)
# Средний случай
E_values_avg_dijkstra = 3 * V_values  # средняя плотность
T_values_avg_dijkstra = E_values_avg_dijkstra + V_values * np.log2(V_values)  # O(E + V log V)
# Лучший случай
E_values_best_dijkstra = V_values  # разреженный граф
T_values_best_dijkstra = V_values * np.log2(V_values)  # O(V log V)

# Алгоритм Форда-Беллмана
# Худший случай
E_values_worst_ford = V_values**2  # плотный граф
T_values_worst_ford = V_values**3  # O(V³)
# Средний случай
E_values_avg_ford = 3 * V_values  # средняя плотность
T_values_avg_ford = V_values * E_values_avg_ford  # O(V × E)
# Лучший случай
E_values_best_ford = V_values  # разреженный граф
T_values_best_ford = V_values * E_values_best_ford  # O(V × E)

# Цвета
colors = {
    "worst_dijkstra": "green",
    "avg_dijkstra": "blue",
    "best_dijkstra": "red",
    "worst_ford": "orange",
    "avg_ford": "magenta",
    "best_ford": "cyan",
}

# Построение отдельных графиков
# 1. Худший случай
plt.figure(figsize=(10, 6))
plt.plot(V_values, T_values_worst_dijkstra, color=colors["worst_dijkstra"], label='Худший случай Дейкстры: O(V²)')
plt.scatter(V_values, T_values_worst_dijkstra, color=colors["worst_dijkstra"])
plt.plot(V_values, T_values_worst_ford, linestyle='--', color=colors["worst_ford"], label='Худший случай Форда-Беллмана: O(V³)')
plt.scatter(V_values, T_values_worst_ford, color=colors["worst_ford"])
plt.xlabel('Количество вершин, V')
plt.ylabel('Временная сложность, T(V)')
plt.title('Худший случай: сравнение алгоритмов Дейкстры и Форда-Беллмана')
plt.legend()
plt.grid(True)
plt.savefig('Графики/comparison_worst_case.png')
plt.close()

# 2. Средний случай
plt.figure(figsize=(10, 6))
plt.plot(V_values, T_values_avg_dijkstra, color=colors["avg_dijkstra"], label='Средний случай Дейкстры: O(E + V log V)')
plt.scatter(V_values, T_values_avg_dijkstra, color=colors["avg_dijkstra"])
plt.plot(V_values, T_values_avg_ford, linestyle='--', color=colors["avg_ford"], label='Средний случай Форда-Беллмана: O(V × E)')
plt.scatter(V_values, T_values_avg_ford, color=colors["avg_ford"])
plt.xlabel('Количество вершин, V')
plt.ylabel('Временная сложность, T(V)')
plt.title('Средний случай: сравнение алгоритмов Дейкстры и Форда-Беллмана')
plt.legend()
plt.grid(True)
plt.savefig('Графики/comparison_avg_case.png')
plt.close()

# 3. Лучший случай
plt.figure(figsize=(10, 6))
plt.plot(V_values, T_values_best_dijkstra, color=colors["best_dijkstra"], label='Лучший случай Дейкстры: O(V log V)')
plt.scatter(V_values, T_values_best_dijkstra, color=colors["best_dijkstra"])
plt.plot(V_values, T_values_best_ford, linestyle='--', color=colors["best_ford"], label='Лучший случай Форда-Беллмана: O(V × E)')
plt.scatter(V_values, T_values_best_ford, color=colors["best_ford"])
plt.xlabel('Количество вершин, V')
plt.ylabel('Временная сложность, T(V)')
plt.title('Лучший случай: сравнение алгоритмов Дейкстры и Форда-Беллмана')
plt.legend()
plt.grid(True)
plt.savefig('Графики/comparison_best_case.png')
plt.close()

# Построение сводного графика
plt.figure(figsize=(12, 8))
plt.plot(V_values, T_values_worst_dijkstra, color=colors["worst_dijkstra"], label='Худший случай Дейкстры')
plt.scatter(V_values, T_values_worst_dijkstra, color=colors["worst_dijkstra"])
plt.plot(V_values, T_values_avg_dijkstra, color=colors["avg_dijkstra"], label='Средний случай Дейкстры')
plt.scatter(V_values, T_values_avg_dijkstra, color=colors["avg_dijkstra"])
plt.plot(V_values, T_values_best_dijkstra, color=colors["best_dijkstra"], label='Лучший случай Дейкстры')
plt.scatter(V_values, T_values_best_dijkstra, color=colors["best_dijkstra"])

plt.plot(V_values, T_values_worst_ford, linestyle='--', color=colors["worst_ford"], label='Худший случай Форда-Беллмана')
plt.scatter(V_values, T_values_worst_ford, color=colors["worst_ford"])
plt.plot(V_values, T_values_avg_ford, linestyle='--', color=colors["avg_ford"], label='Средний случай Форда-Беллмана')
plt.scatter(V_values, T_values_avg_ford, color=colors["avg_ford"])
plt.plot(V_values, T_values_best_ford, linestyle='--', color=colors["best_ford"], label='Лучший случай Форда-Беллмана')
plt.scatter(V_values, T_values_best_ford, color=colors["best_ford"])

plt.xlabel('Количество вершин, V')
plt.ylabel('Временная сложность, T(V)')
plt.title('Сводный график: сравнение алгоритмов Дейкстры и Форда-Беллмана')
plt.legend()
plt.grid(True)
plt.savefig('Графики/summary_comparison.png')
plt.close()
