#####################################################

# Leonardo Satter Cassara. Berkeley, CA, 02/05/2014. 
# Radio Astronomy code for central limit theorem. 

#####################################################

import numpy as np
import matplotlib.pyplot as plt

#############

def imp(l,c,f):

    w=f*2.*np.pi

    z_l = np.complex(w*l*1j)

    z_c = np.complex(1./(w*c*1j))

    return (z_l*z_c)/(z_l+z_c)


l = 10.**(-6)
c = 22000.*10**(-12)
r = 1./(2.*np.pi*np.sqrt(l*c))

y = []
x=[]

for i in np.arange(r-3., r, 0.01):

    y.append(imp(l,c,i))
    x.append(i)

for j in np.arange(r+0.01, r+3., 0.01):

    y.append(imp(l,c,j))
    x.append(j)

Y=[]

for i in y:
    Y.append((np.sqrt(np.real(i)**2+np.imag(i)**2)))


plt.plot(x,Y)
plt.xlabel(r'$Input \ Frequency$',size=24)
plt.ylabel(r'$Impedance$',size=24)
plt.title(r'$LC \ Filter \ Impedance \ variation$',size=28)
plt.axvline(x=r,color='g',ls='dashed')
plt.text(1.07302*10**(6),3.280992*10**(8),r'$f_{max}='+str(r)+'$',size=26)
plt.show()



