class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        if self.head == None:
            return -1
        elif index < 0:
            return -1
        i = index
        targetNode = self.head
        while (i != 0):
            if targetNode.nextNode == None:
                return -1
            targetNode = targetNode.nextNode
            i -= 1
        return targetNode.val
             

    def insertHead(self, val: int) -> None:
        if (self.head == None) and (self.tail == None):
            firstNode = Node(val)
            self.head = firstNode
            self.tail = firstNode
        else:
            self.head = Node(val, self.head)

    def insertTail(self, val: int) -> None:
        if (self.head == None) and (self.tail == None):
            firstNode = Node(val)
            self.head = firstNode
            self.tail = firstNode
        else:
            self.tail.nextNode = Node(val)
            self.tail = self.tail.nextNode

    def remove(self, index: int) -> bool:
        if self.head == None:
            return False
        elif index < 0:
            return False
        i = index
        prevNode = None
        targetNode = self.head
        while (i != 0):
            if targetNode.nextNode == None:
                return False
            prevNode = targetNode
            targetNode = targetNode.nextNode
            i -= 1
        if i == 0 and (targetNode == self.head):
            self.head = self.head.nextNode
            return True
        elif i == 0 and (targetNode == self.tail):
            self.tail = prevNode
            self.tail.nextNode = None
            return True
        else:
            prevNode.nextNode = targetNode.nextNode
            return True

    def getValues(self) -> List[int]:
        retList = []
        targetNode = self.head
        while (targetNode != None):
            retList.append(targetNode.val)
            targetNode = targetNode.nextNode
        return retList

class Node:
    
    def __init__(self, val: int, nextNode: Node=None):
        self.val = val
        self.nextNode = nextNode
