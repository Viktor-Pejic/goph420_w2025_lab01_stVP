import numpy as np
import matplotlib.pyplot as plt
from goph420_lab01.integration import integrate_newton

def main ():
    s_wave = np.loadtxt("data/s_wave_data.txt", dtype='float')

    time = s_wave[:, 0]
    velocity = s_wave[:, 1]

    #Create end point for the data
    max_velocity = np.max(np.abs(velocity))
    threshold = 0.005 * max_velocity
    T_index = np.where(np.abs(velocity) > threshold)[0][-1]

    dt = []
    rel_err_trap = []
    rel_err_simp = []

    #Evaluate integrals for different interval lengths
    x = time[:T_index]
    f = velocity[:T_index]
    int_trap_1 = integrate_newton(x, f, alg='trap')
    int_simp_1 = integrate_newton(x, f, alg='simp')

    x_2 = x[0:T_index:2]
    f_2 = f[0:T_index:2]
    int_trap_2 = integrate_newton(x_2, f_2, alg='trap')
    int_simp_2 = integrate_newton(x_2, f_2, alg='simp')

    x_3 = x[0:T_index:4]
    f_3 = f[0:T_index:4]
    int_trap_3 = integrate_newton(x_3, f_3, alg='trap')
    int_simp_3 = integrate_newton(x_3, f_3, alg='simp')

    x_4 = x[0:T_index:8]
    f_4 = f[0:T_index:8]
    int_trap_4 = integrate_newton(x_4, f_4, alg='trap')
    int_simp_4 = integrate_newton(x_4, f_4, alg='simp')

    x_5 = x[0:T_index:16]
    f_5 = f[0:T_index:16]
    int_trap_5 = integrate_newton(x_5, f_5, alg='trap')
    int_simp_5 = integrate_newton(x_5, f_5, alg='simp')

    #Evaluate the relative error
    err_1_trap = abs((int_trap_4 - int_trap_5)/int_trap_4)
    err_1_simp = abs((int_simp_4 - int_simp_5)/int_simp_4)
    rel_err_trap.append(err_1_trap)
    rel_err_simp.append(err_1_simp)
    dt.append(x_4[1] - x_4[0])

    err_2_trap = abs((int_trap_3 - int_trap_4)/int_trap_3)
    err_2_simp = abs((int_simp_3 - int_simp_4)/int_simp_3)
    rel_err_trap.append(err_2_trap)
    rel_err_simp.append(err_2_simp)
    dt.append(x_3[1] - x_3[0])

    err_3_trap = abs((int_trap_2 - int_trap_3)/int_trap_2)
    err_3_simp = abs((int_simp_2 - int_simp_3)/int_simp_2)
    rel_err_trap.append(err_3_trap)
    rel_err_simp.append(err_3_simp)
    dt.append(x_2[1] - x_2[0])

    err_4_trap = abs((int_trap_1 - int_trap_2)/int_trap_1)
    err_4_simp = abs((int_simp_1 - int_simp_2)/int_simp_1)
    rel_err_trap.append(err_4_trap)
    rel_err_simp.append(err_4_simp)
    dt.append(x[1] - x[0])

    plt.loglog(dt, rel_err_trap, label='trap')
    plt.loglog(dt, rel_err_simp, label='simp')
    plt.title("Error vs. Sample Interval Length")
    plt.xlabel("dt")
    plt.ylabel("error")
    plt.legend()
    plt.grid()
    plt.savefig("figures/Trap_Simp_Convergence_Plot.png")

if __name__ == "__main__":
    main()