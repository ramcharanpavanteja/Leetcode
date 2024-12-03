class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        res = ""
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]]+=1
            else:
                dic[s[i]]=1
        for i,count in dic.items():
            if count == 1:
                res=i
                break
        if res == "":
            return -1
        else:
            for i in range(len(s)):
                if s[i] == res:
                    return i
            
