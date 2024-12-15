/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    

    private boolean isBalanced = true;

    public boolean isBalanced(TreeNode root){
        if(root == null) return true;
        if( Math.abs(maxHeight(root.left) - maxHeight(root.right)) > 1)
            return false;
        return isBalanced(root.left) && isBalanced(root.right);
       
    }

    private void dfs(TreeNode root) {
        if (root == null) {
            return ;
        }
        if( Math.abs(maxHeight(root.left) - maxHeight(root.right)) > 1)
            this.isBalanced = false;
        dfs(root.left);
        dfs(root.right);

    }




    private int maxHeight(TreeNode root){
        if(root == null) return 0;
        return 1+Math.max(maxHeight(root.left),maxHeight(root.right));
    }

}