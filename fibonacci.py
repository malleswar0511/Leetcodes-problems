
def fibonacci(num):
    count = 0
    n1,n2 = 0,1
    while count<num:
        print(n1,end = " ")
        nth = n1+n2
        n1 = n2
        n2 = nth
        count +=1
    print(count)
    
x = 5
fibonacci(x)