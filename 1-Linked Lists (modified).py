class Element():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f'{self.value}\n{self.next}'


class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def append(self, element):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = element
        else:
            self.head = element

    def delete(self, value):
        """ Deletes a node based on a given value """
        if self.head.value == value:
            self.head = self.head.next
        else:
            current = self.head
            while current.next:
                temp_prev = current
                current = current.next
                temp_next = current.next
                
                if current.value == value:
                    temp_prev.next = temp_next


    def insert(self, new_element, position):
        
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        else:
            current = self.head
            counter = 2
            while current:
                if counter == position:
                    temp_prev = current
                    temp_next = current.next
                    temp_prev.next = new_element
                    new_element.next = temp_next

                current = current.next
                counter += 1

    def get_position(self, position):
        current = self.head
        counter = 1
        found_value = None
        while current:
            if position == counter:
                found_value = current.value
            
            counter += 1
            current = current.next

        return found_value        

    def __str__(self):
        current = self.head
        chain = ''
        while current:
            chain += str(current.value)+' -> '
            current = current.next
        return chain + 'None'


element1 = Element(2)
element2 = Element(4)
element3 = Element(5)
element4 = Element(9)


link1 = LinkedList(element1)
#link1.append()
link1.append(element2)
link1.append(element3)
print("Created linked list: ", link1)

link1.delete(2)
print("Linked list after deletion: ", link1)

link1.insert(element4, 3)
print("Linked list after insertion: ", link1)

print(link1.get_position(1))








                
