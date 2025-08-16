## we have been given an array ‘Arr[N]’ and we have to maximise ‘s’. 
## s = p*Arri + q*Arrj + r*Arrk where p, q, r ∈ Z and i < j < k


def maximize_expression(arr, p, q, r):
    n = len(arr)
    pmax = [0] * n
    smax = [0] * n
    ans = -10**9

    pmax[0] = p*arr[0]
    for i in range(1, n):
        pmax[i] = max(p*arr[i], pmax[i-1])

    smax[n-1] = r*arr[n-1]
    for i in range(n-2, 0, -1):
        smax[i] = max(r*arr[i], smax[i+1])

    for i in range(1, n-1):
        val = pmax[i-1] + smax[i+1] + q*arr[i]
        ans = max(val, ans)

    return ans



if __name__ == "__main__":
    n = int(input("Enter the size of array: "))
    arr = list(map(int, input("Enter array elements ").split()))
    p,q,r = map(int, input("Enter p, q, r").split())

    result = maximize_expression(arr, p, q, r)
    print("Maximum value for the expression=", result)

