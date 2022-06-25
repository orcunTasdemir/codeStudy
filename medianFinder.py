import heapq

class MedianFinder:

    def __init__(self):
        self.leftpq = []
        self.rightpq = []     
        
    def balance(self):
        if len(self.leftpq) == len(self.rightpq) + 2:
            node = heapq.heappop(self.leftpq)
            heapq.heappush(self.rightpq, -node)
        if len(self.leftpq) + 2 == len(self.rightpq):
            node = heapq.heappop(self.rightpq)
            heapq.heappush(self.leftpq, -node)
            
    def addNum(self, num: int) -> None:
        if not self.leftpq:
            self.leftpq.append(-num)
            return
        if num <= -self.leftpq[0]:
            heapq.heappush(self.leftpq, -num)
        else:
            heapq.heappush(self.rightpq, num)
        
        self.balance()

    def findMedian(self) -> float:
        if len(self.leftpq) == len(self.rightpq):
            return (-self.leftpq[0] + self.rightpq[0]) / 2
        elif len(self.leftpq) > len(self.rightpq):
            return -self.leftpq[0]
        else:
            return self.rightpq[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()