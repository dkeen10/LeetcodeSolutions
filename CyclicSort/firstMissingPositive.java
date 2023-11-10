//https://leetcode.com/problems/first-missing-positive/description/

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;


class Solution {
    public static int firstMissingPositive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            set.add(nums[i]);
        }

        int j = 1;
        while (j <= nums.length) {
            if (set.contains(j)) {
                j++;
            } else {
                return j;
            }
        }
        return -1;
    }
}    


class Test {
    public static void main(String[] args) {
        int[] array = new int[]{0, 1, -1, 3, 4};
        System.out.println(Solution.firstMissingPositive(array));
    }
}
