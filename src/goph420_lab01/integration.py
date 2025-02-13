import numpy as np

def integrate_newton(x, f, alg='trap'):
    x = np.array(x)
    f = np.array(f)

    if x.shape != f.shape:
        raise ValueError('x and f must have the same shape')

    N = len(x) - 1 #number of intervals
    dx = (x[-1] - x[0]) / N

    if alg.strip().lower() == 'trap':

        sum = np.sum(f[1:-1])

        integral = (dx/2) * (f[0] + 2*sum + f[-1])

        return integral

    if alg.strip().lower() == 'simp':
        #If number of points is odd, perform 1/3 rule
        if (N + 1) % 2 == 1:
            integral = (1 / 3) * dx * (f[0] +
                                        4 * (np.sum(f[1:-1:2])) +
                                        2 * (np.sum(f[2:-2:2])) +
                                        f[-1])
            return integral

        else:
            #If number of points are even, perform 3/8 rule once with 4 points then
            #perform 1/3 rule for remaining points and sum
            integral = 0.375 * dx * (f[0] + (3 * f[1]) + (3 * f[2]) + f[3])

            integral += (1 / 3) * dx * (f[3] +
                                       4 * (np.sum(f[4:-1:2])) +
                                       2 * (np.sum(f[5:-2:2])) +
                                       f[-1])

            return integral
    else:
        raise ValueError("Algorithm type must be trap or simp")


def integrate_gauss(f, lims, npts = 3):

    if not callable(f):
        raise TypeError('f is not callable')

    if len(lims) != 2:
        raise ValueError('lims must only contain 2 elements')

    try:
        float(lims[0])
        float(lims[1])
    except ValueError:
        raise ValueError('lims elements must be convertible to a float')

    if npts not in [1,2,3,4,5]:
        raise ValueError('npts must be an integer between 1 and 5')

    #Generate the nodes and weights for the corresponding n
    x_i, c_i = np.polynomial.legendre.leggauss(npts)

    #Assign integration limits
    a, b = lims

    #Change of variable from [a,b] to [-1,1]
    x = 0.5*(b + a) + (0.5*(b - a) * x_i)
    c = 0.5*(b - a) * c_i

    integral = np.sum(c * f(x))

    return integral





