//https://leetcode.com/problems/missing-number/

import java.util.Arrays;

class Solution {
    public static int missingNumber(int[] nums) {
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != i) {
                return i;
            }
        }
        return nums.length;
    }
}

class Test {
    public static void main(String[] args) {
        int[] array = new int[]{0, 2, 1, 1, 2};
        Solution.missingNumber(array);
    }
}

