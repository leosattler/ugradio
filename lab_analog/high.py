#####################################################

# Leonardo Satter Cassara. Berkeley, CA, 02/05/2014. 
# Radio Astronomy code for High Pass Filter. 

#####################################################

import numpy as np
import matplotlib.pyplot as plt


def imp_rc(r,c,w):
    
    #r_c = 1./(np.complex(1j*w*c))

    #return 20.*np.log10(r_c./(np.sqrt(r**2 + r_c**2.)))
    w *= 2*np.pi
    return 20.*np.log10(w*r*c/(np.sqrt(1. + (w**2.)*(r**2.)*(c**2.))))

r = 419.45
c = 1.e-6
res = 1./(2.*np.pi*r*c)

y = []
x=[]

#look up np.linspace, np.logspace
for i in np.arange(res-100000., res+70000, 1):

    y.append(imp_rc(r,c,i))
    x.append(i)


plt.plot(x,y)
plt.xlabel(r'Frequency (Hz), Log Scale',size=25)
plt.ylabel(r'$20log\left(V_{in}/V_{out}\right)$ in $dB$',size=25)
plt.title(r'RC Filter Impedance Variation',size=29)
plt.axis([50,10**(5),-15,2])
plt.xscale('log')
plt.axhline(-3., color='g',ls='dashed')
plt.axvline(res,color='g',ls='dashed')
plt.text(500,-4.5,r'$\omega_{3dB}\approx'+str(379.4)+'$', size=27)
plt.rc('xtick', labelsize=24)
plt.rc('ytick', labelsize=24)
#plt.text(1.07302*10**(6),3.280992*10**(8),r'$f_{max}='+str(r)+'$',size=16)
plt.show()

