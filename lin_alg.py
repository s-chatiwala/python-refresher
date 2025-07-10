import numpy as np 

class ProblemSet:
    def __init__(self, a, b):
            self.a = a
            self.b = b    
         
def sum_vector(a, b):
    """Find the sum of both vectors. """
    return np.add(a,b)  

def diff_vector(a, b):
    """ Find the difference of both vectors."""
    return np.subtract(a,b)

def sum_matrix(a, b):
    """ Find the sum of the matrix. """
    return np.add(a,b)

def diff_matrix(a, b):
    """ Find the difference of both matrices."""
    return np.subtract(a,b)

def dot_product_arrays(a, b):
    """ Find the dot product of arrays a and b. """
    return np.dot(a, b)

def dot_product_matrices(a, b):
    """Find the dot product of matrices a and b."""
    return np.dot(a, b)

def mag_vector(a):
    """Find the magnitude of vector a"""
    return np.linalg.norm(a)

def trans_matrix(a):
    """Find the transpose of matrix a."""
    return np.transpose(a)