import numpy as np
from pytipsy import rtipsy
import matplotlib.pyplot as plt
import pynbody as pyn


posThin = pyn.load("glass16_001_sphere.000000")
#posThin.g = posThin.g[np.where(np.abs(posThin.g['z']) < 1)]

fluxThin = posThin.g['flux']
xThin = posThin.g['x']
yThin = posThin.g['y']
zThin = posThin.g['z']

sxThin = posThin.s['x'][0]
syThin = posThin.s['y'][0] 
szThin = posThin.s['z'][0]

rThin = np.sqrt((posThin.g['x']-sxThin)**2+(posThin.g['y']-syThin)**2+(posThin.g['z']-szThin)**2)
y_dotThin = 100 * np.exp(-1 * rThin) / (4 * 3.1415926 * rThin * rThin) 

plt.scatter(xThin, yThin, c=np.log10(fluxThin/y_dotThin),s=50,edgecolors='none', marker = '.')#, cmap = 'cubehelix')
plt.colorbar(label=r"$\log(\left|F_{\rm test}/F_{\rm uniform}\right|)$")
plt.scatter(sxThin,syThin, marker = "*", c = "yellow", s = 500)
plt.xlabel("x")
plt.ylabel("y")


plt.gcf().set_size_inches(24,24)

plt.show()