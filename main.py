# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        # Special case: If depth is 1, we need to create a new root
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        # Initialize a queue for BFS
        queue = [(root, 1)]  # (node, current_depth)
        
        # Perform BFS
        while queue:
            current_node, current_depth = queue.pop(0)
            
            # If we are at depth-1, add new nodes at depth
            if current_depth == depth - 1:
                # Save original children
                old_left = current_node.left
                old_right = current_node.right
                
                # Create new nodes with value `val`
                current_node.left = TreeNode(val)
                current_node.right = TreeNode(val)
                
                # Attach old children to new nodes
                current_node.left.left = old_left
                current_node.right.right = old_right
            else:
                # Continue BFS if we haven't reached depth-1
                if current_node.left:
                    queue.append((current_node.left, current_depth + 1))
                if current_node.right:
                    queue.append((current_node.right, current_depth + 1))
        
        return root

# Example usage
if __name__ == "__main__":
    # Create a binary tree
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(5)

    # Solution instance
    solution = Solution()
    
    # Add a row at depth 2 with value 1
    new_root = solution.addOneRow(root, 1, 2)

    # A function to print the tree (for testing purposes)
    def print_tree(node, depth=0):
        if not node:
            return
        print_tree(node.right, depth + 1)
        print("     " * depth + str(node.val))
        print_tree(node.left, depth + 1)

    # Print the updated tree
    print_tree(new_root)
