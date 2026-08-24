class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = {}
        for char in magazine:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1    

        for char in ransomNote:
            if char in counts and counts[char] > 0:
                counts[char] -=1
            else:
                return False
        return True        
