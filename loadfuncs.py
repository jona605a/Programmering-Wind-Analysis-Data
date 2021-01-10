import numpy as np


def dataLoad(filename, Nx, Ny, Nz):
    
    data = np.fromfile(filename)
    
    try:
        data = np.reshape(data, (Nx,Ny,Nz))
        errormessage = 'No error'
    except:
        
        errormessage = 'Wrong dimensions given. Please input valid ranges. \nThere are {:,.0f} points in the given file. '.format(len(data))
    
    return data, errormessage



if __name__ == '__main__':
    data, errormessage = dataLoad('turbine_32x32x8192.bin', 40960, 32, 32)
    print(errormessage)
