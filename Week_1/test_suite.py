import unittest
import numpy as np
import Week_1.adils_function as adils_function
        
class TestLineFit(unittest.TestCase):
    def test_arrays_exist(self):
        # assert that both months and sales are numpy arrays
        self.assertTrue(isinstance(adils_function.months1, np.ndarray) and isinstance(adils_function.sales1, np.ndarray))
