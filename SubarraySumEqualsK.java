/*
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
*/

class SubarraySumEqualsK {
    public int subarraySum(int[] nums, int k) {
        int subarrays = 0;
        int l;
        for (int i = 0; i < nums.length; i ++) {
            l = 0;
            for (int j = i; j < nums.length; j ++) {
                l += nums[j];
                if (l == k){
                    subarrays++;
                }
            }
        }
        return subarrays;
    }
}
