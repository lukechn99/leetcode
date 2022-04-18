### META interview question

from typing import List


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    buckets = {}
    for s in strs:
        sorted_s = str(sorted(s))
        if sorted_s in buckets:
            buckets[sorted_s].append(s)
        else:
            buckets[sorted_s] = [s]
    return [buckets[token] for token in buckets.keys()]