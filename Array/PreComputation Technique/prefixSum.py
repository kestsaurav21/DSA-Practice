
def prefixSum(arr, queries): 
    n = len(arr)
    PS = [0] * n
    PS[0] = arr[0]

    for i in range(1, n):
        PS[i] = PS[i-1] + arr[i]


    result = []

    for l, r in queries: 
        if l == 0:
            result.append(PS[r])
        else:
            result.append(PS[r]- PS[l-1])

    return result

arr = [10, 5, 8, 2, 7]
queries = [(0, 2), (1, 3), (2, 4)]
print(prefixSum(arr, queries))
