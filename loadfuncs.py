import numpy as np


def dataLoad(filename, Nx, Ny, Nz):
    
    data = np.fromfile(filename)
    
    try:
        data = np.reshape(data, (Nx,Ny,Nz))
        errormessage = 'No error'
    except:
        # Temporary
        data = np.reshape(data, (len(data)//(Ny*Nz), Ny, Nz))
        errormessage = 'Wrong dimension'
    
    return data, errormessage



if __name__ == '__main__':
    data = dataLoad('turbine_32x32x8192.bin', 40960, 32, 32)
