class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            table = [0] * 26

            for i in s:
                table[ord(i) - ord('a')] += 1
            
            table = tuple(table)
            if table in res:
                res[table].append(s)
            else:
                res[table] = [s]
        
        return(list(res.values()))