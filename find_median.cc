/* 
* Create an algorithm to efficiently compute the approximate median of a list of numbers.
* More precisely, given an unordered list of N numbers, find an element whose rank is
* between N / 4 and 3 * N / 4, with a high level of certainty, in less than O(N) time.
*/

float FindMedian(float[] list) {
  int N = sizeof(list);
  float lower_bound = N / 4;
  float upper_bound = 3 * N / 4;
  for (int i = 0; i < N; i++) {
    if (list[i] <= upper_bound && list[i] >= lower_bound) {
      return list[i];
    }
  }
  return 0;
}
