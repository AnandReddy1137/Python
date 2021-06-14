# This is to solve math recursive functions having tree kind of equations
# Ex:   T(n)=2T(n-1)+2^n where n is an integer >=1


def Math_eq(n):
    if n <= 1: return 1
    return 2*Math_eq(n-1)+pow(2,n)

print(Math_eq(2))