class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        from collections import deque
        stone_set = set(stones)
        last_stone = stones[-1]
        visited = set()
        queue = deque()
        queue.append((0, 0))  # (position, last_jump)

        while queue:
            pos, jump = queue.popleft()
            for new_jump in [jump - 1, jump, jump + 1]:
                if new_jump > 0:
                    next_pos = pos + new_jump
                    if next_pos == last_stone:
                        return True
                    if next_pos in stone_set and (next_pos, new_jump) not in visited:
                        visited.add((next_pos, new_jump))
                        queue.append((next_pos, new_jump))

        return False
