class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## two pointers defining edges, i defines begin, j defines end.
        i = 0
        j = 0
        ##contains set keeps an active record of what is actually inside of the sliding window to ensure that there is not duplicates
        contains = set()
        ##tracker to see what the maxLen seen so far is
        maxLen = 0
        ##defined var for current length vs maxLen comparison coming up
        curLen = 0
        ## loop terminating when j reaches the end, thus observing all relevant possible combinations
        while j != len(s):
            if s[j] in contains:
                while s[i] != s[j]:
                    contains.remove(s[i])
                    i += 1
                ## increments i without removing character because it is still present just in a different location (at j instead of i - 1)
                i += 1
            else: 
                contains.add(s[j])
                curLen = j - i + 1
                maxLen = max(curLen, maxLen)
            j += 1
        return maxLen

            

            
            
        
        