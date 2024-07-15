// 2196. Create Binary Tree From Descriptions
import java.util.HashMap;
import java.util.HashSet;
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
    public TreeNode createBinaryTree(int[][] descriptions) {
        // [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
        HashMap<Integer, TreeNode> map = new HashMap<>();
        HashSet<Integer> children = new HashSet<>();
        for (int[] ele : descriptions) {
            int parent = ele[0], child = ele[1], isLeft = ele[2];

            TreeNode parentNode = map.getOrDefault(parent, new TreeNode(parent));
            if (isLeft == 1) {
                parentNode.left = map.getOrDefault(child, new TreeNode(child));
                map.put(child, parentNode.left);
            } else {
                parentNode.right = map.getOrDefault(child, new TreeNode(child));
                map.put(child, parentNode.right);
            }
            children.add(child);
            map.put(parent, parentNode);
        }
        TreeNode root = new TreeNode();
        for (int[] ele : descriptions) {
            if (!children.contains(ele[0])) {
                root = map.getOrDefault(ele[0], new TreeNode(ele[0]));
                break;
            }
        }

        return root;
    }

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
}


public class Create_Binary_Tree_From_Descriptions_2196 {
    
}
