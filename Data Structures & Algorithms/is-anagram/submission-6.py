class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = {}
        dic_t = {}

        for i in s:
            if i in dic_s:
                dic_s[i] += 1
            else:
                dic_s[i] = 1
        
        for i in t:
            if i in dic_t:
                dic_t[i] += 1
            else:
                dic_t[i] = 1
        
        return dic_s == dic_t