import matplotlib.pyplot as plt
import numpy as np
from goph420_lab01.integration import integrateGauss


def prob_magnitude():
    """
        Uses standard normal probability density equation to find the
        probability that an earthquake of magnitude greater than 4 occurs

        """

    #Data points of magnitudes greater than 4
    x = np.linspace(4.1, 10, 100)
    mean = 1.5
    stdev = 0.5

    z = (x - mean) / stdev

    lims = [0, np.max(z)]

    def f(z):
        return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * z ** 2)

    probability = integrateGauss(f, lims, npts=3)

    print(f"Probability that an earthquake with magnitude > 4 occurs: {probability}")

def prob_trueValue():
    """
    Compute the convergence of the probability that the true value lands
    between 10.25 and 10.35 using Gauss-Legendre quadrature.
    """

    sample_sizes = [100, 50, 25, 13]

    mean = 10.28
    stError = 0.05

    # Compute standard deviations for different sample sizes
    stdevs = []
    for i in sample_sizes:
        stdevs.append(stError * np.sqrt(i))

    # Integration limits
    a, b = 10.25, 10.35

    def f(z):
        return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * z**2)

    # Compute probabilities
    convergence = []
    for stDeviation in stdevs:
        lims = [(a - mean) / stDeviation, (b - mean) / stDeviation]
        probability = integrateGauss(f, lims, npts=3)
        convergence.append(probability)
    return sample_sizes, convergence


def plotConvergence():
    sample_sizes, convergence = prob_trueValue()

    plt.loglog(sample_sizes, convergence)
    plt.xlabel("Sample Size (N)")
    plt.ylabel("Estimated Probability")
    plt.title("Convergence of Probability that\n10.25 < True Value < 10.35")
    plt.grid()
    plt.tight_layout()

    plt.savefig("figures/True_Value_Convergence.png")

if __name__ == '__main__':
    plotConvergence()
    prob_magnitude()