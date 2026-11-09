class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for i in strs:
            sortedS = tuple(sorted(i))
            if sortedS in res:    
                res[sortedS].append(i)
            else:
                res[sortedS] = [i]
            
        return list(res.values())