def fibonacci_2(n, ht={0: 0, 1: 1}):
    if n in ht:
        return ht[n]
    else:
        ht[n] = fibonacci_2(n - 1, ht) + fibonacci_2(n - 2, ht)
        return ht[n]


print(fibonacci_2(4))
