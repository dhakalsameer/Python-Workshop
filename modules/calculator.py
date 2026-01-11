def sum(*args):
    total = 0
    for num in args:
        total += num
    return total
    

def product(*args):
    result = 1
    for num in args:
        result *= num
    return result

def quotient(dividend, divisor):
    return dividend / divisor

def difference(val1, val2):
    return val1 - val2

print(sum(1, 2, 3, 4))          
print(product(1, 2, 3, 4))      
print(quotient(10, 2))         
print(difference(10, 5))        
# print(quotient(10, 0))          
