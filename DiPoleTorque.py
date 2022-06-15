import numpy as np


def DiPoleTorque(vecDipoleMomentP, vecElectricField):
    return np.cross(vecDipoleMomentP, vecElectricField)
