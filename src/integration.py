import numpy as np



def trapezoid(x, f, T_index, N):

    time_T = x[:T_index + 1]
    vel_T = f[:T_index + 1]

    dx = (time_T[-1] - time_T[0]) / N
    vel_squared = vel_T ** 2

    integral = 0.5 * dx * (vel_squared[0] + np.sum(vel_squared[1:N-1]) + vel_squared[-1])

    return integral

def simpson(x, f, T_index, N):


    time_T = x[:T_index + 1]
    vel_T = f[:T_index + 1]

    dx = (time_T[-1] - time_T[0]) / N
    vel_squared = vel_T ** 2

    integral = (1/3) * dx * (vel_squared[0] + 4*(np.sum(vel_squared[1:N - 1:2])) + 2*(np.sum(vel_squared[2:N - 1:2])) + vel_squared[-1])
    return integral


def integrate_newton(x, f, alg):

    max_velocity = np.max(np.abs(f))
    threshold = 0.005 * max_velocity
    N = len(np.where(np.abs(f) > threshold)[0])
    T_index = np.where(np.abs(f) > threshold)[0][-1]

    if alg == 'trap':
       integral = trapezoid(x, f, T_index, N)
       return integral

    if alg == 'simp':
        integral = simpson(x, f, T_index, N)
        return integral




