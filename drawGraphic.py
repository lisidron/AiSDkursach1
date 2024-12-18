import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

def multiPlotCreate(allData, regression, labels, title, printPolynoms, filenameAdd=""):

    if not isinstance(allData, list):
        allData = [allData]

    if not isinstance(labels, list):
        labels = [labels]

    colors = ['blue', 'green', 'red', 'gray', 'olive', 'cyan']
    i = 0

    if regression:
        for data in allData:
            points = np.array(data)
            x = points[:, 0]
            y = points[:, 1]

            # Линейная регрессия
            slope_linear, intercept_linear, r_value_linear, _, _ = stats.linregress(x, y)
            y_pred_linear = intercept_linear + slope_linear * x
            r_squared_linear = r_value_linear ** 2

            # Логарифмическая регрессия
            x_log2 = np.log2(x)
            slope_log, intercept_log, r_value_log, _, _ = stats.linregress(x_log2, y)
            y_pred_log = intercept_log + slope_log * np.log2(x)
            r_squared_log = r_value_log ** 2

            # Квадратичная регрессия
            coeffs_quad = np.polyfit(x, y, 2)
            y_pred_quad = coeffs_quad[0] * x**2 + coeffs_quad[1] * x + coeffs_quad[2]
            ss_total = np.sum((y - np.mean(y))**2)
            ss_residual_quad = np.sum((y - y_pred_quad)**2)
            r_squared_quad = 1 - (ss_residual_quad / ss_total)

            # Линейно-логарифмическая регрессия
            log_y = np.log(y)
            slope_loglin, intercept_loglin, r_value_loglin, _, _ = stats.linregress(x, log_y)
            y_pred_loglin = np.exp(intercept_loglin + slope_loglin * x)
            ss_residual_loglin = np.sum((y - y_pred_loglin) ** 2)
            r_squared_loglin = 1 - (ss_residual_loglin / ss_total)

            # Выбор лучшей модели
            models = [
                ("Линейная регрессия", r_squared_linear, y_pred_linear, f"y = {intercept_linear:.3f} + {slope_linear:.3f}x"),
                ("Логарифмическая регрессия", r_squared_log, y_pred_log, f"y = {intercept_log:.3f} + {slope_log:.3f}*log2(x)"),
                ("Квадратичная регрессия", r_squared_quad, y_pred_quad,
                 f"y = {coeffs_quad[0]:.3f}x^2 + {coeffs_quad[1]:.3f}x + {coeffs_quad[2]:.3f}"),
                ("Линейно-логарифмическая регрессия", r_squared_loglin, y_pred_loglin,
                 f"y = exp({intercept_loglin:.3f} + {slope_loglin:.3f}x)")
            ]
            best_model, best_r_squared, best_y_pred, best_model_eq = max(models, key=lambda x: x[1])

            # Построение графика лучшей регрессии
            if best_model == "Линейная регрессия" or best_model == "Логарифмическая регрессия":
                plt.plot(x, best_y_pred, color=colors[i], label=f"{labels[i]} ", zorder=10)
            elif best_model == "Квадратичная регрессия":
                x_dense = np.linspace(min(x), max(x), 1000)
                y_dense = coeffs_quad[0] * x_dense**2 + coeffs_quad[1] * x_dense + coeffs_quad[2]
                plt.plot(x_dense, y_dense, color=colors[i], label=f"{labels[i]} ", zorder=10)
            elif best_model == "Линейно-логарифмическая регрессия":
                x_dense = np.linspace(min(x), max(x), 1000)
                y_dense = np.exp(intercept_loglin + slope_loglin * x_dense)
                plt.plot(x_dense, y_dense, color=colors[i], label=f"{labels[i]} ", zorder=10)

            # Печать уравнения регрессии
            if printPolynoms:
                print(f"{title} {labels[i]}: {best_model_eq}")

            i += 1

    else:
        for data in allData:
            points = np.array(data)
            x = points[:, 0]
            y = points[:, 1]
            plt.scatter(x, y, color=colors[i], label=labels[i], zorder=5)
            i += 1

    plt.xlabel('Количество вершин, E')
    plt.ylabel('Время нахождения кратчайшего пути, n')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.savefig("Графики/" + filenameAdd + " " + title.replace(".", "_") + ("Регрессия" if regression else "") + ".png")
    plt.close()


def readDatas(files):
    # Преобразуем в список, если передан одиночный файл
    if not isinstance(files, list):
        files = [files]
    data_prac = []

    for file in files:
        with open(file, encoding="UTF-8") as f:
            lines = f.read().strip().split("\n")
            array_2d = []
            for line in lines:
                parts = line.replace("", "").replace("секунд", "").split(":")
                graph_number = int(parts[0].strip())
                time_in_seconds = float(parts[1].strip())
                array_2d.append([graph_number, time_in_seconds])
            data_prac.append(array_2d)
    return data_prac

#
dots = readDatas(["best_case_times.txt", "average_case_times.txt", "worst_case_times.txt"])
multiPlotCreate(dots, False, ["Лучший случай", "Средний случай", "Худший случай"], "Алгоритм Дейкстры", True,  "combined_practic")
dots = readDatas(["best_case_times_bellman_ford.txt", "average_case_times_bellman_ford.txt", "worst_case_times_bellman_ford.txt"])
multiPlotCreate(dots, False, ["Лучший случай", "Средний случай", "Худший случай"], "Алгоритм Форда-Беллмана", True,  "combined_practic")
dots = readDatas(["best_case_times.txt", "average_case_times.txt", "worst_case_times.txt"])
multiPlotCreate(dots, True, ["Лучший случай", "Средний случай", "Худший случай"], "Алгоритм Дейкстры. Регрессия", True,  "combined_practic_regression")
dots = readDatas(["best_case_times_bellman_ford.txt", "average_case_times_bellman_ford.txt", "worst_case_times_bellman_ford.txt"])
multiPlotCreate(dots, True, ["Лучший случай", "Средний случай", "Худший случай"], "Алгоритм Форда-Беллмана. Регрессия", True,  "combined_practic_regression")
dots = readDatas(["best_case_times.txt", "average_case_times.txt", "worst_case_times.txt", "best_case_times_bellman_ford.txt", "average_case_times_bellman_ford.txt", "worst_case_times_bellman_ford.txt"])
multiPlotCreate(dots, True, ["Лучший случай Алгоритм Дейкстры", "Средний случай Алгоритм Дейкстры", "Худший случай Алгоритм Дейкстры","Лучший случай Алгоритм Форда-Беллмана", "Средний случай Алгоритм Форда-Беллмана", "Худший случай Алгоритм Форда-Беллмана" ], "Сводный график", True,  "combined")
#


dots = readDatas("best_case_times.txt")
multiPlotCreate(dots, False, ["Лучший случай"], "Алгоритм Дейкстры", True,  "best_case")
dots = readDatas("average_case_times.txt")
multiPlotCreate(dots, False, ["Средний случай"], "Алгоритм Дейкстры", True,  "average_case")
dots = readDatas("worst_case_times.txt")
multiPlotCreate(dots, False, ["Худший случай"], "Алгоритм Дейкстры", True,  "wosrt_case")
dots = readDatas("best_case_times.txt")
multiPlotCreate(dots, True, ["Лучший случай"], "Алгоритм Дейкстры", True,  "best_case")
dots = readDatas("average_case_times.txt")
multiPlotCreate(dots, True, ["Средний случай"], "Алгоритм Дейкстры", True,  "average_case")
dots = readDatas("worst_case_times.txt")
multiPlotCreate(dots, True, ["Худший случай"], "Алгоритм Дейкстры", True,  "wosrt_case")
dots = readDatas("best_case_times_bellman_ford.txt")
multiPlotCreate(dots, False, ["Лучший случай"], "Алгоритм Форда-Беллмана", True,  "best_case")
dots = readDatas("average_case_times_bellman_ford.txt")
multiPlotCreate(dots, False, ["Средний случай"], "Алгоритм Форда-Беллмана", True,  "average_case")
dots = readDatas("worst_case_times_bellman_ford.txt")
multiPlotCreate(dots, False, ["Худший случай"], "Алгоритм Форда-Беллмана", True,  "wosrt_case")
dots = readDatas("best_case_times_bellman_ford.txt")
multiPlotCreate(dots, True, ["Лучший случай"], "Алгоритм Форда-Беллмана", True,  "best_case")
dots = readDatas("average_case_times_bellman_ford.txt")
multiPlotCreate(dots, True, ["Средний случай"], "Алгоритм Форда-Беллмана", True,  "average_case")
dots = readDatas("worst_case_times_bellman_ford.txt")
multiPlotCreate(dots, True, ["Худший случай"], "Алгоритм Форда-Беллмана", True,  "wosrt_case")
