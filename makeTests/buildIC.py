import numpy as np
from pytipsy import wtipsy
import pynbody as pyn
import math

glass = pyn.load('./glass16.std')
sphere = pyn.load('./sphere001.std')

ng = len(glass.g) * 8 + len(sphere.g)
print ng
ns = 2

gx = np.zeros(ng)
gy = np.zeros(ng)
gz = np.zeros(ng)
sx = np.zeros(ns)
sy = np.zeros(ns)
sz = np.zeros(ns)

for a in range(0,2):
    for b in range(0, 2):
        for c in range(0, 2):
            for i in range (0, len(glass.g)):
                gx[len(glass.g) * (c + b * 2 + a * 4) + i] = (glass.g['x'][i] - 0.5 + 1.0 * a) / 2
                gy[len(glass.g) * (c + b * 2 + a * 4) + i] = (glass.g['y'][i] - 0.5 + 1.0 * b) / 2
                gz[len(glass.g) * (c + b * 2 + a * 4) + i] = (glass.g['z'][i] - 0.5 + 1.0 * c) / 2

for i in range(len(glass.g) * 8, ng):
    gx[i] = sphere.g['x'][i-len(glass.g)* 8] / 2
    gy[i] = sphere.g['y'][i-len(glass.g)* 8] / 2
    gz[i] = sphere.g['z'][i-len(glass.g)* 8] / 2
    
sx[0] = 0.01414
sy[0] = 0.01414
sz[0] = 0.01414

sx[1] = -0.01414
sy[1] = -0.01414
sz[1] = -0.01414

header = {'time':0, 
          'n':ng+ns,
          'ndim':3, 
          'ngas':ng, 
          'ndark':0, 
          'nstar':ns}

gas_particles = {'mass':(np.ones(ng)/(8*len(glass.g))), 
                 'x':gx, 'y':gy,'z':gz,
                 'vx':np.zeros(ng),'vy':np.zeros(ng),'vz':np.zeros(ng),
                 'dens':np.zeros(ng), 
                 'tempg':np.ones(ng),
                 'h':np.zeros(ng), 
                 'phi':np.zeros(ng),
                 'eps':np.ones(ng),
                 'zmetal':np.zeros(ng)}

star_particles = {'mass':(np.ones(ns)), 
                 'x':sx, 'y':sy,'z':sz,
                 'vx':np.zeros(ns),'vy':np.zeros(ns),'vz':np.zeros(ns),
                 'tform':np.ones(ns),
                 'phi':np.zeros(ns), 
                 'eps':np.ones(ns),
                 'metals':np.ones(ns)}

wtipsy('./glass16_001_sphere.std',header,gas_particles,[],star_particles)