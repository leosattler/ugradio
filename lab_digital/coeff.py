#!/usr/bin/env python
import numpy as np 
from numpy.fft import *
from matplotlib import pyplot as plt
from numpy.fft import *
import radiolab

N = 8
Window = 5 # Centered window

print 'Generating Coeffs:'
print
Fir = np.zeros(N)
print Fir
print
Fir[N/2+1:N/2+1+(Window-1)/2] = 1.0
print Fir
print
Fir[N/2-(Window-1)/2:N/2+1] = 1.0
print Fir
print

FirShift = fftshift(Fir)
print 'Fir Shift: ', FirShift
print
FirPhys = ifft(FirShift)
print 'Fir Phys: ', FirPhys
print

FirCoeffs = ifftshift(FirPhys)
print 'Fir Coeffs Shift: ', FirCoeffs
print
FirCoeffs = np.real(FirCoeffs)
print 'Fir Real: ', FirCoeffs


# Demonstration of "padding with zeros to achieve higer resolution
N_Extend = 2048 # Extend to 2*Extend
FirEx = np.zeros(N_Extend)
FirEx[(N_Extend/2)-4:(N_Extend/2)+4] = FirCoeffs

FirShiftEx = fftshift(FirEx)
FirPhysEx = fft(FirShiftEx)

FirCoeffsEx = fftshift(FirPhysEx)
FirCoeffsEx = np.real(FirCoeffsEx)

ImagData = np.fromfile('ddc_imag_bram','>i4')
RealData = np.fromfile('ddc_real_bram','>i4')

#ExpData = RealData + 1j*ImagData
ExpData = RealData 
FourData = fftshift(fft(ExpData))
FourData = abs(FourData)

#FreqAx = (np.arange(2048)/2048.-.5)/(5e-9)
FreqAx = fftfreq(2048,d=1./(200e6))


plt.plot(fftshift(FreqAx),FourData)
#plt.subplot(2,1,2)
plt.plot((np.arange(2048)/2048.0)*2e8-1e8,(abs(FirCoeffsEx)**2)*10e7)
plt.title('Comparrison of Filters',size=28)
plt.xlabel('Frequency (Hz)',size=24)
plt.ylabel('Spectral Power',size=24)
#plt.axis([0,64,-0.02,0.08])
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)

plt.subplots_adjust(hspace=0.3)
plt.show()
