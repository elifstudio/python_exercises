def longestPalindrome(str):
    if len(str) == 1:
        return str
    else:
        pal = str[:1]
        for j, _ in enumerate(str):
            i = j
            while i < len(str):
                tmpSlice = str[j : (i + 1)]
                reversedSlice = tmpSlice[::-1]
                if (tmpSlice == reversedSlice) and (len(tmpSlice) > len(pal)):
                    pal = tmpSlice
                i += 1
        return pal


# ----------------------------------------------------------------------------------------


def extraLongFactorials(n):
    if n == 1:
        return n
    return n * extraLongFactorials(n - 1)


# ----------------------------------------------------------------------------------------

myList = list(range(10))
listToStr = " ".join(map(str, myList))
exist = "1 2 3" in listToStr

# -----------------------------------------------------------------------------------------


class Node:
    def __init__(self, key):
        self.val = key
        self.next = None


def printLinkedList(head):
    result = ""
    currNode = head
    while currNode != None:
        result += str(currNode.val) + "->"
        currNode = currNode.next
    result += "None"
    print(result)


def generateLinkedList(items):
    head = Node(items[0])
    currNode = head
    for i in range(len(items) - 1):
        currNode.next = Node(items[i + 1])
        currNode = currNode.next
    return head


def mergeLinkedList(head1, head2):
    curr1 = head1
    curr2 = head2
    head = Node(None)
    currNode = head
    while curr1 != None:
        currNode.next = Node(curr2.val) if curr1.val > curr2.val else Node(curr1.val)
        currNode.next.next = (
            Node(curr1.val) if curr1.val > curr2.val else Node(curr2.val)
        )
        currNode = currNode.next.next
        curr1 = curr1.next
        curr2 = curr2.next
    return head.next


""" mylist1 = [0, 1, 2, 4, 5, 6]
myList2 = [1, 1, 3, 5, 6, 9]
head1 = generateLinkedList(mylist1)
head2 = generateLinkedList(myList2)
printLinkedList(head1)
printLinkedList(head2)
myHead = mergeLinkedList(head1, head2)
printLinkedList(myHead) """

# ---------------------------------------------------------------------------
