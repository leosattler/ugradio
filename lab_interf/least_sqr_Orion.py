import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft

#######################################

# Leonardo Sattler Cassara, UC Berkeley  
# Radiolab Class, Orion Least Square Calculation

######################################    

f = 'data_orion_140321_2.npz'

data = np.load(f)

x = data['jd']

y = data['volts']


## taking care of the plot! ##

xx = x
yy = y[0:len(xx)]

y_final = yy
for i in np.arange(10, len(yy)-10):
    if yy[i] < -0.0009:
        y_final[i] = np.average(yy[i-10:i+10])


## Redefining axis. Finally!! ##

XX = xx
YY = y_final


## Smoothing! ##

SM=[]
r = 100
while r < len(XX)-100:
    box = np.arange(r-100,r+101)
    SM.append(np.median(YY[box]))
    r = r+1



x = data['jd']

y = data['volts']

plt.subplot(2,1,1)
plt.plot(x,y,'b-') 
plt.plot(XX[100:-100],SM,'r-')

plt.subplot(2,1,2)
plt.plot(XX[100:-100],YY[100:-100]-SM,'b-') 

plt.show()


#### The Least Square ####

xx_f = data['lst'][0:len(XX)]
x_f = xx_f[100:-100]*np.pi/12. 
y_f = YY[100:-100]-SM

B_line = 10.
lamb = 2.8*10**(-2) 
ra = 1.44 
dec = -5.38*np.pi/180. 
C = (B_line*np.cos(dec))/lamb

X = np.empty([len(x_f),2])
X[:,0]= np.cos(2*np.pi*C*np.sin(x_f-ra))
X[:,1]= -np.sin(2*np.pi*C*np.sin(x_f-ra))

b=np.matrix(X)
bt = np.transpose(b)
a  = np.transpose(np.matrix(y_f))

# Compute moore-penrose pseudo inverse

btb = bt*b
mpsi  = np.linalg.inv(btb)
c = (mpsi * bt) * a


print
print 'Linear least squares'
print
print 'Values of a11, a12, xo for x are:'
print
print 'a11 =', c[0,0], 'a12 =',  c[1,0]


## Least Square 2 (from casper) ##

Y_2 = YY[100:-100]-SM

X_2 = np.empty([len(x_f),2])
X_2[:,0]= np.cos(2*np.pi*C*np.sin(x_f-ra))
X_2[:,1]= -np.sin(2*np.pi*C*np.sin(x_f-ra))

X_X = np.dot(np.transpose(X_2),X_2)

XY = np.dot(np.transpose(X_2),Y_2)

XXI = np.linalg.inv(X_X)

a = np.dot(XY,XXI)

print
print 'Linear least squares 2'
print
print'Values of a11, a12 are:'
print 
print 'a11 =', a[0], 'a21 =', a[1]

YBAR = np.dot(X_2,a)

plt.subplot(2,1,1)
plt.title('Least Square for Orion',size=26)
plt.plot(XX[100:-100],Y_2,'b-') 
plt.plot(XX[100:-100],YBAR,'r-')
plt.rc('ytick', labelsize=19)
plt.rc('xtick', labelsize=19) 
plt.ylabel('Power Spectra' + r' $[V]^{2}$',size=23)
plt.xlabel('Julian Date [Decimal Days]',size=23)

plt.subplot(2,1,2)
plt.plot(XX[100:-100][200:900],Y_2[200:900],'b-') 
plt.plot(XX[100:-100][200:900],YBAR[200:900],'r-')
plt.rc('ytick', labelsize=19)
plt.rc('xtick', labelsize=19) 
plt.ylabel('Power Spectra' + r' $[V]^{2}$',size=23)
plt.xlabel('Julian Date [Decimal Days]',size=23)

plt.show()

plt.title('Least Square for Orion',size=26)
plt.plot(XX[100:-100],Y_2,'b-') 
plt.plot(XX[100:-100],YBAR,'r-')
plt.rc('ytick', labelsize=19)
plt.rc('xtick', labelsize=19) 
plt.ylabel('Power Spectra' + r' $[V]^{2}$',size=23)
plt.xlabel('Julian Date [Decimal Days]',size=23)
plt.show()


#### Residuals! ####

chi = []
k = np.arange(C-50, C+50)
M = len(x_f)
N = 2
bb = []

for i in k:

    X_2 = np.empty([len(x_f),2])
    X_2[:,0]= np.cos(2*np.pi*i*np.sin(x_f-ra))
    X_2[:,1]= -np.sin(2*np.pi*i*np.sin(x_f-ra))

    X_X = np.dot(np.transpose(X_2),X_2)

    XY = np.dot(np.transpose(X_2),Y_2)

    XXI = np.linalg.inv(X_X)

    a = np.dot(XY,XXI)

    YBAR = np.dot(X_2,a)

    res = Y_2 - YBAR 
    
    chi.append(np.sum(res**2)/(M-N))

    #bb.append(i*lamb/np.cos(dec))

plt.title('Squared Residuals vs C for Orion',size=26)
plt.plot(k, chi,'b-o')
plt.axvline(x=k[list(chi).index(np.min(chi))],color = 'g')
plt.rc('ytick', labelsize=19)
plt.rc('xtick', labelsize=19) 
plt.ylabel('Squared Residuals',size=23)
plt.xlabel('Range of C values',size=23)

plt.show()


C_min = k[list(chi).index(np.min(chi))]
co_dec = C_min*lamb/B_line
dec_f = np.arccos(co_dec)
print
print 'C min=', C_min
print 
print 'Base line = ', C_min*lamb/np.cos(dec)
