class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        seen_in_A = set()
        seen_in_B = set()
        C = []

        for i in range(n):
            seen_in_A.add(A[i])
            seen_in_B.add(B[i])
            C.append(len(seen_in_A.intersection(seen_in_B)))
            
        return C