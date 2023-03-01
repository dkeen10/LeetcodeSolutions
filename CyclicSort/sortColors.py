# https://leetcode.com/problems/sort-colors/

class Solution(object):
    def sortColors(self, nums):
        """
        This function moves all zeroes to the beginning, all twos to the right, and leaves the ones unchanged. 

        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if nums.length <= 1:
            return
        beginning = 0
        end = nums.length
        
        for

def main():
    solution = Solution()
    print(solution.sortColors([2, 0, 2, 1, 1, 0]))


if __name__ == "__main__":
    main()