import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        
        for string in strs:
            anagramKey = [0] * 26
            for char in string:            
                anagramKey[ord(char) - ord('a')] += 1
            anagrams[tuple(anagramKey)].append(string)
        return list(anagrams.values())
            
