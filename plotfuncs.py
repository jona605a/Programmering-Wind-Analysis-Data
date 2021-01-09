import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # This import registers the 3D projection, but is otherwise unused.
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from dataStatistics import dataStatistics

def dataPlot(data, statistic, ranges, plottype, Yref = 0, Zref = 0, DeltaX = 0):
    
    M = dataStatistics(data, statistic, Yref, Zref, DeltaX)
    
    if plottype == 'Contour':
        contourPlot(M)
    elif plottype == 'Surface':
        surfacePlot(M, ranges)
    
    plt.title(statistic + ' plot')
    plt.xlabel('y')
    plt.ylabel('z')
    
    
    plt.show()

def contourPlot(data):
    plt.contour(data)
    
        
def surfacePlot(data, ranges):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    # Ranges
    Y = np.arange(0, ranges[1])
    Z = np.arange(0, ranges[2])
    Y, Z = np.meshgrid(Y, Z)
    
    # Plot the surface.
    surf = ax.plot_surface(Y, Z, data, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    
    # Customize the z axis.
    #ax.set_zlim(-1.01, 1.01)
    #ax.zaxis.set_major_locator(LinearLocator(10))
    #ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    
    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)
    