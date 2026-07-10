from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        stack = deque()
        if s == "":
            return True
        if s[0] not in "({[":
            return False
            
        for c in s:
            if c in ("({["):
                stack.append(c)
            else:
                val = None
                if stack:
                    val = stack.pop()
                if closeToOpen[c] != val:
                    return False
                # if c == "}" and val != "{":
                #     return False
                # if c == "]" and val != "[":
                #     return False
                # if c == ")" and val != "(":
                #     return False
            
        return len(stack) == 0