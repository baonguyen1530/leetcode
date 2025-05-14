class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        if event1[0] < event2[0]:
            if event1[1] < event2[0]:
                return False
            else:
                return True
        else:
            if event2[1] < event1[0]:
                return False
            else:
                return True