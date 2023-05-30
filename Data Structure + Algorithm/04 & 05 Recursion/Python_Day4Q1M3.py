def fibonacci_3(n):
    if n<=1: return n
    prev = 0
    curr = 1
    counter =1
    while counter < n:
        next = prev + curr
        counter +=1
        prev = curr
        curr = next
    return curr


print(fibonacci_3(5))
