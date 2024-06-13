class Solution:
    def makeFancyString(self, s: str) -> str:
        output = ""
        count = 1
        output += s[0]
        for letter in range(1,len(s)):
            if s[letter] == s[letter-1]:
                count += 1

            else:
                count = 1

            if count < 3:
                output += s[letter]
            
        return output
        

