class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "None"

        res = []

        for s in strs:
            res.append(s)
            res.append("<>")
        return "".join(res[:-1])

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        return s.split("<>")
