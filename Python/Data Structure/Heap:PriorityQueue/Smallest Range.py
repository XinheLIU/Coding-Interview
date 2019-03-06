class Solution(object):
  def smallestRange(self, arrays):
    """
    input: int[][] arrays
    return: int[]
    """
    import heapq
    heap, n, maxv = [], len(arrays), float('-inf')
    for i in range(n):
      # the fist element to heap
      if len(arrays[i]):
        heap.append((arrays[i][0], i, 0))
        maxv = max(maxv, arrays[i][0])
    heapq.heapify(heap)
    ret = [float('-inf'), maxv]
    while len(heap) == n:
      minv, index_a, index_i = heapq.heappop(heap)
      if maxv - minv < ret[1] - ret[0]:
        ret = [minv, maxv]
      # insert next element
      if index_i + 1 < len(arrays[index_a]):
        maxv = max(arrays[index_a][index_i + 1], maxv)
        heapq.heappush(heap, (arrays[index_a][index_i + 1], index_a, index_i + 1))
    return ret