# This program is to check whether the array is sorted or not

def is_array_in_sorted_order(A):
    if len(A) == 1:
        return True
    return A[0] <= A[1] and is_array_in_sorted_order(A[1:])


A=[123,235,566,768,897,975,989]
print(is_array_in_sorted_order(A))