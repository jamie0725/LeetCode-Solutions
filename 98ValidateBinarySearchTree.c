/*
 * Given a binary tree, determine if it is a valid binary search tree (BST).
 * Assume a BST is defined as follows:
 * The left subtree of a node contains only nodes with keys less than the node's key.
 * The right subtree of a node contains only nodes with keys greater than the node's key.
 * Both the left and right subtrees must also be binary search trees.
 */


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool isValidBST(struct TreeNode* root) {
    if(root == NULL){
        return true;
    }
    if((*root).left != NULL){
        struct TreeNode* current = (*root).left;
        while((*current).right != NULL){
            current = (*current).right;
        }
        if((*current).val >= (*root).val){
            return false;
        }
    }
    if((*root).right != NULL){
        struct TreeNode* current = (*root).right;
        while((*current).left != NULL){
            current = (*current).left;
        }
        if((*current).val <= (*root).val){
            return false;
        }
    }
    if(!isValidBST((*root).left)){
        return false;
    }
    if(!isValidBST((*root).right)){
        return false;
    }
    return true;
}

