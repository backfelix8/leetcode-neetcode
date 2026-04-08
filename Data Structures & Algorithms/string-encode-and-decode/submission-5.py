class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for st in strs:
            result += "%1%"
            result += st

        return result
        

    def decode(self, s: str) -> List[str]:
        return s.split("%1%")[1:]
