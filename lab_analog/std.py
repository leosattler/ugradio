#####################################################

# Leonardo Satter Cassara. Berkeley, CA, 02/05/2014. 
# Radio Astronomy code for Std behavior with sample size. 

#####################################################

import numpy as np
import matplotlib.pyplot as plt

######### Title

print
print 'Program to show the behavior of the Standard deviation of a given distribution with the sample size.'
print
print 'Given distribution: generation of random numbers with random.random_integers() function.'
print
print 'Calculating 400 Standard Deviations:'
print

######### Defining random distribution (with size 500)

x=np.random.random(400)*100

######### Choosing sample size and random index

res=np.arange(0) # list with the means

std=[]

k=0

c=[] # index of sample x

m=[] # list for the means

N=np.arange(1,len(x)+1,10)

for i in N:

    while k < 1000:    
        for j in np.arange(i):
            c.append(np.random.random_integers(0,len(x)-1))

        for l in c:
            m.append(x[l])       

        res=np.append(res,np.sum(m)/len(m))

        m=[]
        c=[]
        k=k+1

    #m1=np.sum(res)/(np.size(res))

    #m2=np.sum(res*res)/(np.size(res))

    #std.append(np.sqrt(m2-m1*m1))

    std.append(np.std(res))

    print 'For ',i , ' samples,', 'Std = ' , np.std(res)

    res=np.arange(0)

    k=0

######### Plot

plt.plot(N,std,'bo')
#plt.errorbar(N, std, xerr=None, yerr=0.04, fmt=None)
plt.ylabel(r'Standard Deviation', size=33)
plt.xlabel(r'Sample Size', size=33)
plt.title(r'Behavior of Standard Deviation', size=39)
plt.rc('xtick', labelsize=25)
plt.rc('ytick', labelsize=25)

## Curve Fit
plt.plot(N,np.std(x)/np.sqrt(N),'r-')
##

plt.show()



