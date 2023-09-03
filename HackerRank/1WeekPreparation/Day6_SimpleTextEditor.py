"""
Implement a simple text editor. The editor initially contains an empty string, S. 
Perform Q operations of the following 4 types:

append(W) - Append string W to the end of S.
delete(k) - Delete the last k characters of S.
print(k) - Print the kth character of S.
undo() - Undo the last (not previously undone) operation of type 1 or 2, 
        reverting S to the state it was in prior to that operation.

Example
S = 'abcde'
ops = ['1 fg', '3 6', '2 5', '4', '3 7', '4', '3 4']

operation
index   S       ops[index]  explanation
-----   ------  ----------  -----------
0       abcde   1 fg        append fg
1       abcdefg 3 6         print the 6th letter - f
2       abcdefg 2 5         delete the last 5 letters
3       ab      4           undo the last operation, index 2
4       abcdefg 3 7         print the 7th character - g
5       abcdefg 4           undo the last operation, index 0
6       abcde   3 4         print the 4th character - d

The results should be printed as:
f
g
d

Input format
The first line contains an integer, Q, denoting the number of operations.
Each line i of the Q subsequent lines (where 0 <= i < Q) defines an operation 
to be performed. 

Each operation starts with a single integer, t (where t belongs to {1,2,3,4}), 
denoting a type of operation as defined in the Problem Statement above. 

If the operation requires an argument, t is followed by its space-separated argument. 

For example, if t = 1 and W = "abcd", line i will be 1 abcd.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT


def simple_text_editor(Q, operations):
    S = ''  # Initial empty string
    history = []  # Stack to keep track of history for undo operations

    # Loop through each operation
    for op in operations:
        cmd = op.split()[0]

        if cmd == '1':
            # Append operation
            W = op.split()[1]
            history.append(S)  # Save the current state before changing
            S += W

        elif cmd == '2':
            # Delete operation
            k = int(op.split()[1])
            history.append(S)  # Save the current state before changing
            S = S[:-k]

        elif cmd == '3':
            # Print operation
            k = int(op.split()[1])
            if 0 <= k-1 < len(S):  # Check if index is in bounds
                print(S[k-1])
            else:
                print("Error: Index out of range")

        elif cmd == '4':
            # Undo operation
            if history:
                S = history.pop()  # Revert to the last saved state


# Test the function
Q = 7
operations = ['1 fg', '3 6', '2 5', '4', '3 7', '4', '3 4']
simple_text_editor(Q, operations)

Q = 8
ops = ['1 abc', '3 3', '2 3', '1 xy', '3 2', '4', '4', '3 1']
simple_text_editor(Q, ops)


# The version for HackerRank Input and Output
def simple_text_editor():
    Q = int(input().strip())  # Number of operations
    S = ''  # Initial empty string
    history = []  # Stack to keep track of history for undo operations

    # Loop through each operation
    for _ in range(Q):
        op = input().strip()
        cmd = op.split()[0]

        if cmd == '1':
            # Append operation
            W = op.split()[1]
            history.append(S)  # Save the current state before changing
            S += W

        elif cmd == '2':
            # Delete operation
            k = int(op.split()[1])
            history.append(S)  # Save the current state before changing
            S = S[:-k]

        elif cmd == '3':
            # Print operation
            k = int(op.split()[1])
            if 0 <= k-1 < len(S):  # Check if index is in bounds
                print(S[k-1])
            else:
                print("Error: Index out of range")

        elif cmd == '4':
            # Undo operation
            if history:
                S = history.pop()  # Revert to the last saved state


# Call the function
simple_text_editor()
