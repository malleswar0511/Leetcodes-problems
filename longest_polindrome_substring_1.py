def isPolindrome(sub):
    if sub == sub[::-1]:
        return sub

def longest_polindrome_substring(s):
    if len(s) == 0:
        return ""
    
    longest = s[0]
    for i in range(len(s)):
        for j in range(i,len(s)):
            sub = s[i:j+1]
            if isPolindrome(sub) and len(sub)> len(longest):
                longest = sub
    return longest
            
print(longest_polindrome_substring("abc"))
print(longest_polindrome_substring("forgeeksskeegfor"))
print(longest_polindrome_substring("geeks"))
print(longest_polindrome_substring(""))

