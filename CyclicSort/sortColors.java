//https://leetcode.com/problems/sort-colors/


class Solution {
    public static void sortColors(int[] nums) {
        if (nums.length < 2) {
            return;
        }
        int min = 0;
        int max = nums.length - 1;

        for (int i  = min; i < max; i++) {
            if (nums[i] == 0) {
                int temp = nums[i];
                nums[i] = nums[min];
                nums[min] = temp;
                i++;
                min++;
            }
            else if (nums[i] == 2) {
                int temp = nums[i];
                nums[i] = nums[max];
                nums[max] = temp;
                max--;
            }
            else {
                i++;
            }
        }
        System.out.println(nums); 
    }
}


class Test {
    public static void main(String[] args) {
        int[] array = new int[]{0, 2, 1, 1, 2};
        Solution.sortColors(array);
    }
}
