class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) <= 0:
            return "%nn%"
        return "%n_n%".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "%nn%":
            return []
        return s.split("%n_n%")