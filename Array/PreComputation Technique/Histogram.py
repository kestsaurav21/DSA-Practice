# we have been given an integer array ‘Arr[N]’ containing the heights of 'N' pillars. We have to find the total height of the water column trapped between the pillars after the rainfall. 

# LEETCODE - 42. Trapping Rain Water

#Brute force - T.C -> O(n^2)
def calculateTrappedWater(height):
    n = len(height)
    trappedWater = 0


    for i in range(1, n-1):
        left_max = max(height[:i+1])

        right_max = max(height[i:])

        trappedWater += min(left_max, right_max) - height[i]

    return trappedWater

height = [2,3,2,1,4,3]
print(calculateTrappedWater(height))

#Optimized Solution - using precomputation technique

def trappedWater(height):
    n = len(height)
    totalWater = 0
    leftMax = [0] * n
    rightMax = [0] * n

    leftMax[0] = height[0]

    for i in range(1,n):
        leftMax[i] = max(height[i], leftMax[i-1])

    rightMax[n-1] = height[n-1]

    for i in range(n-2, 0, -1):
        rightMax[i] = max(height[i], rightMax[i+1])

    for i in range(1, n-1):
        totalWater += min(leftMax[i], rightMax[i]) - height[i]

    return totalWater

height = [2,3,2,1,4,3]
print(trappedWater(height))