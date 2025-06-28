class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        answer = [0] * n
        stack = [] 
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                answer[idx] = i - idx
            stack.append(i)
        return answer
temperatures = [73,74,75,71,69,72,76,73]
sol = Solution()
print(sol.dailyTemperatures(temperatures)) 
