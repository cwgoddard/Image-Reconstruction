import numpy as np
import numpy.fft as fft
import scipy.ndimage as nd
import scipy.misc as misc
from math import pi

source = nd.imread("einstein.bmp", flatten=True)

pad_len = len(source)
padded = np.pad(source, ((pad_len, pad_len),(pad_len, pad_len)), 'constant', 
                constant_values=((0,0),(0,0)))

ft = fft.fft2(padded)

diffract = np.abs(ft)

l = len(padded)

mask = np.ones((pad_len+2,pad_len+2))
mask = np.pad(mask, ((pad_len-1, pad_len-1),(pad_len-1, pad_len-1)), 'constant', 
                constant_values=((0,0),(0,0)))

guess = diffract * np.exp(1j * np.random.rand(l,l) * 2 * pi)

r = 801
err = np.zeros(r)

beta = 0.8


prev = None
for s in range(0,r):
    #apply fourier domain constraints
    update = diffract * np.exp(1j * np.angle(guess)) 
    
    inv = fft.ifft2(update)
    inv = np.real(inv)
    if prev is None:
        prev = inv
        
    
    temp = inv
    for i in range(0,l):
        for j in range(0,l):
            if inv[i,j] < 0 and mask[i,j] == 1:
                inv[i,j] = prev[i,j] - beta*inv[i,j]
            if mask[i,j] == 0:
                inv[i,j] = prev[i,j] - beta*inv[i,j]
    
    
    prev = temp
    
    guess = fft.fft2(inv)
        
    #save an image of the progress
    if s % 10 == 0:
        misc.imsave("/Users/chasegoddard/Stuff/CDI/code/save/progress" + str(s) +
                    ".bmp", prev)
        print(s)


