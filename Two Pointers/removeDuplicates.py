# Leetcode 26
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0;
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[j] = nums[i]
                j = j + 1
            i = i + 1 
        return j


def main():
    solution = Solution()
    print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


if __name__ == "__main__":
    main()