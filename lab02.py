from typing import Any

class Node:
    def __init__(self, value, next=None):  # Funkcja, ktora inicjalizuje obiekt Node
        self.value = value  # Przypisuje wartosc
        self.next = next  # Inicjalizuje next jako None


class LinkedList:
    def __init__(self, node=None):  # Funkcja inicjalizujaca glowe i ogon
        self.head = node
        self.tail = node

    # def __str__(self):  # Funkcja printujaca liste
    #     currentNode = self.head
    #     while currentNode is not None:
    #         print(currentNode.value, '->', end=' ')
    #         currentNode = currentNode.next
    #     print("None")

    def __str__(self):
        new_node = self.head
        text = ""
        while new_node.next:
            text += str(new_node.value) + " -> "
            new_node = new_node.next
        text += str(new_node.value)
        return text

    def push(self, value: Any):  # Funkcja wstawiajaca nowy wezel na poczatku listy
        new_node = Node(value)  # Wstawianie wartosci
        new_node.next = self.head  # Ustawia nowy wezel jako glowe
        self.head = new_node  # Przenosi glowe aby wskazac nowy wezel
        if self.tail is None:
            self.tail = self.head

    def node(self, index):
        new_node = self.head
        count = 0

        while new_node:
            if count == index-1:
                return new_node.value
            count += 1
            new_node = new_node.next

    def insert(self, value: Any, after: Node):
        if after is None:
            raise ValueError("Wezel nie nalezy do listy, a ten kod nalezy do Jacka Sosnowskiego")
        new_node = Node(value)
        new_node.next = after.next
        after.next = new_node

    def append(self, value: Any):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
        if self.tail is None:
            self.tail = self.head

    def pop(self):
        node = self.head
        self.head = node.next
        return node

    def remove_last(self):
        new_node = self.head
        while new_node.next.next:
            new_node = new_node.next
        new_node.next = None
        self.tail = new_node
        return self.tail

    def remove(self, after: Any):
        if self.head is None:
            return
        new_node = self.head
        if after == 0:
            self.head = new_node.next
            return
        for i in range(after-1):
            new_node = new_node.next
            if new_node is None:
                break
        if new_node is None:
            return
        if new_node.next is None:
            return
        next = new_node.next.next
        new_node.next = None
        new_node.next = next

    def __len__(self):
        temp = self.head
        count = 0

        while temp:
            count += 1
            temp = temp.next
        return count

class Stack:
    def __init__(self):
        self.storage = LinkedList()

    def __len__(self):
        return len(self.storage)

    def __str__(self):
        stos = self.storage.head
        text = ""
        while stos.next:
            text += str(stos.value) + " -> "
            stos = stos.next
        text += str(stos.value)
        return text

    def push(self, element: Any):
        self.storage.append(element)

    def pop(self):
        if len(self.storage) != 0:
            return self.storage.remove_last().value

class Queue:
    def __init__(self):
        self.storage = LinkedList()

    def __len__(self):
        return len(self.storage)

    def enqueue(self, element: Any):
        self.storage.append(element)

    def dequeue(self):
        if len(self.storage) != 0:
            return self.storage.remove_last().value

    def peek(self):
        if len(self.storage) != 0:
            return self.storage.tail.value

    def __str__(self):
        kju = self.storage.head
        text = ""
        while kju.next:
            text += str(kju.value) + ", "
            kju = kju.next
        text += str(kju.value)
        return text

    # def __str__(self):
    #     strng = ""
    #
    #     for x in range(len(self.storage)):
    #         strng += str(self.storage.node(x).value) + " "
    #
    #     return strng


if __name__ == '__main__':
    ll = LinkedList()

    ll.append(6)
    print((ll.__str__()))
    ll.push(7)
    print((ll.__str__()))
    ll.push(1)
    print((ll.__str__()))
    ll.append(4)
    print((ll.__str__()))
    ll.insert(8, ll.head)
    print((ll.__str__()))
    ll.pop()
    print((ll.__str__()))
    ll.remove_last()
    print((ll.__str__()))
    ll.remove(1)
    print((ll.__str__()))

    print(ll.node(1))


    queue = Queue()
    queue.enqueue("Projekty")
    queue.enqueue("Z Pythona")
    queue.enqueue("są")
    queue.enqueue("w pyte")
    print(queue.__str__())
    print(queue.dequeue())
    queue.dequeue()
    print(queue.__str__())
    print(queue.__len__())
    print(queue.peek())

    stack = Stack()
    stack.push(31)
    print(stack.__str__())
    stack.push(69)
    print(stack.__str__())
    stack.push(77)
    print(stack.__str__())
    stack.pop()
    print(stack.__str__())

    # def node(self, at: int):
    #     if at < 0:
    #         raise ValueError("podano indeks mniejszy od 0")
    #
    #     if len(self) > at:
    #         new_node = self.head
    #     for x in range(at):
    #         new_node = new_node.next
    #     else:
    #         raise ValueError("TEST123")
    #     return node

    # def insert(self, value: Any, after: Node):
    #     if after == None:
    #         raise ValueError("Wezel nie nalezy do listy")
    #         return
    #     node = Node(value)
    #     node.next = after.next
    #     after.next = node

    # def insert(self, value: Any, after: Node) -> None:
    #     new_node = self.head
    #     if after == self.head:
    #         node = Node(value, new_node.next)
    #         self.head.next = node
    #         return
    #     while new_node is not None:
    #         new_node = new_node.next
    #         if new_node == after:
    #             node = Node(value, new_node.next)
    #             new_node.next = node
