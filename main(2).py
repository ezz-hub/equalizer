
from scipy import signal
from scipy.fft import fftshift
import matplotlib.pyplot as plt
import numpy as np

fs = 32e3
t = np.arange(0, 15, 1.0/fs)
f0 = 1e3
A = 1
x = A*np.sin(2*np.pi*f0*t)

fig, ax = plt.subplots()
cmap = plt.get_cmap('viridis')
vmin = 20*np.log10(np.max(x)) - 40  # hide anything below -40 dBc
cmap.set_under(color='k', alpha=None)

NFFT = 256
pxx,  freq, t, cax = plt.specgram(x/(NFFT/2), Fs=fs, mode='magnitude',
                                 NFFT=NFFT, noverlap=NFFT/2,
                                 vmin=vmin, cmap=cmap,)
fig.colorbar(cax)
plt.show()
