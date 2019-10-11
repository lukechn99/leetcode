/*
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
*/

class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        int sumIndices[] = new int[2];
        for (int j = 0; j < nums.length; j ++) {
            sumIndices[0] = j;
            for (int i = j + 1; i < nums.length; i ++) {
                if (nums[sumIndices[0]] + nums[i] == target){
                    sumIndices[1] = i;
                    return sumIndices;
                }
            }
        }
        return sumIndices;
    }
}