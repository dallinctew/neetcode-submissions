class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for character in s:
            if d.get(character):
                d[character] += 1
            else:
                d.update({character: 1})
        for character in t:
            if d.get(character):
                d[character] -= 1
            else:
                return False
        for v in d:
            if d[v] != 0:
                return False
        return True