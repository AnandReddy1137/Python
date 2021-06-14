def k_strings(n, k):
    if n == 0: return []
    if n == 1: return k

    return [digit + bitstring for digit in k_strings(1, k) for bitstring in k_strings(n - 1, k)]


print(k_strings(5, ['a', 'b', 's']))
