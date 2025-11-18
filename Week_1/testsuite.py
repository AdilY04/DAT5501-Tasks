import unittest
import numpy as np
import adilsfunction
        
class TestLineFit(unittest.TestCase):
    def test_arrays_exist(self):
        # assert that both months and sales are numpy arrays
        self.assertTrue(isinstance(adilsfunction.months1, np.ndarray) and isinstance(adilsfunction.sales1, np.ndarray))
