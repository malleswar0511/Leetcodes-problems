class Solution:
    def addTwoNumbers(self, l1, l2):
        res = []
        carry = 0
        i, j = 0, 0
        while i < len(l1) or j < len(l2) or carry:
            v1 = l1[i] if i < len(l1) else 0
            v2 = l2[j] if j < len(l2) else 0
            total = v1 + v2 + carry
            carry = total // 10
            res.append(total % 10)
            i += 1
            j += 1
        return res


# Test cases
s = Solution()
print(f"example 1 : {s.addTwoNumbers([2,4,3],[5,6,4])}")
print(f"example 2 : {s.addTwoNumbers([0],[0])}")
print(f"example 3 : {s.addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9])}")
