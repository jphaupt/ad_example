module functions_to_minimize
    use iso_fortran_env, only: rp => real64
    implicit none

  contains

    subroutine example_function(x, result)
      real(rp), intent(in) :: x(:)
      real(rp), intent(out) :: result
      integer :: i
      result = 0.0
      do i = 1, size(x)
        result = result + x(i)**2
      end do
    end subroutine example_function

end module functions_to_minimize
