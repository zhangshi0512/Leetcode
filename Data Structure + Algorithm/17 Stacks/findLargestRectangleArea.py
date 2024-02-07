def findLargestRectangleArea(heights):
    stack = []  # Stack to store indices of bars
    maxArea = 0  # Keep track of the maximum area
    heights.append(0)  # Append a 0 to handle remaining bars in stack

    for i, height in enumerate(heights):
        while stack and height < heights[stack[-1]]:
            top = stack.pop()  # Pop the top bar off the stack
            # Calculate the width of the rectangle
            width = i if not stack else i - stack[-1] - 1
            area = heights[top] * width  # Calculate the area
            maxArea = max(maxArea, area)  # Update max area if necessary

            # Visualize the process when a rectangle is calculated
            print(
                f"Rectangle with height {heights[top]} and width {width} => Area: {area}")
            printHistogram(heights[:len(heights)-1],
                           heights[top], stack[-1]+1 if stack else 0, i-1)

        # Visualize every step when considering a new bar
        if stack:
            print(f"Considering bar at index {i} with height {height}")
            printHistogram(heights[:len(heights)-1], height, stack[-1], i)

        stack.append(i)  # Push the current bar onto the stack

    return maxArea


def printHistogram(heights, height, start, end):
    for row in range(max(heights), 0, -1):
        for i, h in enumerate(heights):
            if start <= i <= end and h >= row:
                print('*', end='')
            else:
                print(' ', end='')
        print()  # New line after each row
    print('^' * len(heights))  # Base of the histogram


# Example histogram heights
heights = [2, 1, 5, 6, 2, 3]
print("Given histogram:", heights)
maxArea = findLargestRectangleArea(heights)
print("Maximum Rectangle Area:", maxArea)
