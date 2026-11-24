class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. get initial position (pos, speed)
        car_states = [] 
        for i in range(len(position)):
            car_states.append((position[i], speed[i]))
        
        car_states.sort(reverse=True)

        # 2. iterate through array
        stack = []
        for p, s in car_states:
            target_time = (target - p) / s
            stack.append(target_time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)




