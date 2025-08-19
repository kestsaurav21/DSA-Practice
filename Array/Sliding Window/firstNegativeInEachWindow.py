# First negative in every window of size k

# Given an array arr[]  and a positive integer k, find the first negative integer for each and every window(contiguous subarray) of size k.

#Brute Force - O(N^2)
# def firstNegative(arr, k):
#     n = len(arr)
#     ans = []
#     for i in range(n-k+1):
#         found = False
#         for j in range(i, i+k):
#             if arr[j] < 0:
#                 ans.append(arr[j])
#                 found = True
#                 break
#         if found == False:
#             ans.append(0)    
#     print(ans)         


# arr = [-8,2,3,-6,10]
# k = 2
# firstNegative(arr, k)


# Optimised - Sliding window


def firstNegativeInteger(arr,k):
    n = len(arr)
    q = []
    ans = []
    i=j=0

    while j < n:
        if arr[j] < 0:
            q.append(j)

        if( j-i+1 < k):
            j+=1
        elif(j-i+1 == k):
            if q: 
                ans.append(arr[q[0]])
            else: 
                ans.append(0)

            if q and q[0] == i:
                q.pop(0)
            i+=1
            j+=1
        

    return ans

arr = [-8,2,3,-6,10]
k = 2

print(firstNegativeInteger(arr, k))
