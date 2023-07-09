# this might help fix this broken code:
# https://stackoverflow.com/questions/22404060/fortran-cython-workflow
cimport cython
cimport numpy as np

cdef extern from "functions_to_minimize.h":
    void example_function_interface(double* x, int* n, double* result)

def example_function_wrapper(np.ndarray[np.float64_t, ndim=1] x):
    cdef double result
    cdef int n = x.size
    example_function_interface(<double*> x.data, &n, &result)
    return result
