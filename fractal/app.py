from fractal.common.GUI import showGUI, sliders
from fractal.common.JuliasFractal import calculateArray, fractalJulia
from matplotlib.pyplot import subplots_adjust, figure

def run():
    fig = figure(figsize=(6,7))
    subplots_adjust(bottom=.3)

    start = [-1.5,-1.5]
    size = [3,3]
    precision = 200

    C1 = 0
    C2 = 0

    C = complex(C1, C2)

    A = fractalJulia(C)
    T = calculateArray(start, size, precision, A)

    sliderList = sliders(fig)
    
    def updateJulia(val):
        c1 = sliderList[0].val
        c2 = sliderList[1].val

        C = complex(c1, c2)
        A = fractalJulia(C)
        T = calculateArray(start, size, precision, A)
        showGUI(fig, T, sliderList)


    sliderList[0].on_changed(updateJulia)
    sliderList[1].on_changed(updateJulia)
    
    showGUI(fig, T, sliderList)



