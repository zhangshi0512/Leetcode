def quick_sort(A, start=0, end=None, step=0):
    # If end is None, set it to the last index of the array
    if end is None:
        end = len(A) - 1

    # Only proceed if the array has more than one element
    if start < end:
        # Partition the array and get the pivot's final position
        pivot_index, step = partition(A, start, end, step)
        # Recursively apply Quick Sort to the sub-array to the left of the pivot
        step = quick_sort(A, start, pivot_index - 1, step + 1)
        # Recursively apply Quick Sort to the sub-array to the right of the pivot
        step = quick_sort(A, pivot_index + 1, end, step + 1)
    return step


def partition(A, start, end, step):
    # Choose the last element as the pivot
    pivot = A[end]
    # 'i' pointer is used to track the "wall" - the boundary between elements less than the pivot and greater than the pivot
    i = start - 1

    # Iterate over each element in the array with 'j' pointer
    for j in range(start, end):
        # Determine the reason for the action based on the comparison with the pivot
        reason = f"{A[j]} <= {pivot}" if A[j] <= pivot else f"{A[j]} > {pivot}"
        # Default action is "Move" if the element is less than or equal to the pivot, otherwise "No Swap"
        action = "Move" if A[j] <= pivot else "No Swap"
        # If the current element is less than or equal to the pivot, swap it with the element at 'i + 1'
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
            # Update the action to "Swap" if a swap occurred
            action = f"Swap A[{i}] and A[{j}]"
        # Log the current step
        step = print_state(A, i, j, end, step, action, reason)

    # After all elements have been compared with the pivot, place the pivot in its correct position
    action = f"Pivot Swap A[{i + 1}] and A[{end}]"
    reason = f"Place pivot {pivot} in correct position"
    A[i + 1], A[end] = A[end], A[i + 1]
    # Log the pivot swap step
    step = print_state(A, i + 1, end - 1, end, step, action, reason)
    return i + 1, step


def print_state(A, i, j, p, step, action, reason):
    array_str = ' '.join([f'{num:2}' for num in A])
    i_str = ' ' * (3 * max(i, 0) + 1) + 'i'
    j_str = ' ' * (3 * j + 1) + 'j' if j >= 0 else ''
    p_str = ' ' * (3 * p + 1) + 'p'

    print(f"Step {step}: {reason}, {action}")
    print(i_str)
    print(array_str)
    print(j_str)
    print(p_str)
    print('-' * len(array_str))
    return step + 1


# Example usage
A = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]
B = [8, 3, 5, 7, 2, 4]
final_step = quick_sort(B)
print("Sorted array:", ' '.join(str(x) for x in B))
print(f"Total steps: {final_step}")
