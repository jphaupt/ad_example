module functions_to_minimize
    use iso_fortran_env, only: rp => real64
    use iso_c_binding, only: c_double, c_int
    implicit none

  contains

    subroutine example_function(x, n, result)
        integer, intent(in) :: n
        real(rp), intent(in) :: x(n) ! need explicit size
        real(rp), intent(out) :: result
        integer :: i
        result = 0.0
        do i = 1, size(x)
            result = result + x(i)**2
        end do
    end subroutine example_function

    subroutine example_function_interface(x, n, result) bind(c)
        integer(c_int), intent(in) :: n
        real(c_double), intent(in) :: x(n)
        real(c_double), intent(out) :: result
        call example_function(x, n, result)
    end subroutine example_function_interface

end module functions_to_minimize
