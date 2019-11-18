class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        # to do in O(n) space, use the fact that 
        # start from any point in a cycle would have yield the same length
        # for visted ones, we do not need to visit again
        # swap to the array in place while you are counting
        n, ret = len(nums), 0
        for i in range(n):
            cnt = 1
            while nums[i] != i:
                # swap
                j = nums[i]
                nums[i], nums[j] = nums[j], nums[i]
                cnt += 1
            ret = max(cnt, ret)
        return ret        
'''
# official ans
public class Solution {
    public int arrayNesting(int[] nums) {
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != Integer.MAX_VALUE) {
                int start = nums[i], count = 0;
                while (nums[start] != Integer.MAX_VALUE) {
                    int temp = start;
                    start = nums[start];
                    count++;
                    nums[temp] = Integer.MAX_VALUE;
                }
                res = Math.max(res, count);
            }
        }
        return res;
    }
}
'''      