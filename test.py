from xmlrpc.client import MAXINT


from xmlrpc.client import MAXINT

class Solution:
    def findMax(self, l, k):
        size =len(l)
        if k > size: k = size
        
        sums = []
        for wS in range(1,k):
            sums.append(self.getHighestSum(l, wS)) 
        return max(sums)
    
    def getHighestSum(self, l, wS):
        sums = []
        for i in range(len(l)):
            sum = 0
            for idx in range(i, i+wS-1):
                if idx < len(l):
                    sum += l[idx]
            sums.append(sum)
        return max(sums)
                
s = Solution()
l = (1,4,7,6,5,4,3,1,99,8,5,3,2,1,6,0,5)
k = 4
print(s.findMax(l, k))
                
                