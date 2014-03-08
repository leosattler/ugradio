#####################################################

# Leonardo Satter Cassara. Berkeley, CA, 02/14/2014. 
# Radio Astronomy code for Digital Lab. 

#####################################################

import numpy as np
import matplotlib.pyplot as plt

########## Calling arrays

a=np.loadtxt('data_0.1')

b=np.loadtxt('data_0.2')

c=np.loadtxt('data_0.3')

d=np.loadtxt('data_0.4')

e=np.loadtxt('data_0.5')

f=np.loadtxt('data_0.6')

g=np.loadtxt('data_0.7')

h=np.loadtxt('data_0.8')

i=np.loadtxt('data_0.9')

########## Plot

k=1

l=0.1

for item in (a,b,c,d,e,f,g,h,i):

######### Defining 

    if k == 1:
        plt.rc('xtick', labelsize=0)
        plt.rc('ytick', labelsize=18)
    elif k == 4:
        plt.rc('xtick', labelsize=0)
        plt.rc('ytick', labelsize=18)
    elif k == 8:
        plt.rc('xtick', labelsize=18)
        plt.rc('ytick', labelsize=0)
    elif k == 9:
        plt.rc('xtick', labelsize=18)
        plt.rc('ytick', labelsize=0)
    elif k == 7:
        plt.rc('xtick', labelsize=18)
        plt.rc('ytick', labelsize=18)
    else:
        plt.rc('xtick', labelsize=0)
        plt.rc('ytick', labelsize=0)
        
        
    plt.subplot(3,3,k)
    plt.grid()
    plt.plot(item,'-*')
    plt.axis([0,12,-0.35,0.35])
    plt.title('Plot for '+str(l)+r'$\times \ \nu_{sampl}$',size=26)
    #plt.xlabel('Sample Number',size=18)
    #plt.ylabel('Voltage',size=18)

    if k in (1,4,7):
        plt.ylabel(r'Amplitude $[Volts]$',size=22)

    if k in (7,8,9):
        plt.xlabel('Time '+r'$[\mu s]$',size=22)


    k=k+1
    l=l+0.1
    

#plt.title('')

plt.show()
