class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        d = set()

       
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
            elif s[i] == s[-1]:
                return t[-1]

        if not s:
            return t[0]

     

       





