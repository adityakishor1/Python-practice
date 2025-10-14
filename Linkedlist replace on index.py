class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def swap_even_positions(self):
        index = 1  # 1-based index
        temp = self.head
        prev_even = None  # Store the previous even node

        while temp:
            if index % 2 == 0:  # Even index
                if prev_even:  # Swap data with previous even
                    prev_even.data, temp.data = temp.data, prev_even.data
                    prev_even = None  # Reset after swap
                else:
                    prev_even = temp  # Store first even node
            temp = temp.next
            index += 1

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")


# Create linked list 1 to 6
ll = LinkedList()
for i in range(1, 7):
    ll.append(i)

print("Before swap:")
ll.display()

ll.swap_even_positions()

print("After swap:")
ll.display()
