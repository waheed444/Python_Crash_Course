
# 9. Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit.

def even_generator(limit):
    for i in range(2, limit + 1, 2):   # Start from 2 , goes to limit , step of 2 
        yield i   # that yields even numbers up to a specified limit.



for num in even_generator(10):
    print(num)
    
    
# A generator function uses yield instead of return to produce a value. When yield is executed, 
   # it pauses the function's execution and sends the yielded value to the caller. 
   # The function can resume from where it left off the next time it is called.