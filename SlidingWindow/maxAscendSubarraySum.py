#LeetCode 1800

class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        maxSum = 0
        subSum = 0

        for i in range(len(nums)):
            if i == 0 or nums[i - 1] < nums[i]:
                subSum += nums[i]
                maxSum = max(maxSum, subSum)
            else:
                subSum = nums[i]
        return maxSum


def main():
    solution = Solution()
    print(solution.maxAscendingSum([10, 20, 30, 5, 10, 50]))


if __name__ == "__main__":
    main()