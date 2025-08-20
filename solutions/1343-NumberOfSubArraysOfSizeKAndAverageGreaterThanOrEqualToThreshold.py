class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_sum = sum(arr[:k])
        threshold = threshold * k
        result = 0

        # Check the first window
        if window_sum >= threshold:
            result += 1

        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i-k]
            if window_sum >= threshold:
                result += 1

        return result