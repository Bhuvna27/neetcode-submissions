class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        one, two = cost[n-2], cost[n-1]
        i = n-3
        while i>=0:
            cost[i]=cost[i]+min(one,two)
            two = one
            one = cost[i]
            i= i-1
        return min(cost[0],cost[1])
        