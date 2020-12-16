/*
* This problem was asked by Dropbox.
* Implement an efficient string matching algorithm.
* That is, given a string of length N and a pattern of length k,
* write a program that searches for the pattern in the string with
* less than O(N * k) worst-case time complexity.
* If the pattern is found, return the start index of its location. If not, return False.
*/

int SubstringMatch(std::string string, std::string pattern, int N, int K) {
  // pointers to the beginning and end of pattern
  int beg = 0;
  int end = K - 1;
  int begptr = beg;
  int endptr = end;
  while (endptr < N) {
    if (string[begptr] == pattern[beg] && string[endptr] == pattern[end]) {
      int temp_begptr = begptr;
      int temp_beg = beg
      while (begptr < endptr) {
        if (string[begptr] != pattern[begptr]) {
          break;
        }
        begptr++;
        beg++;
      }
      if (begptr == endptr) {
        return temp_begptr;
      }
      begptr = temp_begptr;
      beg = temp_beg;
    }
    begptr++
    endptr++
  }
  return -1;
}
