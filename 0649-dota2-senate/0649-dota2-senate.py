class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        r_q = deque(i for i, c in enumerate(senate) if c == 'R')
        d_q = deque(i for i, c in enumerate(senate) if c == 'D')

        while r_q and d_q:
            r = r_q.popleft()
            d = d_q.popleft()
            if r < d:
                # R bans D; R survives to next round at position r + n
                r_q.append(r + n)
            else:
                # D bans R; D survives to next round at position d + n
                d_q.append(d + n)

        return "Radiant" if r_q else "Dire"
        