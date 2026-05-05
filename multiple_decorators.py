def deco1(func):
    def wrapper():
        print("deco1")
        func()
        
    return wrapper

def deco2(func):
    def wrapper():
        print("Deco2")
        func()
    return wrapper
@deco1
@deco2
def test():
    print("Hello")
    
test()