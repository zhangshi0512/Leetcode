def radix_sort(lst):
    if not lst:
        return lst

    # Determine the maximum length of the words
    max_length = max(len(word) for word in lst)

    # Start from the least significant digit (rightmost character)
    for i in range(max_length - 1, -1, -1):
        # Initialize buckets for each letter in the alphabet
        # We assume only lowercase letters plus one bucket for shorter words
        buckets = {chr(k): [] for k in range(ord('a'), ord('z') + 1)}
        buckets[''] = []  # For shorter words

        # Place each word into the corresponding bucket based on current character
        for word in lst:
            letter = word[i] if i < len(word) else ''
            buckets[letter].append(word)

        # Combine words from buckets back to list
        lst = []
        print(f"--- Sorting by character at position {-max_length + i}: ---")
        for letter in sorted(buckets.keys()):
            lst.extend(buckets[letter])
            if buckets[letter]:  # Only print non-empty buckets for clarity
                print(f"Bucket '{letter}': {buckets[letter]}")
        print(f"Combined list: {lst}\n")

    return lst


# List of words to sort
words = ["cow", "dog", "sea", "rug", "row", "mob", "box", "tab",
         "bar", "ear", "tar", "dig", "big", "tea", "now", "fox"]

# Perform radix sort
sorted_words = radix_sort(words)
print(f"\nSorted list: {sorted_words}")
