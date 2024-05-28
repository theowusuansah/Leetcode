class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_brackets = {')':'(', ']': '[', '}': '{'}
        for char in s:
            if char in matching_brackets.values():
                  stack.append(char)
            else:
                  if not stack or stack.pop() != matching_brackets[char]:
                        return False
        return len(stack) ==0

            