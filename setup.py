# do: python3 setup.py build_ext --inplace
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
from os import system
from numpy import get_include

# compile fortran without linking
fortran_mod_comp = 'gfortran functions_to_minimize.f90 -c -o functions_to_minimize.o -O3 -fPIC'
print(fortran_mod_comp)
system(fortran_mod_comp)
# shared_obj_comp = 'gfortran pyfunctions_to_minimize.f90 -c -o pyfunctions_to_minimize.o -O3 -fPIC'
# print(shared_obj_comp)
# system(shared_obj_comp)

ext_modules = [Extension(# module name:
                            'pyfunctions_to_minimize',
                            # source file:
                            ['pyfunctions_to_minimize.pyx'],
                            # other compile args for gcc
                            extra_compile_args=['-fPIC', '-O3'],
                            # other files to link to
                            extra_link_args=['functions_to_minimize.o'])]

setup(name = 'pyfunctions_to_minimize',
      cmdclass = {'build_ext': build_ext},
      include_dirs = [get_include()],
      ext_modules = ext_modules)

setup(ext_modules=cythonize("pyfunctions_to_minimize.pyx"))
