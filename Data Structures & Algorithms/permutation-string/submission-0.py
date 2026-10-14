class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #sliding window problem
        #the range of the sliding window is based on the size of s1
        #first we will pass over s1 and make a hash map of occurences
        s1Map = defaultdict(int)
        winMap = defaultdict(int)
        for char in s1:
            s1Map[char] += 1
        reqMatch = len(s1)
        winMatch = 0
        #then based on the length we will create a sliding window that will manage the occurences 
        #of every letter in the window
        # the left will be i, and the right will be r = i + len(s1) - 1
        for i in range(len(s2) - len(s1) + 1):
            print("i: ", i)
            if i == 0:
                for r in range(len(s1) - 1):
                    print("r init: ", r)
                    winMap[s2[r]] += 1
                    if winMap[s2[r]] <= s1Map[s2[r]]:
                        winMatch += 1
            r = i + len(s1) - 1
            # i - 1 has now left the window, so we shall remove
            if i != 0:
                winMap[s2[i-1]] -= 1
                if winMap[s2[i-1]] < s1Map[s2[i-1]]:
                    winMatch -= 1
            print("r: ", r)

            winMap[s2[r]] += 1
            if winMap[s2[r]] <= s1Map[s2[r]]:
                winMatch += 1
            print(winMatch)
            if winMatch == reqMatch:
                return True
            print("loop")
        return False

                    
        


        # if the occurences directly match the map of occurences in s1 we can return true
        # after loop then return false as no matches were found


        