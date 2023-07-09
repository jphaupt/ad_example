import pyfunctions_to_minimize as f
import numpy as np
x = np.asarray([3,2], dtype='float64')
out = f.example_function_wrapper(x)
print(np.abs(out - 13.0) < 1.e-10)
