import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

row = np.array(
    [-0.03, 0.73, -0.59, -1.59, 0.38, 1.49, 0.14, -0.62, -1.59, 1.45, -0.38, -1.49, -0.15, 0.63, 0.06, -1.59, 0.61,
     0.62,
     -0.05, 1.56])


def print_answer(row):
    print(f"Исходный ряд: {row}")
    variation_row_not_unique =row.copy()
    variation_row_not_unique.sort()

    variation_row = np.unique(row.copy(), )
    variation_row.sort()
    print(f"Вариационный ряд: {variation_row}")
    max = variation_row[variation_row.size - 1]
    min = variation_row[0]
    print(f"Эстремальные значения\nМинимум: {min}\nМаксимум: {max}")
    selection_scope = max - min
    print(f"Размах: {selection_scope}")
    math_waiting = np.sum(variation_row) / variation_row.size
    temp_array = variation_row.copy()
    standard_deviation = (np.sum((temp_array - math_waiting) ** 2) / temp_array.size) ** 0.5
    print(f"Математическое ожидание: {math_waiting}\nСреднеквадратичное отклонение: {standard_deviation}")

    selection_volume = variation_row.size
    empirical_values = [(i / selection_volume) for i in range(selection_volume)]
    print("f(x)   value")
    for i in range(variation_row.size - 1):
        print(f"({variation_row[i]};{variation_row[i + 1]}] : {empirical_values[i + 1]}")

    # Эмпирическая функция распределения
    plt.step(variation_row, empirical_values, color="r")
    plt.show()

    # Гистограмма

    # формула Стерджесса
    interval_count = int(1 + np.log2(selection_volume))

    sns.histplot(variation_row, stat="density", color="r", bins=interval_count)
    plt.show()

    # Полигон группированной выборки
    interval_width = selection_scope / interval_count

    counter = 0
    last_element = variation_row_not_unique[0]
    for i in range(interval_count):
        for j in range(row.size):
            if (variation_row_not_unique[j] < (last_element + interval_width) and variation_row_not_unique[j] >= last_element):
                counter += 1
        print(f"[{last_element};{last_element + interval_width}) : {counter}")
        counter = 0
        last_element += interval_width

    y, x = np.histogram(variation_row, np.arange(min, max + 0.1, interval_width))
    interval_centres = [(x[i] + x[i - 1]) * 0.5 for i in range(1, x.size)]
    plt.plot(interval_centres, y, color="r")
    plt.show()


print_answer(row)
