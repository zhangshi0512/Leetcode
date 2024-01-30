def counting_sort(A):
    # Step 1: Initialize C with size max(A) + 1
    k = max(A) + 1
    C = [0] * k
    B = [0] * len(A)
    print(f'Given: A = {A}')
    print(f'Maximum value in A: {max(A)}, Length for C: len(C) = {k}')
    print(f'Initializing: C = {C}')
    print(f'Initializing: B = {B}')

    # Step 2: Count each element
    for j in range(len(A)):
        C[A[j]] += 1
    print(f'After counting: C = {C}')

    # Step 3: Cumulative sum in C
    for i in range(1, k):
        C[i] = C[i] + C[i - 1]
    print(f'After cumulative sum: C = {C}')

    # Step 4: Place elements in B
    for j in reversed(range(len(A))):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1
        print(f'Placing {A[j]}: B = {B}, C = {C}')

    return B


A = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
sorted_A = counting_sort(A)
print(f'Sorted array: {sorted_A}')
