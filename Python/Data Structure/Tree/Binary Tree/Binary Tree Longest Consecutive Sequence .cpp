**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int longest;
    int helper(TreeNode* root) {
       if (!root) 
          return 0;
       int left = helper(root->left);
       int right = helper(root->right);

       int sublongest = 1; //at least we have the root
       if (root->left && root->val + 1 == root->left->val)
            sublongest = max(sublongest, 1 + left);
       if (root->right && root->val + 1 == root->right->val)
            sublongest = max(sublongest, 1 + right);
            
       longest = max(longest, sublongest);
       return sublongest;
    }
    int longestConsecutive(TreeNode* root) {
        longest = 0;
        helper(root);
        return longest;
    }
};


// // // version 2: Another Traverse + Divide Conquer 

// public class Solution {
//     private int longest;
    
//     /**
//      * @param root the root of binary tree
//      * @return the length of the longest consecutive sequence path
//      */
//     public int longestConsecutive(TreeNode root) {
//         return helper(root, null, 0);
//     }
    
//     private int helper(TreeNode root, TreeNode parent, int lengthWithoutRoot) {
//         if (root == null) {
//             return 0;
//         }
        
//         int length = (parent != null && parent.val + 1 == root.val)
//             ? lengthWithoutRoot + 1
//             : 1;
//         int left = helper(root.left, root, length);
//         int right = helper(root.right, root, length);
//         return Math.max(length, Math.max(left, right));
//     }
// }

// // version 3: Divide Conquer
// public class Solution {
//     private class ResultType {
//         int maxInSubtree;
//         int maxFromRoot;
//         public ResultType(int maxInSubtree, int maxFromRoot) {
//             this.maxInSubtree = maxInSubtree;
//             this.maxFromRoot = maxFromRoot;
//         }
//     }
//     /**
//      * @param root the root of binary tree
//      * @return the length of the longest consecutive sequence path
//      */
//     public int longestConsecutive(TreeNode root) {
//         return helper(root).maxInSubtree;
//     }
    
//     private ResultType helper(TreeNode root) {
//         if (root == null) {
//             return new ResultType(0, 0);
//         }
        
//         ResultType left = helper(root.left);
//         ResultType right = helper(root.right);
        
//         // 1 is the root itself.
//         ResultType result = new ResultType(0, 1);
        
//         if (root.left != null && root.val + 1 == root.left.val) {
//             result.maxFromRoot = Math.max(
//                 result.maxFromRoot,
//                 left.maxFromRoot + 1
//             );
//         }
        
//         if (root.right != null && root.val + 1 == root.right.val) {
//             result.maxFromRoot = Math.max(
//                 result.maxFromRoot,
//                 right.maxFromRoot + 1
//             );
//         }
        
//         result.maxInSubtree = Math.max(
//             result.maxFromRoot,
//             Math.max(left.maxInSubtree, right.maxInSubtree)
//         );
        
//         return result;
//     }
// }