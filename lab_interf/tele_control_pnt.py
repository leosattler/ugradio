import numpy as np
import matplotlib.pyplot as plt
import ephem
import time
import radiolab as rlb
import rot_func_pnt
import threading
from threading import Thread

#################################
# Leonardo Sattler Cassara
# Telescope Control - Point Source
#################################

n = input('End of observation hour (24h-format): ')
t = time.localtime()[4]+time.localtime()[5]/60.

if n - t > 0:
    t_s = (n-time.localtime()[3])*3600 - time.localtime()[4])*60. 
else:
    t_s = (24-time.localtime()[3]+n)*3600 - time.localtime()[4])*60. 


def rec():

    rlb.recordDVM(filename='pnt.npz', recordLength=t_s)


def track():

    if time.localtime()[4]+time.localtime()[5]/60. == t:
        print 'Home! - at ' +  str(time.localtime()[3]) + ':' + str(time.localtime()[4])
        rlb.pntHome()
        rlb.pntTo(rot_func_pnt.convert()[1]*180./np.pi, rot_func_pnt.convert()[0]*180./np.pi)

        time.sleep(30)
        rlb.pntTo(rot_func_pnt.convert()[1]*180./np.pi, rot_func_pnt.convert()[0]*180./np.pi)

        time.sleep(30)
        rlb.pntTo(rot_func_pnt.convert()[1]*180./np.pi, rot_func_pnt.convert()[0]*180./np.pi)

    else:
        time.sleep(30)
        rlb.pntTo(rot_func_pnt.convert()[1]*180./np.pi, rot_func_pnt.convert()[0]*180./np.pi)


rec = threading.Thread(target=rec)
track = threading.Thread(target=track)

track.daemon = True

rec.start()
track.start()

rec.join()
