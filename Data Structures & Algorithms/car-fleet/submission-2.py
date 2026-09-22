class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        for i, p in enumerate(position):
            pos_speed.append((p, (target - p) / speed[i]))

        pos_speed.sort(key=lambda x: (x[0]))

        stack = []
        for (p, t) in reversed(pos_speed):
            if stack and t > stack[-1]:
                stack.append(t)
            elif not stack:
                stack.append(t)
            
        return len(stack)