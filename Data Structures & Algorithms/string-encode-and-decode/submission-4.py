class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(str(len(s)))
            parts.append('#')
            parts.append(s)
        return ''.join(parts)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        n = len(s)
        while i < n:
            j = s.index('#', i)
            length = int(s[i:j])
            j += 1
            result.append(s[j:j+length])
            i = j + length
        return result
