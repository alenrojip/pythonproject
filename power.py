#Implement pow(x, n), which calculates x raised to the power n (i.e., xn)
def pow(x, n):
    if n==0:
        return 1
    if n<0:
        x=1/x
        n=-n
    
    result=1
    current_product=x
    
    while n>0:
        if n%2==1:
            result*=current_product
        current_product*=current_product
        n//=2
    
    return result


print(pow(2,10))
print(pow(2,-2))
print(pow(2,0))