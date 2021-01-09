import numpy as np

def dataStatistics(data, statistic, Yref = 0, Zref = 0, DeltaX = 0):

    y_length = len(data[0])
    z_length = len(data[0,0])

    return_statistic = np.zeros((y_length,z_length))
    print(y_length, z_length, return_statistic)
    for i in range(y_length):
        for j in range(z_length):
            if statistic == "Mean":
                return_statistic[i,j] = np.mean(data[:,i,j])
            elif statistic == "Variance":
                return_statistic[i,j] = np.var(data[:,i,j])
            else:
                return_statistic[i,j] = np.correlate(data[:(len(data) - DeltaX),i,j], data[DeltaX:,i,j])
        return_statistic

if __name__ == "__main__":
    test_array = np.array([[[1,2,3],[2,3,4],[3,4,5]],[[4,5,6],[5,6,7],[6,7,8]],[[7,8,9],[8,9,10],[9,10,11]]])
    print(test_array, dataStatistics(test_array, statistic = "Mean"))