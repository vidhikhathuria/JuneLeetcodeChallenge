# Problem Link : https://leetcode.com/problems/two-city-scheduling/


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:  
        costs.sort(key= lambda  x : x[1] - x[0])
        return sum([i[0] for i in costs[int(len(costs) / 2):]]) + sum([i[1] for i in costs[:int(len(costs) / 2)]])