# -*- coding: utf-8 -*-

import sys
import os.path



class BinaryTreeNode():
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    
    def getValue(self):
        return self.value
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right



class BinaryTree():
    def __init__(self, root_value = None):
        if root_value == None:
            self.root = None
        else:
            self.root = BinaryTreeNode(root_value)
        self.current = self.root
    
    def getValue(self):
        return self.current.getValue()
    
    def getLeft(self):
        return self.current.getLeft()
    
    def getRight(self):
        return self.current.getRight()
    
    def goLeft(self):
        if self.current.left == None:
            pass
        else:
            self.current = self.current.left
    
    def goRight(self):
        if self.current.right == None:
            pass
        else:
            self.current = self.current.Right
    
    def addLeft(self, left_value):
        if self.current.left != None:
            pass
        else:
            self.current.left = BinaryTreeNode(left_value)
    
    def addRight(self, right_value):
        if self.current.right != None:
            pass
        else:
            self.current.right = BinaryTreeNode(right_value)
    
    def preorderTraversal(self, node):
        if node == None:
            return
        yield node
        self.preorderTraversal(node.left)
        self.preorderTraversal(node.right)
    
    def initTree_layer(self, f):
        pass



def HeapSort(f):
    pass




def InputArr():
    try:
        infile = open(os.path.join(sys.path[0], 'sort.in'), 'r')
        f = [int(i) for i in infile.read().split()]
        infile.close()
    except IOError:
        f = [int(i) for i in input().split()]

    return f



def OutputArr(f):
    try:
        outfile = open(os.path.join(sys.path[0], 'sort.out'), 'w')
        for i in range(len(f) - 1):
            outfile.write(str(f[i]) + ' ')
        outfile.write(str(f[-1]))
        outfile.close()
    except IOError:
        for i in range(len(f)):
            print(f[i])



if __name__ == "__main__":
    f = InputArr()
    HeapSort(f)
    OutputArr(f)
