import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft

a=np.loadtxt('MixAnPlus')

b=np.fromfile('mix_bram', dtype='>i4')

#t_a=fft.fftfreq(len(a))

#t_b=fft.fftfreq(len(b))

t_a=fft.fftfreq(len(a),d=1./(4e6))

t_b=fft.fftfreq(len(b),d=1./(200e6))

plt.subplot(2,1,1)
plt.plot(fft.fftshift(t_a),fft.fftshift(np.abs(fft.fft(a))**2))
plt.title('Analog Mixer Power Spectrum',size=26)
plt.xlabel('Frequency '+r'$[kHz]$',size=22)
plt.ylabel('Power Spectrum',size=22)
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)
plt.axis([-250000,250000,0,7000])

plt.subplot(2,1,2)
plt.plot(fft.fftshift(t_b),fft.fftshift(np.abs(fft.fft(b))**2))
plt.title('Digital Mixer Power Spectrum',size=26)
plt.xlabel('Frequency '+r'$[kHz]$',size=22)
plt.ylabel('Power Spectrum',size=22)
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)
plt.axis([-250000,250000,0,1e12])

plt.subplots_adjust(hspace=0.3)
plt.show()
