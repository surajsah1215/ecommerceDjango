
cpdef int sum_of_squares(int n):
    cdef int i
    cdef int result = 0
    for i in range(n):
        result += i * i
    return result
