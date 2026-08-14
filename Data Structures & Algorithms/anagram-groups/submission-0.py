import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for string in strs:
            sortedStr = tuple(sorted(string))
            anagrams[sortedStr].append(string)
        return list(anagrams.values())
            
