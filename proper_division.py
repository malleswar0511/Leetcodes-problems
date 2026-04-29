def proper_division(num):
    set_data = set()
    for i in range(1,num):
        if num % i ==0:
            set_data.add(i)
    return set_data

n = 220
print(proper_division(n))