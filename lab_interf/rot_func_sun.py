import numpy as np
import matplotlib.pyplot as plt
import ephem
import time

def convert():

    obs = ephem.Observer()

    obs.lat = 37.8732*np.pi/180.

    obs.long = -122.2573*np.pi/180.

    obs.date = ephem.now()

    lst = float(obs.sidereal_time()) ## local sidereal time

    sun = ephem.Sun()
    sun.compute(obs)

## Defining the matrices

    R_x=np.zeros_like(np.empty([3,3]))

    R_y=np.zeros_like(np.empty([3,3]))

    R_z=np.zeros_like(np.empty([3,3]))

## Building Coordinates

    t_l = 37.8732*np.pi/180.  ## terrestrial latitude

## Rotation for ra, dec -> ha, dec (1)

    R_x[0,0]= np.cos(lst)
    R_x[1,0]= -np.sin(lst)
    R_x[2,0]= 0.

    R_x[0,1]= np.sin(lst)
    R_x[1,1]= np.cos(lst)
    R_x[2,1]= 0.

    R_x[0,2]= 0.
    R_x[1,2]= 0.
    R_x[2,2]= 1.

## Rotation for ra, dec -> ha, dec (2)

    R_y[0,0]= 1.
    R_y[1,0]= 0.
    R_y[2,0]= 0.

    R_y[0,1]= 0.
    R_y[1,1]= -1.
    R_y[2,1]= 0.

    R_y[0,2]= 0.
    R_y[1,2]= 0.
    R_y[2,2]= 1.

## Rotation for ha, dec -> az, alt

    R_z[0,0]= -np.sin(t_l)
    R_z[1,0]= 0.
    R_z[2,0]= np.cos(t_l)

    R_z[0,1]= 0.
    R_z[1,1]= -1.
    R_z[2,1]= 0.

    R_z[0,2]= np.cos(t_l)
    R_z[1,2]= 0.
    R_z[2,2]= np.sin(t_l)

## Building the Rotation Matrices

# From ra, dec -> ha, dec:

    R_ra_ah = np.dot(R_y,R_x)

# From ha, dec -> az, alt

    R_ah_az = R_z

##### Working with input ######

    #x = ra*np.pi/180.
    #y = dec*np.pi/180.

    x = float(sun.ra) # For the sun.ra, already in radians
    y = float(sun.dec) # For the sun.dec, already in radians

    M = np.array([0.,0.,0.], dtype=float)
    M[0] = np.cos(y)*np.cos(x)
    M[1] = np.cos(y)*np.sin(x)
    M[2] = np.sin(y)

    Rot_1 = np.dot(R_ra_ah,M) # First Rotation
    Rot_2 = np.dot(R_ah_az,Rot_1) # Second Rotation
    
    az = np.arctan2(Rot_2[1],Rot_2[0])

    alt = np.arcsin(Rot_2[2])
    
    #return sun.compute(obs)

    if az < 0.:
        return np.arctan2(Rot_2[1],Rot_2[0]) +2*np.pi, alt
    else:
        return az, alt
