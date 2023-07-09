# this might help fix this broken code:
# https://stackoverflow.com/questions/22404060/fortran-cython-workflow
cimport cython

cdef extern from "functions_to_minimize.f90" nogil:
    cdef void example_function(double[:] x, double* result)

@cython.boundscheck(False)
def example_function_wrapper(x):
    cdef double result
    example_function(x, &result)
    return result
