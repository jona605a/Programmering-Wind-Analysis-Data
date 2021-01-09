import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter



def dataPlot(data, statistic):
    
    if statistic.lower() == 'mean':
        plttype = 1
    elif statistic.lower() == 'variance':
        plttype = 2
    elif statistic.lower() == 'cross correlation':
        plttype = 3
    else:
        return 'Error, invalid statistic'
    
    #contourPlot(data)
    surfacePlot(data)
    
    plt.title(statistic + ' plot')
    plt.axis('equal')
    plt.ylabel('z')
    plt.xlabel('y')
    
    
    plt.show()

def contourPlot(data):
    fig = plt.figure()
    plt.contour(data)
    
    return fig
        
def surfacePlot(data):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    # Plot the surface.
    surf = ax.plot_surface(data, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    
    # Customize the z axis.
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    
    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)
    
    return fig