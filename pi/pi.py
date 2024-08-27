from math import sqrt, pi
import random
import matplotlib.pyplot as plt
from tqdm import tqdm


def estimate_pi(N, display=False):
    points_x = []
    points_y = []

    for _ in range(N):
        x = random.uniform(-0.5, 0.5)
        y = random.uniform(-0.5, 0.5)
        points_x.append(x)
        points_y.append(y)

    in_square = 0
    in_circle = 0

    for i in range(N):
        in_square += 1
        if sqrt((points_x[i] ** 2) + (points_y[i] ** 2)) <= 0.5:
            in_circle += 1
    ret = (in_circle / in_square) * 4

    pe = abs((ret - pi) / pi) * 100

    if display:
        print(f"N = {N} | approx = {ret} | percent error = {pe}%")
    return ret


def plot_estimations():
    incs = [10,100,1000,10000,100000,1000000]
    for inc in incs:
        vals = []
        for _ in tqdm(range(1000)):
            vals.append(estimate_pi(inc))
        fig=plt.figure(figsize=(10,8))
        plt.hist(vals, bins=40)
        plt.title(f"N={inc}")
        plt.yscale('log')
        plt.savefig(rf'C:\Users\jackm\PycharmProjects\PHYS416\pi\plots\est{inc}.png')
        plt.close(fig)


def average_runs(N, n):
    avg_ret = 0.0
    for i in range(n):
        avg_ret += estimate_pi(N)

    avg_ret /= n

    pe = abs((avg_ret - pi) / pi) * 100

    print(f"N = {N} | avg approx over {n} runs = {avg_ret} | percent error of average = {pe}%")


plot_estimatios()