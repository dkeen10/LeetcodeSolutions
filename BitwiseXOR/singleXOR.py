"""https://leetcode.com/problems/xor-operation-in-an-array/"""


class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums = []
        for i in range (0, n):
            nums.append(start + 2 * i)
        xor_result = 0
        for j in range(len(nums)):
            xor_result = xor_result ^ nums[j]
        return xor_result


def main():
    soln = Solution()
    print(soln.xorOperation(4, 3))


if __name__=="__main__":
    main()
