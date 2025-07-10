import unittest
import lin_alg
import numpy as np 
import math

class TestProblemSet(unittest.TestCase):
    def test_sum_vector(self):
        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])
        self.assertEqual(lin_alg.sum_vector(a, b).all(), np.array([5, 7, 9]).all())

    def test_diff_vector(self):
        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])
        self.assertEqual(lin_alg.diff_vector(a, b).all(), np.array([-3, -3, -3]).all())

    def test_sum_matrix(self):
        a = np.array([[1, 2], [3, 4]])
        b = np.array([[5, 6], [7, 8]])
        self.assertEqual(lin_alg.sum_matrix(a, b).all(), np.array([[6, 8], [10, 12]]).all())

    def test_diff_matrix(self):
        a = np.array([[1, 2], [3, 4]])
        b = np.array([[5, 6], [7, 8]])
        self.assertEqual(lin_alg.diff_matrix(a,b).all(), np.array([[-4, -4], [-4, -4]]).all())
    
    def test_dot_product_arrays(self):
        a = np.array([1, 2, 3])
        b = np.array([ 4, 5, 6])
        self.assertEqual(lin_alg.dot_product_arrays(a,b), 32)
    
    def test_dot_product_matrices(self):
        a = np.array([[1, 2, 3], [4, 5, 6]])
        b = np.array([[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]])
        self.assertEqual(lin_alg.dot_product_matrices(a,b).all(), np.array([[74, 80, 86, 88], [173, 188, 203, 218]]).all())
    
    def test_mag_vector(self):
        a = np.array([1, 1, 2])
        self.assertEqual(lin_alg.mag_vector(a), math.sqrt(6))

    def test_trans_matrix(self):
        a = np.array([[1, 2], [3, 4]])
        self.assertEqual(lin_alg.trans_matrix(a).all(), np.array([[1, 3], [2, 4]]).all())

if __name__ == "__main__":
    unittest.main()