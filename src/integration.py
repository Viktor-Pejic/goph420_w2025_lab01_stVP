import numpy as np

def integrate_newton(x, f, alg='trap'):

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
            integral = ((1 / 8) * ((f[3] - f[0]) / 3) *
                                   (f[0] + (3 * f[1]) + (3 * f[2]) + f[3]))

            integral += (1 / 3) * dx * (f[3] +
                                       4 * (np.sum(f[4:-1:2])) +
                                       2 * (np.sum(f[5:-2:2])) +
                                       f[-1])

            return integral





