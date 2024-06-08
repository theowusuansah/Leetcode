class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')','{':'}', '[':']'}
        storage = []
        for i in s:
            if i in d.keys():
                storage.append(i)
            else:
                if not storage or  d[storage.pop()] != i :
                    return False

        return len(storage)==0

            