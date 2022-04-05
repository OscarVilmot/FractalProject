from fractal.common.GUI import showGUI
from fractal.common.JuliasFractal import calculateArray, fractalJulia
from matplotlib.pyplot import subplots, subplots_adjust

def run():

    fig, ax = subplots()
    subplots_adjust(bottom=0.35)

    start = [-2,-2]
    size = [4,4]
    precision = 100

    C1 = -0.038088
    C2 = 0.9754633

    C = complex(C1, C2)

    A = fractalJulia(C)
    T = calculateArray(start, size, precision, A)

    showGUI(fig, T)