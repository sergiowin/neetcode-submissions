class Solution:

    def encode(self, strs: List[str]) -> str:
        retString = ""
        for s in strs:
            retString += "".join(str(len(s)) + "#" + s)
        return retString

    def decode(self, s: str) -> List[str]:
        retList = []
        lenInd = 0
        delimInd = 1
        while lenInd < len(s):
            delimInd = lenInd + 1
            while s[delimInd] != "#":
                delimInd += 1
            lenWid = delimInd-lenInd
            strWid = int(s[lenInd: lenInd + lenWid])
            startPoint = lenInd + lenWid + 1
            endPoint = startPoint + strWid
            retList.append(s[startPoint:endPoint])
            lenInd += lenWid + strWid + 1
        return retList