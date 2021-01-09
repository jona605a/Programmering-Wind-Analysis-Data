import numpy as np

def dataStatistics(data, statistic, Yref = 0, Zref = 0, DeltaX = 0):

    y_length = len(data[0])
    z_length = len(data[0,0])

    return_statistic = np.zeros((y_length,z_length))

    for i in range(y_length):
        for j in range(z_length):
            if statistic == "Mean":
                return_statistic[i,j] = np.mean(data[:,i,j])
            elif statistic == "Variance":
                return_statistic[i,j] = np.var(data[:,i,j])
            else:
                return_statistic[i,j] = np.correlate(data[:(len(data) - DeltaX),i,j], data[DeltaX:,i,j])

    return return_statistic
