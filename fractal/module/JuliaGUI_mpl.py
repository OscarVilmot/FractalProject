import math
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.widgets import Slider
matplotlib.use('Qt5Agg')

def showGUI(fig, Array, sliders):
    ax = fig.subplots()

    ax.clear()
    plt.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)

    ax.imshow(Array, interpolation="bicubic", cmap='plasma')
    plt.show()

def sliders(fig):
    C1slider = plt.axes([.2,.2,.65,.03])
    C2slider = plt.axes([.2,.1,.65,.03])

    C1 = Slider(C1slider, "c1", valmin=-math.pi/6,valmax=math.pi/6,valinit=0,valstep=0.002)
    C2 = Slider(C2slider, "c2", valmin=-math.pi/6,valmax=math.pi/6,valinit=0,valstep=0.002)

    return C1, C2

    
