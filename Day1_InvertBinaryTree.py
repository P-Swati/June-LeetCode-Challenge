######## recursive solution #############
class Solution:
    def rec(self,root):
        if(root==None):
            return None
        # if(not root.left and not root.right):
        #     pass
        lf=root.left
        root.left = self.rec(root.right)
        root.right = self.rec(lf)
        
        return root
    
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        return self.rec(root)
        
########iterative solution (bfs)#############

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if(not root):
            return None
        
        queue=deque()
        
        queue.append(root)
        
        while(queue):
            pop=queue.popleft()
            
            temp=pop.left
            pop.left=pop.right
            pop.right=temp
            
            if(pop.left):
                queue.append(pop.left)
            if(pop.right):
                queue.append(pop.right)
                
        return root
