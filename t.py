import matplotlib.pyplot as plt


def parse_data(text):
    # Ищем omega0 и t
    for line in text.split("\n"):
        if "omega0" in line:
            parts = line.split("=")
            omega0 = float(parts[1].split(",")[0].strip())
            t = float(parts[2].strip())
            break

    # Парсим метод бисекции
    bisection = []
    for line in text.split("\n"):
        if "Iteration" in line and "[" in line:
            nums = line[line.find("[") + 1 : line.find("]")].split(",")
            bisection.append((float(nums[0]), float(nums[1])))

    # Парсим метод Ньютона
    newton = []
    for line in text.split("\n"):
        if "Iteration" in line and "[" not in line and "starting" not in line:
            num = line.split()[1]  # Берем первое число после "Iteration"
            newton.append(float(num))

    return omega0, t, bisection, newton


def plot_methods(bisection, newton):
    plt.figure(figsize=(12, 6))

    # График бисекции
    plt.subplot(1, 2, 1)
    x = range(len(bisection))
    plt.plot(x, [a for a, b in bisection], "b-", label="Левая граница")
    plt.plot(x, [b for a, b in bisection], "r-", label="Правая граница")
    plt.xlabel("Итерации")
    plt.ylabel("Значение")
    plt.title("Метод бисекции")
    plt.legend()
    plt.grid()

    # График Ньютона
    plt.subplot(1, 2, 2)
    plt.plot(range(len(newton)), newton, "go-", label="Приближение")
    plt.xlabel("Итерации")
    plt.ylabel("Значение")
    plt.title("Метод Ньютона")
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()


data = """
[Example_2] omega0 = 6.31, t = 1.2351
    6.31 1.2351
    Bisection method, starting with [1.01,10]
    Iteration [1.01,10]
    Iteration [5.505,10]
    Iteration [7.7525,10]
    Iteration [8.87625,10]
    Iteration [9.43812,10]
    Iteration [9.71906,10]
    Iteration [9.71906,9.85953]
    Iteration [9.71906,9.7893]
    Iteration [9.71906,9.75418]
    Iteration [9.71906,9.73662]
    Iteration [9.72784,9.73662]
    Iteration [9.72784,9.73223]
    Iteration [9.73004,9.73223]
    Iteration [9.73004,9.73113]
    Iteration [9.73059,9.73113]
    Iteration [9.73086,9.73113]
    Iteration [9.731,9.73113]
    Iteration [9.73107,9.73113]
    Iteration [9.7311,9.73113]
    Iteration [9.73112,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Iteration [9.73113,9.73113]
    Newton's method, starting with 4.495
    Iteration 4.495 9.49851
    Iteration 9.49851 9.73096
    Iteration 9.73096 9.73113
    Iteration 9.73113 9.73113
    Lambda in bisection = 9.731126993968664
    Lambda in newthon = 9.731126993968664
    |lambda_bisection-lambda_newton|= 0.000000000000000
"""

omega0, t, bisection, newton = parse_data(data)
plot_methods(bisection, newton)
