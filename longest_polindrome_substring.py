def longest_palindrome(s: str) -> str:
    if not s or len(s) == 1:
        return s

    start, end = 0, 0

    def expand_around_center(left: int, right: int):
        # Expand while characters match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the bounds of the palindrome found
        return left + 1, right - 1

    for i in range(len(s)):
        # Odd length palindrome (center at i)
        l1, r1 = expand_around_center(i, i)
        # Even length palindrome (center between i and i+1)
        l2, r2 = expand_around_center(i, i + 1)

        # Update longest palindrome if found longer
        if r1 - l1 > end - start:
            start, end = l1, r1
        if r2 - l2 > end - start:
            start, end = l2, r2

    return s[start:end + 1]


# Example runs
print(longest_palindrome("babad"))  # Output: "bab" or "aba"
print(longest_palindrome("cbbd"))   # Output: "bb"
