<<<<<<< HEAD
#####################################################

# Leonardo Satter Cassara. Berkeley, CA, 02/05/2014. 
# Radio Astronomy code for central limit theorem. 

#####################################################

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

######### Title

print
print 'Program to show the approach of a Normal Distribution by given mean of samples.'
print
print 'Original distribution: generation of random numbers with random.random_integers() function.'
print

######### Inputing the values

i1=input('Type maximum value of your distribution: ')
print
i2=input('Define sample size: ')
print
i3=input('Define your n: ' )
print

######### Defining random distribution (with size i1)

x=[] # random results from 0 to i1

for i in np.arange(float(i1+1)):
    x.append(float(np.random.random_integers(i1)))

######### Choosing sample size and random index

c=[] # index of sample x

m=[] # list for the means

res=[] # list with the means

n=0

while n < i3:    

    for i in np.arange(i2):
        c.append(np.random.random_integers(i1))

    for i in c:
        m.append(x[i])

    res.append(np.sum(m)/len(m)) 

    m=[]
    c=[]
    n=n+1

print 'Mean: ', np.mean(res), ',Standard Deviation: ', np.std(res)
print 

######### Plot

n, bins, patches = plt.hist(res, 50, normed=1, facecolor='g')
plt.xlabel(r'$Means$', size=24)
plt.ylabel(r'$Normalized Occurrences$', size=24)
plt.title(r'$Histogram$', size=28)

m1=np.mean(res)
s1=np.std(res)
g=mlab.normpdf(bins,m1,s1)
plt.plot(bins,g,'r-')

plt.show()

######### Choosing another N

s=raw_input('Choose another n? y/n ' )

n=0

while s == 'y':

    print
    i3=input('Define your n :' )
    print

    while n < i3:    

        for i in np.arange(i2):
            c.append(np.random.random_integers(i1))

        for i in c:
            m.append(x[i])

        res.append(np.sum(m)/len(m)) 

        m=[]
        c=[]
        n=n+1

    print 'Mean: ', np.mean(res), ',Standard Deviation: ', np.std(res)
    print 

######### Plot

    n, bins, patches = plt.hist(res, 50, normed=1, facecolor='g')
    plt.xlabel(r'$Means$', size=24)
    plt.ylabel(r'$Normalized Occurrences$', size=24)
    plt.title(r'$Histogram$', size=28)

    m1=np.mean(res)
    s1=np.std(res)
    g=mlab.normpdf(bins,m1,s1)
    plt.plot(bins,g,'r-')

    plt.show()

    s=raw_input('Choose another N? y/n ' )

    n=0

else:
    print 'Bye!'


=======
save.py
>>>>>>> f03e506eed37f496d2d5e5b1115005e50b4d20df
