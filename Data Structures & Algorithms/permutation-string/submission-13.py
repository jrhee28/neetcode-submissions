class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r = 0
        l = 0
        for l in range(len(s2)):
            r = l + len(s1) - 1
            
            if r >= len(s2):
                return False
            
            window = sorted(s2[l:r+1])
            if sorted(s1) == window:
                return True 
        return False




