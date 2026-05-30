def two_sum(nums,target):
    seen = {}
    for _,value in enumerate(nums):
        compliment = target-value
        if compliment in seen:
            return [seen[compliment],_]
        seen[value] = _
        
        
        
print(two_sum([2,7,11,15], 9))  
print(two_sum([3,2,4], 6))      
print(two_sum([3,3], 6))