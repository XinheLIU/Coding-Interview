class Solution(object):
	def reverseWords(self, s):
    	"""
    	input: string input
    	return: string
   	 	"""
   		if not s:
      		return s
    	array, end = list(s), 0
    	# remove second spaces
    	for i in range(len(array)):
      		if array[i] == ' ' and (i == 0 or array[i - 1] == ' '):
        		continue
      		array[end] = array[i]
      		end += 1
    	# remove trailling spaces
   	    if end > 0 and array[end - 1] == ' ':
      		end -= 1
    	# reverse the whole array first
    	self.reverse(array, 0, end - 1)
    	# reverse each words
    	for i in range(end):
      		if array[i] != ' ' and (i == 0 or array[i - 1] ==' '):
        		start = i
      		if array[i] != ' ' and (i == end - 1 or array[i + 1] == ' '):
        		self.reverse(array, start, i)
    	return ''.join(array[:end])

 	 def reverse(self, array, l, r):
    	while l < r:
      		array[l], array[r] = array[r], array[l]
      		l += 1
      		r -= 1
'''
  def reverseWords(self, s):
        return ' '.join(reversed(s.strip().split()))
'''
	