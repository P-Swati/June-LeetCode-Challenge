#approach : sort acc to diff in cost to send to city A and B
# the half having min diff ie either more cost to B than A, or bery small value will go to city A.
# and other half will go to B.
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs.sort(key=lambda x:x[0]-x[1])
        
        print(costs)
        
        s=0
        
        for i in range(len(costs)):
            if(i<len(costs)//2):
                s+=costs[i][0]
            else:
                s+=costs[i][1]
                
                
        return s
