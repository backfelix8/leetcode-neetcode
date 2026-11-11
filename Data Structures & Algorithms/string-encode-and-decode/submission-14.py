class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        result = ""

        for s in strs:
            result += str(len(s)) + "#"
            result += s
        
        return result


    # len#string
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        if s == "":
            return [""]
        
        result = []
        
        i = 0
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            next_len = int(s[i:j])
            next_str = s[j+1 : j+1+next_len]
            result.append(next_str)

            i = j + 1 + next_len

        return result
