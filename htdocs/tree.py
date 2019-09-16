
# 遍历

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def pre_order(root_node):
        if not root_node:
            return
        print root_node.val
        pre_order(root_node.left)
        pre_order(root_node.right)

    def mid_order(root_node):
        if not root_node:
            return
        mid_order(root_node.left)
        print root_node.val
        mid_order(root_node.right)

    def post_order(root_node):
        if not root_node:
            return
        post_order(root_node.left)
        post_order(root_node.right)
        print root_node.val

# 快排
def quick_sort(a, left, right):
    if left > right:
        return
    temp = a[left]
    i = left
    j = right
    while i!=j:
        while a[j] >=temp and j>i:
            j-=1
        while a[i] <=temp and j> i:
            i+=1
        if i <j:
            swap(a[i], a[j])
        a[left]=a[i]
        a[i]=temp
        quicksort(left,i-1)
        quicksort(i+1,right)

# 二分 递归
# alist [2,3,5,6,4] item 3
def binary_search_2(alist, item):
    n = len(alist)
    if 0 == n:
        return False
    mid = n / 2
    if alist[mid] == item:
        return True
    elif item < alist[mid]:
        return binary_search_2(alist[:mid], item)
    else:
        return binary_search_2(alist[mid + 1:], item)