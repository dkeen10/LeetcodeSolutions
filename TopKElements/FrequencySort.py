"""come back to this one."""

class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        for element in nums:
            if element in dic:
                dic[element] += 1
            else:
                dic[element] = 1
        sorted_dic = sorted(dic, reverse=True)
        list_occur = list(sorted(sorted_dic.keys()))
        result = []
        for element in list_occur:
            sorted_dic[element].sort(reverse=True)
            for y in sorted_dic[element]:
                result.append(sorted_dic[element])

        return result
            
def main():
    solution = Solution()
    solution.frequencySort([1, 1, 2, 2, 2, 3])


if __name__ == "__main__":
    main()
    