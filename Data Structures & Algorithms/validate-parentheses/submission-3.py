class Solution:
    def isValid(self, s: str) -> bool:

        stack = collections.deque()

        mapping = {
            "[" : "]",
            "{" : "}",
            "(" : ")"
        }

        for c in s:

            if c in "[({":
                stack.append(c)
                continue

            if len(stack) == 0 or mapping[stack.pop()] != c:
                return False
            
        if len(stack) != 0:
            return False

        return True