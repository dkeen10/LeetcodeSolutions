#LeetCode 1800

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        nums = [num**2 for num in nums]
        nums.sort()
        return nums

def main():
    solution = Solution()
    print(solution.sortedSquares([-4, -1, 0, 3, 10]))


if __name__ == "__main__":
    main()