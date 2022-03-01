import numpy as np
import matplotlib.pyplot as plt
def FFT(x):
	N = len(x)    
	if N == 1:
		return x
	else:
		X_even = FFT(x[::2])
		X_odd = FFT(x[1::2])
		factor = np.exp(-2j*np.pi*np.arange(N)/ N)
        
	X = np.concatenate(\
		[X_even+factor[:int(N/2)]*X_odd, X_even+factor[int(N/2):]*X_odd])
	return X
# sampling rate
fs = 128
# sampling interval
ts = 1.0/fs
t = np.arange(0,1,ts)
freq = 1.
x = 3*np.sin(2*np.pi*freq*t)
freq = 4
x += np.sin(2*np.pi*freq*t)
freq = 7
x += 0.5* np.sin(2*np.pi*freq*t)
N = len(x)
plt.figure(figsize = (8, 6))
plt.plot(t, x, 'r')
plt.ylabel('Input Amplitude')
plt.show()
# Compute FFT of x
X=FFT(x)
print(X)	
def inverseFFT_1D(u):
    """ use recursive method to speed up"""
    
    u = np.asarray(u, dtype=complex)
    u_conjugate = np.conjugate(u)

    x = FFT(u_conjugate)

    x = np.conjugate(x)
    x = x / u.shape[0]
    return x	
B=inverseFFT_1D(X)
Z=B
plt.figure(figsize = (8, 6))
plt.plot(t, Z, 'r')
plt.ylabel('Input Amplitude after ifft')
plt.show()
