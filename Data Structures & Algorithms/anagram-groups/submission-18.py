import string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashgroups = defaultdict(list)
        for i in range(len(strs)):
            letters = tuple([strs[i].count(char) for char in string.ascii_lowercase])
            hashgroups[letters].append(strs[i])

        return list(hashgroups.values())