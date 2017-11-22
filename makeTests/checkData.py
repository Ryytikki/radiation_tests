from pytipsy import rtipsy
import pynbody as pyn
import matplotlib.pyplot as plt
import numpy as np
import sys

h,g,d,s = rtipsy(sys.argv[1] + ".std")

plt.scatter(g["x"], g["y"])
plt.show()
