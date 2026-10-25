class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            freq = {}

            for c in s:
                freq[c] = freq.get(c, 0) + 1

            key = tuple(sorted(freq.items()))

            if key not in groups:
                groups[key] = []

            groups[key].append(s)

        return list(groups.values())