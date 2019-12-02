# -*- coding: utf-8 -*-


class BST_Node():
    def __init__(self, parent, value):
        """BST节点类初始化"""
        self.parent = parent
        self.value = value
        self.left = None
        self.right = None
        

    def insert(self, value):
        """插入节点"""
        if value < self.value:                      #比当前节点小
            if self.left == None:
                self.left = BST_Node(self, value)
                return self.left
            else:
                self.left.insert(value)
        else:                                       #大于或等于当前节点
            if self.right == None:
                self.right = BST_Node(self, value)
                return self.right
            else:
                self.right.insert(value)



class BST_Tree():
    def __init__(self):
        """BST初始化"""
        self.root = None
        
    def insert(self, value):
        """插入节点"""
        if self.root == None:
            self.root = BST_Node(None, value)
        else:
            self.root.insert(value)


    def pre_order(self, x):
        """前序遍历"""
        if x== None:
            return
        print(x.value, end = ' ')               #先输出父节点，再递归左右子树
        self.pre_order(x.left)
        self.pre_order(x.right)


    def in_order(self, x):
        """中序遍历"""
        if x== None:
            return
        self.in_order(x.left)
        print(x.value, end = ' ')               #先递归左子树，再输出父节点，最后再递归右子树
        self.in_order(x.right)


    def post_order(self, x):
        """后序遍历"""
        if x== None:
            return
        self.post_order(x.left)
        self.post_order(x.right)
        print(x.value, end = ' ')               #先递归左右子树，再输出父节点


    def delete_node(self, x :BST_Node):
        """删除节点"""
        if x != None:                           #若删除的节点不为None
            if x.right != None:                 #若右子树不为空则查找右子树中的最小节点
                p = self.find_min(x.right)
                x.value = p.value
                self.delete_node(p)
            elif x.left != None:                #若右子树为空，左子树不为空，直接把左子树替换原删除节点
                if x.parent == None:
                    x.left.parent = None
                    return x.left
                else:
                    p = x.left
                    if x.parent.left == x:
                        x.parent.left = p
                    else:
                        x.parent.right = p
                    p.parent = x.parent
            else:                               #若左右子树均为空则直接删除
                if x.parent != None:
                    if x.parent.left == x:
                        x.parent.left = None
                    else:
                        x.parent.right = None


    def delete(self, value):
        """删除对应value值的节点（只能删除第一个查到的节点）"""
        self.delete_node(self.find(value))      #先查找对应值的节点，再调用删除指定节点的方法



    def find(self, value):
        """查找对应value值的节点"""
        p = self.root
        while (p != None):                      #利用树实现分治查找
            if (value < p.value):
                p = p.left
            elif (value > p.value):
                p = p.right
            else:
                return p
        return None
    

    def find_min(self, x):
        """查找x子树中的最小节点"""
        if x == None:
            x = self.root                       #若没有指定子树则查找整棵数的最小节点
        while (x.left != None):
            x = x.left
        return x
    

    def find_max(self, x):
        """查找x子树中的最大节点"""
        if x == None:
            x = self.root                       #若没有指定子树则查找整棵数的最大节点
        while (x.right != None):
            x = x.right
        return x


    def find_nextSmaller(self, x):
        """查找指定节点x的次小节点"""
        if x == None:
            return self.find_max(None)
        else:
            if x.left != None:                  #若左子树不为空，则找左子树中的最大节点
                return self.find_max(x.left)
            else:                               #若左子树为空，则往上找第一个右折的节点
                p = x
                while (p.parent != None):
                    if (p.parent.left == p):
                        p = p.parent
                    else:
                        return p.parent
                return None


    def find_nextLarger(self, x):
        """查找指定节点x的次大节点"""
        if x == None:
            return self.find_min(None)
        else:
            if x.right != None:                 #若右子树不为空，则找右子树中的最小节点
                return self.find_min(x.right)
            else:                               #若右子树为空，则往上找第一个左折的节点
                p = x
                while (p.parent != None):
                    if (p.parent.right == p):
                        p = p.parent
                    else:
                        return p.parent
                return None
    

    def output_order_des(self):
        """利用查找次小节点方法降序输出序列"""
        p = self.find_max(None)
        while (p != None):
            print(p.value, end = ' ')
            p = self.find_nextSmaller(p)
    

    def output_order_asc(self):
        """利用查找次小节点方法升序输出序列"""
        p = self.find_min(None)
        while (p != None):
            print(p.value, end = ' ')
            p = self.find_nextLarger(p)
    

    def trim(self, x, minVal, maxVal):
        """修剪指定x节点为根节点的子树"""
        if x == None:
            return
        self.trim(x.left, minVal, maxVal)           #左子树递归
        self.trim(x.right, minVal, maxVal)          #右子树递归
        if x.value < minVal or x.value > maxVal:    #保留临界值
            self.delete_node(x)                     #删除不在指定范围内的节点






if __name__ == "__main__":
    #建树
    tree = BST_Tree()

    #插入测试
    tree.insert(23)
    tree.insert(2)
    tree.insert(66)
    tree.insert(34)
    tree.insert(11)
    tree.insert(77)
    tree.insert(30)
    tree.insert(15)
    tree.insert(44)
    tree.insert(1)
    tree.insert(33)

    
    #				  23
    #			   /       \
    #			 2          66
    #           / \        /  \
    #          1   11     34   77
    #               \     / \
    #               15   30  44
    #                      \
    #                      33

    print("pre order:", end = "\t")
    tree.pre_order(tree.root); print()      #先序遍历
    print("in order:", end = "\t")
    tree.in_order(tree.root); print()       #中序遍历
    print("post order:", end = "\t")
    tree.post_order(tree.root); print()     #后序遍历
    print("asc order:", end = "\t")
    tree.output_order_asc(); print()        #升序输出
    print("des order:", end = "\t")
    tree.output_order_des(); print()        #降序输出



    print()



    #删除测试
    print("before delelte 34:", end = '\t')
    print(tree.find(34))                    #删除前先查找34节点
    print("delete 34", end = '\n')
    tree.delete(34)                         #删除34节点
    print("after delelte 34:", end = '\t')
    print(tree.find(34))                    #删除后先查找34节点

    
    #				  23
    #			   /       \
    #			 2          66
    #           / \        /  \
    #          1   11     44   77
    #               \     /
    #               15   30
    #                      \
    #                      33

    print("pre order:", end = "\t")
    tree.pre_order(tree.root); print()      #先序遍历
    print("in order:", end = "\t")
    tree.in_order(tree.root); print()       #中序遍历
    print("post order:", end = "\t")
    tree.post_order(tree.root); print()     #后序遍历
    print("asc order:", end = "\t")
    tree.output_order_asc(); print()        #升序输出
    print("des order:", end = "\t")
    tree.output_order_des(); print()        #降序输出



    print()



    #删除测试
    print("before delelte 44:", end = '\t')
    print(tree.find(44))                    #删除前先查找44节点
    print("delete 44", end = '\n')
    tree.delete(44)                         #删除44节点
    print("after delelte 44:", end = '\t')
    print(tree.find(44))                    #删除后先查找44节点

    
    #				  23
    #			   /       \
    #			 2          66
    #           / \        /  \
    #          1   11     30   77
    #               \       \
    #               15     33

    print("pre order:", end = "\t")
    tree.pre_order(tree.root); print()      #先序遍历
    print("in order:", end = "\t")
    tree.in_order(tree.root); print()       #中序遍历
    print("post order:", end = "\t")
    tree.post_order(tree.root); print()     #后序遍历
    print("asc order:", end = "\t")
    tree.output_order_asc(); print()        #升序输出
    print("des order:", end = "\t")
    tree.output_order_des(); print()        #降序输出



    print()


    
    #插入新的数字，恢复原有结构以便后面测试
    print("insert 25", end = '\n')
    tree.insert(25)
    print("insert 28", end = '\n')
    tree.insert(28)

    
    #				  23
    #			   /       \
    #			 2          66
    #           / \        /  \
    #          1   11     30   77
    #               \    /  \
    #               15  25  33
    #                     \
    #                     28

    print("pre order:", end = "\t")
    tree.pre_order(tree.root); print()      #先序遍历
    print("in order:", end = "\t")
    tree.in_order(tree.root); print()       #中序遍历
    print("post order:", end = "\t")
    tree.post_order(tree.root); print()     #后序遍历
    print("asc order:", end = "\t")
    tree.output_order_asc(); print()        #升序输出
    print("des order:", end = "\t")
    tree.output_order_des(); print()        #降序输出



    print()



    #查找节点30的次大节点
    print("30 next larger:", end = "\t")
    print(tree.find_nextLarger(tree.find(30)).value)

    #查找节点15的次大节点
    print("15 next larger:", end = "\t")
    print(tree.find_nextLarger(tree.find(15)).value)

    #查找节点77的次大节点
    print("77 next larger:", end = "\t")
    print(tree.find_nextLarger(tree.find(77)))



    print()



    #修建树，范围[11, 30]
    print("BST trim [11, 30]", end = "\n")
    tree.trim(tree.root, 11, 30)

    
    #				  23
    #			   /       \
    #			 11         30
    #             \        /  
    #              15     25  
    #                       \
    #                       28

    print("pre order:", end = "\t")
    tree.pre_order(tree.root); print()      #先序遍历
    print("in order:", end = "\t")
    tree.in_order(tree.root); print()       #中序遍历
    print("post order:", end = "\t")
    tree.post_order(tree.root); print()     #后序遍历
    print("asc order:", end = "\t")
    tree.output_order_asc(); print()        #升序输出
    print("des order:", end = "\t")
    tree.output_order_des(); print()        #降序输出



    print()



    #修建树，范围[26, 31]
    print("BST trim [26, 31]", end = "\n")
    tree.trim(tree.root, 26, 31)

    
    #			   30
    #             /  
    #            25  
    #              \
    #              28

    print("pre order:", end = "\t")
    tree.pre_order(tree.root); print()      #先序遍历
    print("in order:", end = "\t")
    tree.in_order(tree.root); print()       #中序遍历
    print("post order:", end = "\t")
    tree.post_order(tree.root); print()     #后序遍历
    print("asc order:", end = "\t")
    tree.output_order_asc(); print()        #升序输出
    print("des order:", end = "\t")
    tree.output_order_des(); print()        #降序输出
    
