# Inputs
# 1. Size of Dusa
# N. Size of Yogis 

class Solution(object):
    def eat_yogis(self, s):
        size = s
        while True:
            yogi_size = int(input())
            if yogi_size >= size:
                break
            else:
                size += yogi_size

        return size

dusa_size = int(input())

S = Solution()
final_size = S.eat_yogis(dusa_size)
print(final_size)





