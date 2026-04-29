def number_adjacent(nums):
    count = 0
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            count += 1 
    print(count)
n = [1,2,2,3,4,4,5]
number_adjacent(n)
    