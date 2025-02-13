import unittest
from goph420_lab01.integration import integrateGauss



class TestGaussLegendreIntegration(unittest.TestCase):

    def test_polynomial_exactness(self):
        """
        Test integration of gauss quadrature integration for
        polynomials with degree = 2n - 1 up to degree 9.
        """

        # Define polynomials of different degrees
        #npts = (degree + 1) / 2 rounded up
        poly_funcs = [
            (lambda x: x**0, 1, 0),
            (lambda x: x, 2, 1),
            (lambda x: x**2, 2, 2),
            (lambda x: x**3, 3, 3),
            (lambda x: x**4, 3, 4),
            (lambda x: x**5, 4, 5),
            (lambda x: x**6, 4, 6),
            (lambda x: x**7, 5, 7),
            (lambda x: x**8, 5, 8),
            (lambda x: x**9, 5, 9),
        ]

        lims = [-1, 1]  # Integration limits

        for f, npts, degree in poly_funcs:
            result = integrateGauss(f, lims, npts)
            expected = (lims[1]**(degree + 1) - lims[0]**(degree + 1)) / (degree + 1)  # Exact integral
            self.assertAlmostEqual(result, expected, places=10,
                msg=f"Failed for polynomial of degree {npts}")

if __name__ == '__main__':
    unittest.main()