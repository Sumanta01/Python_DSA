
def nearest_divisible_integer(x, n):
    
    if x % n == 0:
        next_div = x
    else:
        next_div= x + (n - x % n)
    
    prev_div = x - (x % n)
    
    if abs(x - prev_div) <= abs(next_div - x):
        return prev_div
        
    else:
        return next_div

print(nearest_divisible_integer(67, 8)) 
print(nearest_divisible_integer(10, 3))  
