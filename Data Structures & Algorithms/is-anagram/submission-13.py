class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = defaultdict(int)
        tDict = defaultdict(int)
        for i in range(len(s)):
            sDict[s[i]] += 1
        for j in range(len(t)):
            tDict[t[j]] += 1
        if sDict == tDict:
            return True
        else:
            return False