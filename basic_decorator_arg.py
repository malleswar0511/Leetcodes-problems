def repeat_decorator(func):
    def wrapper(*args,**kwargs):
        print("Running function twice")
        func(*args,**kwargs)
        func(*args,**kwargs)
    return wrapper

@repeat_decorator
def greet(name):
    print(f"Hello {name}")
    
greet("Malleswar")