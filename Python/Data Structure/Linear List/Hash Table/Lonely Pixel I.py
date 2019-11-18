class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        w, h = len(picture), len(picture[0])
        rows, cols = [0] * w, [0] * h
        for x in range(w):
            for y in range(h):
                if picture[x][y] == 'B':
                    rows[x] += 1
                    cols[y] += 1
        ans = 0
        for x in range(w):
            for y in range(h):
                if picture[x][y] == 'B':
                    if rows[x] == 1:
                        if cols[y] == 1:
                            ans += 1
        return ans
"""
class Solution(object):
    def findLonelyPixel(self, picture):
        return sum(col.count('B') == 1 == picture[col.index('B')].count('B') \
               for col in zip(*picture))
"""