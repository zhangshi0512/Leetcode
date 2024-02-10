import csv


def quick_sort(A, start=0, end=None, log=None, step=0):
    if end is None:
        end = len(A) - 1
    if start < end:
        pivot_index, step = partition(A, start, end, log, step)
        step = quick_sort(A, start, pivot_index - 1, log, step + 1)
        step = quick_sort(A, pivot_index + 1, end, log, step + 1)
    return step


def partition(A, start, end, log, step):
    pivot = A[end]
    i = start - 1
    for j in range(start, end):
        action = "No Swap"
        reason = f"{A[j]} > {pivot}" if A[j] > pivot else f"{A[j]} <= {pivot}"
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
            action = "Swap" if i != j else "Move"
        log_step(log, step, reason, action, A, i, j, end)
        step += 1
    action = "Pivot Swap"
    reason = "Place pivot in correct position"
    A[i + 1], A[end] = A[end], A[i + 1]
    log_step(log, step, reason, action, A, i + 1, end, end)
    return i + 1, step + 1


def log_step(log, step, reason, action, A, i, j, p):
    log.append({
        "Step": step,
        "Reason": reason,
        "Action": action,
        "Array State": ', '.join(map(str, A)),
        "i": i if i >= 0 else '',
        "j": j,
        "p": p
    })


log = []
A = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]
final_step = quick_sort(A, log=log)

with open('quick_sort_log.csv', 'w', newline='') as file:
    fieldnames = ["Step", "Reason", "Action", "Array State", "i", "j", "p"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(log)

print(
    f"Quick Sort completed. Log saved to 'quick_sort_log.csv'. Total steps: {final_step}")
