class Solution {
    public void sortColors(int[] nums) {
        if (nums.length < 2) {
            return;
        }
        min = 0;
        max = nums.length - 1;

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
        system.out.println(nums)
        
    }
}

