def nearest_subnumber(n1: int, n2: int) -> int:
    s = str(n1)
    subnumbers = []

    # Generate all possible contiguous subnumbers
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            subnumbers.append(int(s[i:j]))

    # First, filter subnumbers that are >= n2
    larger_or_equal = [x for x in subnumbers if x >= n2]

    if larger_or_equal:
        # Pick the one with smallest difference among larger ones
        return min(larger_or_equal, key=lambda x: abs(x - n2))
    else:
        # If no larger subnumber exists, fallback to closest smaller
        return min(subnumbers, key=lambda x: abs(x - n2))


# Example usage
n1 = 123
n2 = 16
print(nearest_subnumber(n1, n2))  # Output: 23
