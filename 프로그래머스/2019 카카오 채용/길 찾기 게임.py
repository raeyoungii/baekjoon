import sys

sys.setrecursionlimit(1000000)


class Tree:
    def __init__(self, idx, data):
        self.idx = idx
        self.data = data
        self.left = None
        self.right = None


def make_tree(node, arr, nodeinfo):
    data = max(arr, key=lambda x: x[1])
    left_arr = list(filter(lambda x: x[0] < data[0], arr))
    right_arr = list(filter(lambda x: x[0] > data[0], arr))

    if node.data == data:
        if left_arr:
            make_tree(node, left_arr, nodeinfo)
        if right_arr:
            make_tree(node, right_arr, nodeinfo)
    else:
        if data[0] < node.data[0]:
            node.left = Tree(nodeinfo.index(data), data)
            tmp = node.left
        else:
            node.right = Tree(nodeinfo.index(data), data)
            tmp = node.right

        if left_arr:
            make_tree(tmp, left_arr, nodeinfo)
        if right_arr:
            make_tree(tmp, right_arr, nodeinfo)


def preorder(arr, node):
    arr.append(node.idx + 1)
    if node.left:
        preorder(arr, node.left)
    if node.right:
        preorder(arr, node.right)
    return arr


def postorder(arr, node):
    if node.left:
        postorder(arr, node.left)
    if node.right:
        postorder(arr, node.right)
    arr.append(node.idx + 1)
    return arr


def solution(nodeinfo):
    root_data = max(nodeinfo, key=lambda x: x[1])
    root = Tree(nodeinfo.index(root_data), root_data)

    make_tree(root, nodeinfo, nodeinfo)

    answer = [preorder([], root), postorder([], root)]
    return answer


Nodeinfo = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
print(solution(Nodeinfo))

# 라이언은 아래와 같은 특별한 규칙으로 트리 노드들을 구성한다.
# - 트리를 구성하는 모든 노드의 x, y 좌표 값은 정수이다.
# - 모든 노드는 서로 다른 x값을 가진다.
# - 같은 레벨(level)에 있는 노드는 같은 y 좌표를 가진다.
# - 자식 노드의 y 값은 항상 부모 노드보다 작다.
# - 임의의 노드 V의 왼쪽 서브 트리(left subtree)에 있는 모든 노드의 x값은 V의 x값 보다 작다.
# - 임의의 노드 V의 오른쪽 서브 트리(right subtree)에 있는 모든 노드의 x값은 V의 x값 보다 크다.
