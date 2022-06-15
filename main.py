import numpy as np

from PhysFunctions import *


basic = np.array([1,2,3])


allNew = FnCoulombsLaw(0.005,0.10,5)
print(allNew)

print(DiPoleTorque(basic, [5,6,3]))
