def factorialOfN(n):

    if n == 0 or n == 1:
        return 1
    
    return n * factorialOfN(n-1)




n = int(input("Enter a number:"))
ans = factorialOfN(n)
print(ans)