class Solution:
    def startStation(self, gas, cost):
        total_gas, total_cost = sum(gas), sum(cost)
        
        # If total gas is less than total cost, it's impossible to complete the circuit
        if total_gas < total_cost:
            return -1
        
        start, fuel = 0, 0
        
        for i in range(len(gas)):
            fuel += gas[i] - cost[i]
            if fuel < 0:
                start = i + 1
                fuel = 0
        
        return start
