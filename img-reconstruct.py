import numpy as np
import numpy.fft as fft
import scipy.ndimg as nd

source = nd.imread("einstein.bmp", flatten=True)

pad_len = len(source)
padded = np.pad(source, ((pad_len, pad_len),(pad_len, pad_len)), 'constant', 
                constant_values=((0,0),(0,0)))

ft = fft.fft2(padded)

diffract = np.abs(ft)

