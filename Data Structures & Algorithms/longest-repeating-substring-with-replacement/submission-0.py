class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        occurs = defaultdict(int) ## will hold all characters
        curMaxChar = None ## the character that occurs the most, we will use to do O(1) lookup comparison everytime a letter is added
        maxStr = 0 ## 
        replacements = 0 ## amount of replacements currently made
        l = 0 ## left ptr

        for i, char in enumerate(s):
            if curMaxChar == None:
                curMaxChar = char
            if char != curMaxChar:
                occurs[char] += 1
                if occurs[char] > occurs[curMaxChar]: ## changes to new most occuring character
                    curMaxChar = char
                    replacements = (sum(occurs.values()) - occurs[curMaxChar])
                if char != curMaxChar:
                    replacements += 1 ## needs another replacement

            elif char == curMaxChar: 
                occurs[char] += 1

            while replacements > k:
                if s[l] == curMaxChar:
                    occurs[curMaxChar] -= 1
                    if max(occurs.values()) != occurs[curMaxChar]:
                        for key, v in occurs.items():
                            if v > occurs[curMaxChar]:
                                curMaxChar = key ## sets new max character 
                    replacements = (sum(occurs.values()) - occurs[curMaxChar])         
                elif s[l] != curMaxChar:
                    occurs[s[l]] -= 1
                    replacements -= 1
                l += 1

            calcLen = i - l + 1

            if calcLen > maxStr:
                maxStr = calcLen
        return maxStr


            
            



            

            
            