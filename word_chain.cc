/*
* This problem was asked by Dropbox.
* Given a list of words, determine whether the words can be chained to form a circle.
* A word X can be placed in front of another word Y in a circle if the last character
* of X is same as the first character of Y.
* For example, the words ['chair', 'height', 'racket', touch', 'tunic'] can form the
* following circle: chair --> racket --> touch --> height --> tunic --> chair
*/

using namespace std;

bool IsChain(const vector<string> words) {
  vector<string> w(words);
  map<char, bool> pair_exists;
  while (!w.empty()) {
    // take
    string val = w.back();
    w.pop_back();
    // store first and last letters in the map
    // if they exist, switch their boolean
    char start = val.at(0);
    if (pair_exists.count(start)) {
      pair_exists.at(start) = !pair_exists.at(start);
    } else {
      pair_exists.emplace(start, false);
    }
    char end = val.at(sizeof(val) - 1);
    if (pair_exists.count(end)) {
      pair_exists.at(end) = !pair_exists.at(end);
    } else {
      pair_exists.emplace(end, false);
    }
  }
  // for key in map, return true if all values are true
}
