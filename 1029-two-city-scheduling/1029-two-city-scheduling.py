class Solution(object):
    def twoCitySchedCost(self, costs):
        costs.sort(key=lambda x:x[0] - x[1])
        total=0
        print(costs)
        n=len(costs)//2
        for i in range(n):
            total+=costs[i][0]
        for i in range(n,2*n):
            total+=costs[i][1]
        return total
            