class MergeSortArray {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        // dynamically sort the array
        int endPtr = m + n;

    }
    public void merge2(int[] nums1, int m, int[] nums2, int n) {
        for (int i = m; i < m+n; i++) {
            nums1[i] = nums2[i-m];
        }
        for (int i = 0; i < m+n; i++) {
            int min = nums1[i];
            int placeholder = i;
            for (int j = i; j < m+n; j++) {
                if (nums1[j] < min) {
                    min = nums1[j];
                    placeholder = j;
                }
            }
            int temp = nums1[i];
            nums1[i] = min;
            nums1[placeholder] = temp;
        }
    }
}