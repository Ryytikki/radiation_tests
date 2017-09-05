from pytipsy import rtipsy
import pynbody as pyn
import matplotlib.pyplot as plt
import numpy as np

# First we make the basic spheres

nBase = 4096        # Number of gas particles in the base glass
mass = 1/nBase      # Mass of each gas particle
tau = 4             # Intended optical depth of the sphere

sphereX = [[],[]]
sphereY = [[],[]]
sphereZ = [[],[]]

# 0.1 diameter sphere
rho = tau / 0.1 - 1
nSphere = np.floor(nBase * ((4./3.) * np.pi * 0.1) * rho)

radius = np.power(np.random.uniform(0.0, 0.1, (nSphere, 1)), 1/3.)
theta = np.random.uniform(0.0, 1.0, (nSphere, 1)) * np.pi
phi = np.random.uniform(0.0, 1.0, (nSphere, 1)) * 2 * np.pi

sphereX[0] = radius * np.sin(theta) * np.cos(phi)
sphereY[0] = radius * np.sin(theta) * np.sin(phi)
sphereZ[0] = radius * np.cos(theta)

header = {'time':0, 
          'n':nSphere,
          'ndim':3, 
          'ngas':ng, 
          'ndark':0, 
          'nstar':0}

gas_particles = {'mass':(np.ones(nSphere) * mass), 
                 'x':sphereX[0], 'y':sphereY[0],'z':sphereZ[0],
                 'vx':np.zeros(nSphere),'vy':np.zeros(nSphere),'vz':np.zeros(nSphere),
                 'dens':np.zeros(nSphere), 
                 'tempg':np.ones(nSphere),
                 'h':np.zeros(nSphere), 
                 'phi':np.zeros(nSphere),
                 'eps':np.ones(nSphere),
                 'zmetal':np.zeros(nSphere)}

wtipsy(wdir + 'sphere01.std',header,gas_particles,[],[])


# 0.01 radius sphere
rho = tau / 0.01 - 1
nSphere = np.floor(nBase * ((4./3.) * np.pi * 0.01) * rho)

radius = np.power(np.random.uniform(0.0, 0.01, (nSphere, 1)), 1/3.)
theta = np.random.uniform(0.0, 1.0, (nSphere, 1)) * np.pi
phi = np.random.uniform(0.0, 1.0, (nSphere, 1)) * 2 * np.pi

sphereX[0] = radius * np.sin(theta) * np.cos(phi)
sphereY[0] = radius * np.sin(theta) * np.sin(phi)
sphereZ[0] = radius * np.cos(theta)

header = {'time':0, 
          'n':nSphere,
          'ndim':3, 
          'ngas':ng, 
          'ndark':0, 
          'nstar':0}

gas_particles = {'mass':(np.ones(nSphere) * mass), 
                 'x':sphereX[1], 'y':sphereY[1],'z':sphereZ[1],
                 'vx':np.zeros(nSphere),'vy':np.zeros(nSphere),'vz':np.zeros(nSphere),
                 'dens':np.zeros(nSphere), 
                 'tempg':np.ones(nSphere),
                 'h':np.zeros(nSphere), 
                 'phi':np.zeros(nSphere),
                 'eps':np.ones(nSphere),
                 'zmetal':np.zeros(nSphere)}

wtipsy(wdir + 'sphere001',header,gas_particles,[],[])