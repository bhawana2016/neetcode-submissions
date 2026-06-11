class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        l1 = sorted(s)
        l2 = sorted(t)
        if l1 == l2:
            return True
        return False