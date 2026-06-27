class Solution:
    @classmethod
    def check_polindrome(cls,s):
        return s == s[::-1]
        
    
    def longest_substring(n):
        longest_substr = n[0]
        for i in range(len(n)):
            for j in range(i,len(n)):
                sub_str = n[i:j+1]
                if Solution.check_polindrome(sub_str) and len(sub_str)>len(longest_substr):
                    longest_substr = sub_str
        return longest_substr
            
            
n1= "babad"
n2 = "cbbd"
print(Solution.longest_substring(n1))
print(Solution.longest_substring(n2))