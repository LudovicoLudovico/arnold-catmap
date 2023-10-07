import math
import matplotlib.pyplot as plt
from random import random
import numpy as np


class Point:
    x = 0.
    y = 0.

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def evolution(self):
        curr_x = self.x
        self.x = math.fmod(2 * self.x + self.y, 1)
        self.y = math.fmod(curr_x + self.y, 1)

    def inv_evolution(self):
        curr_x = self.x
        self.x = abs(math.fmod(self.x - self.y, 1))
        self.y = abs(math.fmod((-curr_x) + 2.0 * self.y, 1))


n_points = int(input("Number of points (Default 1000): ") or 1000)
iter_n = int(input("Number of iterations (Default 100): ") or 100)

for i in range(0, n_points):
    x = np.random.uniform(0.4, 0.6)
    y = np.random.uniform(0.4, 0.6)
    p = Point(x, y)
    plt.plot(x, y, markersize=0.7, marker='o', color='black')
    for j in range(0, iter_n):
        p.evolution()
    plt.plot(p.x, p.y, markersize=0.5, marker='o', color='red')
    for j in range(0, iter_n):
        p.inv_evolution()
    plt.plot(p.x, p.y, markersize=0.5, marker='o', color='blue')

plt.show()
