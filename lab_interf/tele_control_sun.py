import numpy as np
import matplotlib.pyplot as plt
import ephem
import time
import radiolab as rlb
import rot_func_sun
import threading
from threading import Thread


n = input('End of observation hour (24h-format): ')
t = time.localtime()[4]+time.localtime()[5]/60.

if n - t > 0:
    t_s = (n-time.localtime()[3])*3600 + (60- time.localtime()[4])*60. 
else:
    t_s = (24-time.localtime()[3]+n)*3600 + (60- time.localtime()[4])*60. 


def rec():

    rlb.recordDVM(filename='sun.npz', recordLength=t_s)


def track():

    while time.localtime()[3] < n+7:

        if time.localtime()[4]+time.localtime()[5]/60. == t:
            print 'Home! - at ' +  str(time.localtime()[3]) + ':' + str(time.localtime()[4])
            rlb.pntHome
            rlb.pntTo(rot_func_sun.convert()[1]*180./np.pi, rot_func_sun.convert()[0]*180./np.pi)

            time.sleep(30)
            rlb.pntTo(rot_func_sun.convert()[1]*180./np.pi, rot_func_sun.convert()[0]*180./np.pi)

            time.sleep(30)
            rlb.pntTo(rot_func_sun.convert()[1]*180./np.pi, rot_func_sun.convert()[0]*180./np.pi)

        else:
            time.sleep(30)
            rlb.pntTo(rot_func_sun.convert()[1]*180./np.pi, rot_func_sun.convert()[0]*180./np.pi)


rec = threading.Thread(target=rec)
track = threading.Thread(target=track)

track.daemon = True

rec.start()
track.start()

rec.join()
