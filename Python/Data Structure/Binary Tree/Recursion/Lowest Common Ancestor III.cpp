/*

Given two nodes in a binary tree, find their lowest common ancestor (the given two nodes are not guaranteed to be in the binary tree).

Return null If any of the nodes is not in the tree.

Assumptions

There is no parent pointer for the nodes in the binary tree

The given two nodes are not guaranteed to be in the binary tree

Examples

        5

      /   \

     9     12

   /  \      \

  2    3      14

The lowest common ancestor of 2 and 14 is 5

The lowest common ancestor of 2 and 9 is 9

The lowest common ancestor of 2 and 8 is null (8 is not in the tree)


*/

//class TreeNode {
// public:
//  int value;
//  TreeNode* left;
//  TreeNode* right;
//  TreeNode(int v) : value(v), left(NULL), right(NULL) {}
//};
class Solution {
private:
  bool find(TreeNode* root, TreeNode* p) {
    //base caser
    if (p == NULL) return false;
    if (root == NULL) return false;
    if (root == p) return true;
    if (find(root->left, p)) return true;
    if (find(root->right, p)) return true;
    return false;
  }
  TreeNode* LCA(TreeNode* root, TreeNode* one, TreeNode* two) {
    if (root == NULL) return NULL;
    if (root == one || root == two) return root;
    TreeNode* left = LCA(root->left, one, two);
    TreeNode* right = LCA(root->right, one, two);
    if (left && right) return root;
    return left ? left : right;
  }
 public: 
  TreeNode* solve(TreeNode* root, TreeNode* one, TreeNode* two) {
    //base case
    if (root == NULL) return NULL;
    if (find(root, one) && find(root, two)) {
      return LCA(root, one, two);
    } else {
      return NULL;
    }
  }
};