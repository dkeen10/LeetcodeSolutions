#LeetCode 876
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_val):
        new_node = ListNode(new_val)
        new_node.next = self.head
        self.head = new_node

class Solution:
    def middleNode(self, head):
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
            return arr[len(arr) // 2]
        

def main():
    solution = Solution()
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)

    print(solution.middleNode(llist))


if __name__ == "__main__":
    main()