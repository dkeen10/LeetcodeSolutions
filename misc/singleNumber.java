package misc;

//https://leetcode.com/problems/single-number/description/

import java.util.Arrays;


class Solution {
    public static int singleNumber(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }

        Arrays.sort(nums);

        if (nums[0] != nums[1]) {
            return nums[0];
        }
        if (nums[nums.length-1] != nums [nums.length-2]) {
            return nums[nums.length-1];
        }

        for (int i = 1; i < (nums.length - 1); i++) {
            if (nums[i-1] != nums[i] && nums[i+1] != nums[i]) {
                return nums[i];
            }
        }
        return -1;
    }
}


class Test {
    public static void main(String[] args) {
        int[] array = new int[]{4, 2, 1, 1, 2};
        System.out.println(Solution.singleNumber(array));
        Solution.singleNumber(array);
    }
}
