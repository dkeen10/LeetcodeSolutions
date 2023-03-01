class Solution {
    public int missingNumber(int[] nums) {
        nums.sort();
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != i) {
                return nums[i];
            }
        }
    }
}

Solution.missingNumber([3, 0, 1])