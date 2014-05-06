import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as scp

data = np.load('data.npz')

l = data['longitude']  

b = data['latitude'] 

spec = data['spectrum'] 

freq = data['freqs']

vel = (1420.4058-(freq))*299790 # doppler vel in km/sec

del_v = ((4.e6)/len(spec[0]))/(4.73e3)

res = input('Type resolution: ')

#fac = input('Type resolution: ')
#fac = 4.
fac =2.

#intg = []

grid_mom0 = np.zeros([res*1000,res*1000])
grid_mom1 = np.zeros([res*1000,res*1000])
whg = np.zeros([res*1000,res*1000])
k = np.zeros([res*1000,res*1000])

#p = input('Type distr. meas. (use 35!): ')
p = 55.
intg = []

for i in np.arange(len(b)):
    if b[i] >= -60:
        m = np.round(l[i])
        n = b[i]
        #grid[round((n+70)*999/60.),((190-(190-m)*np.cos(b[i]*np.pi/180.))-160)*999/60.] =  (1.8e18)*np.sum(spec[i])*del_v
        x_pos = (n+70)*(res*1000-1)/60.0
        y_pos = ((190-(190-m)*np.cos(b[i]*np.pi/180.))-160)*(res*1000-1)/60.
        
        for val in spec[i]:
            if val > 2.:
                intg.append(val)

        #intg = spec[i][list(spec[i]).index(np.max(spec[i]))-100:list(spec[i]).index(np.max(spec[i]))+100]
        #print np.sum(intg)
        grid_mom0[x_pos,y_pos] = (1.8e18)*np.sum(intg)*del_v
        grid_mom1[x_pos,y_pos] = np.sum(spec[i]*vel)/np.sum(spec[i])
        
        whg[x_pos,y_pos] = 1.
        intg = []

for i in np.arange(res*1000):
    for j in np.arange(res*1000):
        gau = np.exp(-((i-(res*1000)/2.)**2 + (j-(res*1000)/2.)**2)/(2.*p**2.))
        k[i,j] = gau

cnv = scp.fftconvolve(grid_mom0, k, mode='same')

whg_cnv = scp.fftconvolve(whg, k, mode='same')

epsilon = 0.0001
for i in np.arange(res*1000):
    for j in np.arange(res*1000):
        if whg_cnv[i,j] < epsilon:
            whg_cnv[i,j] = 1.
            cnv[i,j] = 0
img  = cnv/whg_cnv

fin_img = np.zeros([1+fac*120,1+fac*120])
l_range = np.linspace(160,220,1+fac*120)
b_range = np.linspace(-70,-10,1+fac*120)

for idx in np.arange(len(l_range)):
    for jdx in np.arange(len(b_range)):
        fin_img[jdx,idx] = img[(b_range[jdx]+70)*(res*1000-1)/60.,((190-(190-l_range[idx])*np.cos(b_range[jdx]*np.pi/180.))-160)*(res*1000-1)/60.]


plt.imshow(fin_img, cmap = 'gray', origin='lower', extent = (160,220,-70,-10), vmin = 0.0, vmax=2.8e21)
plt.title('The Orion-Eridanus Superbubble', size = 25)
plt.xlabel(r'$l$', size = 24)
plt.ylabel(r'$b$', size = 24)

cb = plt.colorbar()
cb.set_label('Column Density ' + r'$[cm^{2}]$', size = 23)

plt.show()

plt.imshow(img, cmap = 'gray', origin='lower', extent = (160,220,-70,-10), vmin = 0.0, vmax=2.8e21)
t = plt.title('The Orion-Eridanus Superbubble', size=25)
t.set_y(1.04)

plt.xlabel(r'$l$', size = 24)
plt.ylabel(r'$b$', size = 24)

cb = plt.colorbar()
cb.set_label('Column Density ' + r'$[cm^{2}]$', size = 23)

plt.tick_params(axis='x',labelbottom='off',labeltop='on')
plt.xlim([160,220])
plt.ylim([-70,-10])

pp = []
bb = np.linspace(-70., -10., 7.)
for m in np.linspace(160,222,7.):
    for i in bb:
        pp.append((190-(190-m)*np.cos(i*np.pi/180.)))
    plt.plot(pp,bb, color='k')
    pp = []

for i in bb:
    plt.axhline(y = i, color='k')

plt.show()
