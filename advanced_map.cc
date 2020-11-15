/*
* Create a data structure that performs all the following operations in O(1) time:
* plus: Add a key with value 1. If the key already exists, increment its value by one.
* minus: Decrement the value of a key. If the key's value is currently 1, remove it.
* get_max: Return a key with the highest value.
* get_min: Return a key with the lowest value.
*/

class AdvancedMap {
public:
  /// plus: Add a key with value 1. If the key already exists, increment its value by one.
  void plus(std::string key) {
    if ((iterator = find(key)) == false) {
      insert(pair<std::string, int>(key, 1);
    } else {
      // add one and compare to the max
    }
  }
  
  /// minus: Decrement the value of a key. If the key's value is currently 1, remove it.
  void minus(std::string key) {
    // if value of iterator is 1, remove
    if ((iterator = find(key)) == true && iterator[0] == 1) {
      // remove
    } else {
      // subtract one and compare to the min
    }
  }
  
  /// get_max: Return a key with the highest value.
  int get_max() { return max; }
  
  /// get_min: Return a key with the lowest value.
  int get_min() { return min; }

private:
  int max, min;
};
