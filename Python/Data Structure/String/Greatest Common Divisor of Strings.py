import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        size = math.gcd(len(str1), len(str2))   
        return str2[:size] if str2[:size] * (len(str1)//size) == str1 else ""   