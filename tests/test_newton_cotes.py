from src.integration import integrate_newton
import numpy as np


def test_trap():
    x = np.linspace(-2, 6) #even data points
    x2 = np.linspace(-2,6, len(x) + 1) #odd data points
    f1 = 2*(x) #linear
    f2 = np.full(len(x), 5) #constant
    f3 = 3 * x ** 2 #quadratic
    f4 = 3 * x2 ** 2

    #expected value of integral
    i1 = (6**2) - ((-2)**2)
    i2 = 8 * 5
    i3 = (6**3) - ((-2)**3)

    int1_actual = integrate_newton(x, f1, alg = 'trap')
    int2_actual = integrate_newton(x, f2, alg = 'trap')
    int3_actual = integrate_newton(x, f3, alg = 'simp')
    int4_actual = integrate_newton(x2, f4, alg = 'simp')


    print("-------Testing trapezoid integration-------")
    print(f"Linear function expected value: {i1}")
    print(f"Linear function actual value: {int1_actual}")
    print(f"relative error: {(i1-int1_actual)/i1:.4f}")
    print()
    print(f"Constant function expected value: {i2}")
    print(f"Constant function actual value: {int2_actual}")
    print(f"relative error: {(i2-int2_actual)/i2:.4f}")
    print()
    print("--------Testing simpson integration-------")
    print(f"Quadratic function expected value: {i3}")
    print(f"Quadratic function actual using even data points value: {int3_actual}")
    print(f"Quadratic function actual using odd data points value: {int4_actual}")
    print(f"relative error using even data points: {(i3-int3_actual)/i3:.4f}")
    print(f"relative error using odd data points: {(i3-int4_actual)/i3:.4f}")
test_trap()
