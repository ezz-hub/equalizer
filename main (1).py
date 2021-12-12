from scipy import signal
from scipy.fft import fftshift
import matplotlib.pyplot as plt
import numpy as np
Alpha=1
Beta=1
Ts = 1/20
fs = 20
t = np.arange(0,10+Ts,Ts)

fMin=2
FMax=3

y=[1,2,3,4]


for i in range(3):

    if(fMin<y[i]):
        Alpha=0 # Alpha of y[i] Min

    if(FMax>y[i]):
        Beta=0  #Beta of Y[i] Max





x =Alpha* 2*np.sin(2*np.pi*y[0]*t)+ 2*np.sin(2*np.pi*y[1]*t)+2*np.sin(2*np.pi*y[2]*t)+Beta*2*np.sin(2*np.pi*y[3]*t)

vmin = 20*np.log10(np.max(x)) - 60
plt.subplot(211)

plt.subplot(212)

cmap = plt.get_cmap('cool')
cmap.set_under(color='k', alpha=None)

y=plt.specgram(x, Fs=fs,cmap=cmap, NFFT=256, noverlap=256/2,vmin=vmin)
print(y[2])
plt.colorbar()#format='%+2.0f dB')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.tight_layout()
plt.show()



