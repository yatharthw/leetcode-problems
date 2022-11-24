# brute force approach
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        guess, secret = list(guess), list(secret)
        l = len(guess)
        bulls, cows = 0, 0
        for i in range(l):
            if guess[i] == secret[i]:
                bulls += 1
                guess[i], secret[i] = '#', '#'
        for i in range(l):
            if secret[i] != '#' and secret[i] in guess:
                guess[guess.index(secret[i])] = '#'
                secret[i] = '#'
                cows += 1
        return str(bulls)+"A"+str(cows)+"B"
