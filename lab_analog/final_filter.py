#####################################################

# Leonardo Satter Cassara. Berkeley, CA, 02/05/2014. 
# Radio Astronomy code for central limit theorem. 

#####################################################

import numpy as np
import matplotlib.pyplot as plt


def imp_rc(r,c,w):
    
    #r_c = 1./(np.complex(1j*w*c))

    #return 20.*np.log10(r_c./(np.sqrt(r**2 + r_c**2.)))
    w *= 2*np.pi
    return 20.*np.log10(1./(np.sqrt(1. + (w**2.)*(r**2.)*(c**2.))))

r = 150.
c = 10000.*10**(-12)
res = 1./(2.*np.pi*r*c)

y = []
x=[]

#look up np.linspace, np.logspace
for i in np.arange(res-1000000., res+700000, 10):

    y.append(imp_rc(r,c,i))
    x.append(i)


plt.plot(x,y)
plt.xlabel(r'Frequency (Hz), Log Scale',size=25)
plt.ylabel(r'$20log\left(V_{in}/V_{out}\right)$ in $dB$',size=25)
plt.title(r'RC Filter Impedance Variation',size=29)
plt.axis([10,2.6*10**(6),-18,2])
plt.xscale('log')
plt.axhline(-3., color='g',ls='dashed')
plt.axvline(res,color='g',ls='dashed')
plt.text(res+16000,-2.5,r'$\omega_{3dB}\approx'+str(106103.3)+'$', size=27)
plt.rc('xtick', labelsize=24)
plt.rc('ytick', labelsize=24)
#plt.text(1.07302*10**(6),3.280992*10**(8),r'$f_{max}='+str(r)+'$',size=16)
plt.show()

