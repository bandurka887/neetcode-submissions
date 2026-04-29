class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = {}

        for i in s:
            hash[i] = hash.get(i,0) + 1
        
        if len(s) == len(t):
            for n in t:
                if n in hash:
                    hash[n] = hash[n] - 1
                    if hash[n] == 0:
                        del hash[n]
                else:
                    return False
        else:
            return False
        return True