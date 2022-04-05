import numpy as np

class fractalJulia:
    def __init__(self, c):
        self.c = c 

    def nextValue(self, ZnM1):
        return ZnM1**2 + self.c

    def calculateValue(self, x, y, threshold, limit):
        Z = complex(x, y)

        for i in range(threshold):
            Z = self.nextValue(Z)
            if abs(Z) > limit:
                return i
        return threshold - 1
   


def calculateArray(start, size, precision, fractal, threshold = 20, limit = 4.):
    X = np.linspace(start[0], start[0] + size[0], num = size[0]*precision)
    Y = np.linspace(start[1], start[1] + size[1], num = size[1]*precision)

    Array = np.empty((len(X), len(Y)))

    for x in range(len(X)):
        for y in range(len(Y)):
            Array[x, y] = fractal.calculateValue(X[x], Y[y], threshold, limit)
    return Array