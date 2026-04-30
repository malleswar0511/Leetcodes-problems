def factorial(num):
    if num == 0 or num == 1 :
        return 1
    else:
        return num * factorial(num-1)
    

def check_strong_number(num):
    temp = str(num)
    count = 0
    for i in temp:    
        count += factorial(int(i))
    if count == int(temp):
        print(f"{num} is a strong number")
    else:
        print(f"{num} is a Not strong number")
    
    
    

n = 145
check_strong_number(n)