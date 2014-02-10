#####################################################

# Leonardo Satter Cassara. Berkeley, CA, 02/05/2014. 
# Radio Astronomy code to calculate Gain of an Amplifier. 

#####################################################

import numpy as np
import matplotlib.pyplot as plt

#############

def gain(re,rc,c,w):

    w=w*2.*np.pi
    a=rc/re
    b=(re**2.)*(w**2.)*(c**2.)
    return a*np.sqrt(1+b)

re=220.
rc=510.
c=1.e-6

x=np.linspace(1,100000000,100000)

y=gain(re,rc,c,x)

plt.plot(x,y)
plt.xscale('log')
plt.axis([10e3,10e7,0,250000])
plt.xlabel(r'Log of Input Frequency',size=25)
plt.ylabel(r'Gain',size=25)
plt.title(r'Gain of the Amplifier for Input Frequency',size=29)
plt.text(10e4,150000,r'$g=\frac{R_C}{R_E}\sqrt{(1+R^{2}_{E}\omega^{2}C_{3}^{2})}$',size=27)
plt.axvline(np.log10(1./(re*c)),color='g',ls='dashed')
plt.rc('xtick', labelsize=23)
plt.rc('ytick', labelsize=23)
plt.show()
