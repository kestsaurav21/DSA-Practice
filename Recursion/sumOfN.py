

def sumOfN(n):
    
    if n == 0:
        return 0
    
    return n + sumOfN(n-1)


n = int(input("Enter the number: "))
ans = sumOfN(n)
print(ans)



