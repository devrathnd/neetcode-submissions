class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        close_to_open = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in close_to_open:  # closing bracket

                if not stack:
                    return False

                if stack.pop() != close_to_open[ch]:
                    return False

            else:  # opening bracket
                stack.append(ch)

        return len(stack) == 0
                        