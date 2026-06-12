class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        seconds = 0
        for i in range(len(tickets)):
            if k == i:
                continue
            if tickets[i] < tickets[k]:
                seconds += tickets[i]
            elif tickets[i] >= tickets[k]:
                seconds += tickets[k]
                if i > k:
                    seconds -= 1
                    
        return seconds + tickets[k]