class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        maxVal = 0
        chunks = 0

        for i in range(len(arr)):
            maxVal = max(arr[i], maxVal)

            if (maxVal == i):
                chunks += 1

        return chunks
