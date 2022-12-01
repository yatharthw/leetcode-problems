# niave counter hash
class Solution:
def halvesAreAlike(self, s: str) -> bool:
    s = s.upper()
    l = len(s)
    a = Counter(s[:l//2])
    b = Counter(s[l//2:])
    if a.get('A', 0)+a.get('E', 0)+a.get('I', 0)+a.get('O', 0)+a.get('U', 0) == b.get('A', 0)+b.get('E', 0)+b.get('I', 0)+b.get('O', 0)+b.get('U', 0):
        return True
    return False

# two pointer
def halvesAreAlike(self, s: str) -> bool:
    vowels = set('aeiouAEIOU')
    a = b = 0
    i, j = 0, len(s) - 1
    while i < j:
        a += s[i] in vowels
        b += s[j] in vowels
        i += 1
        j -= 1
    return a == b
