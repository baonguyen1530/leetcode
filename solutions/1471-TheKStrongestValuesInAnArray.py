class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        if len(arr) == 1:
            return arr
        arr.sort()
        centre = arr[(len(arr)-1)//2]
        res = []
        l,r = 0,len(arr)-1

        while (l<=r):
            if abs(arr[l]-centre) > abs(arr[r]-centre):
                res.append(arr[l])
                l += 1
            else:
                res.append(arr[r])
                r -= 1
                
        return res[:k]