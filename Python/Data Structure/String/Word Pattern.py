class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if  len(words) != len(pattern):
            return False
        map = {}
        for i,c in enumerate(pattern):
            if c not in map:
                map[c] = words[i]
            else:
                if map[c] != words[i]:
                    return False
        num_p, num_w = len(map),len(set(map.values()))
        # if it is one-to-one
        return num_p == num_w