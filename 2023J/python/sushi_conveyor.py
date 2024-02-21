# Inputs 
# 1. Number of red plates ($3 each)
# 2. Number of green plates ($4 each)
# 3. Number of blue plates ($5 each)

class Solution(object):
    def calculate_cost(self, red, green, blue):
        red_cost = red * 3
        green_cost = green * 4
        blue_cost = blue * 5
        total_cost = red_cost + green_cost + blue_cost 

        return total_cost

red_plates = int(input())
green_plates = int(input())
blue_plates = int(input())

S = Solution()
cost = S.calculate_cost(red_plates, green_plates, blue_plates)
print(cost)

