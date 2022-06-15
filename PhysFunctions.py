import numpy as np


def DiPoleTorque(vecDipoleMomentP, vecElectricField):
    return np.cross(vecDipoleMomentP, vecElectricField)


def FnCoulombsLaw(chargeOne, chargeTwo, radiusR):
    KVALUE = 8.99 * np.power(10, 9)

    force = (KVALUE * (chargeOne * chargeTwo)) / np.power(radiusR, 2)

    return force

    # force = k*q1*q2/r^2

