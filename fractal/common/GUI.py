import matplotlib.pyplot as plt

def showGUI(figure, Array):
    ax = plt.axes()

    ax.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)
    ax.clear()

    ax.imshow(Array, interpolation="bicubic", cmap='plasma')
    plt.show()