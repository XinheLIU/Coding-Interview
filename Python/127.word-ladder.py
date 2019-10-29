#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)  # to avoid TLE
        q = deque([beginWord])
        visited = set([beginWord])
        dist = 0
        while q:
            dist += 1
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return dist
                for next_word in self.get_next_words(word):
                    if next_word not in wordList or next_word in visited:
                        continue
                    q.append(next_word)
                    visited.add(next_word)
        return 0
    
    def get_next_words(self, word):
        ret = []
        for i in range(len(word)):
            l, r = word[:i], word[i+1:]
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == c:
                    continue
                ret.append(l + c +r)
        return ret
# @lc code=end

