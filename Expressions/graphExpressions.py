import numpy as np
import matplotlib.pyplot as plt

def graphDisplay(math):
    
    x = np.arange(-5, 5, 0.1)
    y = eval(math)
    plt.plot(x, y)
    plt.savefig("./images/graph.png")
    plt.clf()