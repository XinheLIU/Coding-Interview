class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> res;
        for (int i = 0; i < nums.size(); ++i) {
            int idx = abs(nums[i]) - 1;
            nums[idx] = (nums[idx] > 0) ? -nums[idx] : nums[idx];
        }
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] > 0) {
                res.push_back(i + 1);
            }
        }
        return res;
    }
};



class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> res;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] != nums[nums[i] - 1]) {
                swap(nums[i], nums[nums[i] - 1]);
                --i;
            }
        }
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] != i + 1) {
                res.push_back(i + 1);
            }
        }
        return res;
    }
};

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> res;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            nums[(nums[i] - 1) % n] += n;            
        }
        for (int i = 0; i < n; ++i) {
            if (nums[i] <= n) {
                res.push_back(i + 1);
            }
        }
        return res;
    }
};