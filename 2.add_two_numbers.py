def add_two_numbers(l1,l2):
    res = []
    carry = 0
    i,j = 0,0
    while i < len(l1) or j < len(l2) or carry:
        v1 = l1[i] if i<len(l1) else 0
        v2 = l2[j] if j<len(l2) else 0
        total = v1 + v2 + carry
        carry = total // 10
        res.append(total % 10)
        i +=1
        j +=1
    return res

# Example usage:
print(add_two_numbers([2,4,3], [5,6,4]))   # Output: [7,0,8]
print(add_two_numbers([0], [0]))           # Output: [0]
print(add_two_numbers([9,9,9,9,9,9,9], [9,9,9,9]))  # Output: [8,9,9,9,0,0,0,1]