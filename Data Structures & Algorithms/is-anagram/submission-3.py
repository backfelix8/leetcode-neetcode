class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        for i in range(len(s)):
            c_s = s[i]
            c_t = t[i]

            count_s[c_s] = count_s.get(c_s,0) + 1
            count_t[c_t] = count_t.get(c_t,0) + 1

        return count_s == count_t