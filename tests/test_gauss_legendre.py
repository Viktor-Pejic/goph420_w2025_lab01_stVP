import scipy.integrate
import numpy as np
from goph420_lab01.integration import integrateGauss

def main():
    def f(x):
        return np.sin(x) + np.cos(x)

    lims = [0, np.pi]
    npts = 5

    result = integrateGauss(f, lims, npts)
    expectedResult, _ = scipy.integrate.fixed_quad(f, lims[0], lims[1], n=npts)

    print("------------Testing Gauss Quadrature Integration----------")
    print(f"Calculated Result = {result}")
    print(f"Scipy result = {expectedResult}")
    print(f"Error between calculated and Scipy result = {(expectedResult - result) / expectedResult:.5f}")

if __name__ == '__main__':
    main()

