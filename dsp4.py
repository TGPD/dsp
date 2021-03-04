import numpy as np
import datetime
import time
import math
import pylab as pl
import scipy.signal as signal
import matplotlib.pyplot as plt



# 普通傅里叶变换
from scipy.fftpack import fft, ifft


def fft1(xx):
    t=np.linspace(0, 1.0, len(xx))
    f = np.arange(len(xx)/2+1, dtype=complex)
    for index in range(len(f)):
        f[index]=complex(np.sum(np.cos(2*np.pi*index*t)*xx), -np.sum(np.sin(2*np.pi*index*t)*xx))
    return f


# 普通傅里叶逆变换
def ifft1(a):
    N = len(a)
    f = []
    for k in range(N):
        F = 0
        for m in range(N):
            F += a[m] * np.e**(2j * np.pi * (m*k) / N)/N
        f.append(F)
    return f




def dft(sig):
    N = sig.size
    V = np.matrix([[np.exp(-1j*2*np.pi*v*y/N) for v in range(N)] for y in range(N)])
    return sig.dot(V)

def FFT(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    if N % 2 > 0:
        raise ValueError("size of x must be a power of 2")
    elif N <= 8:  # this cutoff should be optimized
        return dft(x)
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = np.matrix(np.exp(-2j * np.pi * np.arange(N) / N))
        return np.hstack([X_even + np.multiply(factor[0,:int(N/2)],X_odd),
                               X_even + np.multiply(factor[0,int(N/2):],X_odd)])



test = [np.random.random() for i in range(pow(2,13))]

# a = [1,2,3,4,5,6,7,8]
# print(fft1(a))
# print(FFT(a))
# print(ifft1(a))
# print(ifft(a))







# start = time.perf_counter()
# fft1(test)
# end = time.perf_counter()
# print(end-start)
#
# start = time.perf_counter()
# FFT(test)
# end = time.perf_counter()
# print(end-start)
#
# start = time.perf_counter()
# fft(test)
# end = time.perf_counter()
# print(end-start)




# 验证线性性质：
x1 = [np.random.random() for i in range(pow(2,4))]
x2 = [np.random.random() for i in range(pow(2,4))]
x3 = x1 + x2
y1 = fft(x1)
y2 = fft(x2)
y3 = fft(x3)

y4 = []
for v in range(0,len(y1)):
    y4.append(y1[v]+y2[v])
print(y3)
print(y4)



