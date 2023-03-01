class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left = letters[0:len(letters)//2]
        right = letters[len(letters)//2:len(letters)]
        print(left)
        print(right)
        
def main():
    solution = Solution()
    solution.nextGreatestLetter(["c","f","j"], "a")


if __name__ == "__main__":
    main()
    