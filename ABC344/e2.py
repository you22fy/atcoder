"""
https://techpr.info/python/singly-linked-list/
https://qiita.com/milk_soyyy/items/aa3d4bd7b55a2e873889
"""
# 双方向リスト

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self, a):
        self.head = None
        self.tail = None
        self.node_dict = {}

        for val in a:
            self.insert(val)

    def insert(self, val, after=None):
        new_node = Node(val)
        self.node_dict[val] = new_node

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            if after == None:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            else:
                after_node = self.node_dict[after]
                new_node.prev = after_node
                new_node.next = after_node.next
                if after_node.next:
                    after_node.next.prev = new_node
                after_node.next = new_node

    def delete(self, val):
        node = self.node_dict.pop(val, None)
        if node:
            if node.prev:
                node.prev.next = node.next
            else:
                self.head = node.next
            if node.next:
                node.next.prev = node.prev
            else:
                self.tail = node.prev

    def cat(self):
        result = []
        node = self.head
        while node:
            result.append(node.val)
            node = node.next
        return result

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())

    linked_list = LinkedList(a)

    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x, y = query[1], query[2]
            linked_list.insert(y, x)
        else:
            x = query[1]
            linked_list.delete(x)

    result = linked_list.cat()
    print(*result)

if __name__ == '__main__':
    main()