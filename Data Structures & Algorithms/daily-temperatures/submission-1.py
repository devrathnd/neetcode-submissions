class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #[temp, index]
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            if not stack:
                stack.append([t, i])
            else:
                while stack:
                    [lastTemp, lastIndex]  = stack[-1]
                    if t > lastTemp:
                        result[lastIndex] = i - lastIndex
                        stack.pop()
                    else:
                        break
                stack.append([t, i])

        return result

