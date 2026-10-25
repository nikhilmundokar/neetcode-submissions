class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        res_s, res_t = {}, {}
        for ch in s:
            if ch in res_s:
                res_s[ch] += 1
            else:
                res_s[ch] = 1

        for ch in t:
            if ch not in res_t:
                res_t[ch] = 1
            else:
                res_t[ch] += 1

        print(res_s, res_t)

        for key_s, value_s in res_s.items():
            if key_s not in res_t.keys():
                return False
            if value_s != res_t[key_s]:
                return False

        return True