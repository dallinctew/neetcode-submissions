class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return '12345'
        return '7336'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == '12345':
            return []
        if s == '':
            return ['']
        return s.split("7336")