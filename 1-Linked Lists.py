class Element():
    def __init__(self, value):
        self.value = value
        self.next_element = None

    def __str__(self):
        return f'{self.value}\n{self.next_element}'


class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def append(self, element):
        if self.head:
            current = self.head
            while current.next_element:
                current = current.next_element
            current.next_element = element
        else:
            self.head = element

    def delete(self, find_val):
        """ Deletes a node based on a given value """
        if self.head.value == find_val:
            self.head = self.head.next_element
        else:
            current = self.head
            while current.next_element:
                temp_prev = current
                current = current.next_element
                temp_next = current.next_element
                
                if current.value == find_val:
                    temp_prev.next_element = temp_next


    def insert(self, new_element, position):
        
        if position == 1:
            new_element.next_element = self.head
            self.head = new_element
        else:
            current = self.head
            counter = 2
            while current:
                if counter == position:
                    temp_prev = current
                    temp_next = current.next_element
                    temp_prev.next_element = new_element
                    new_element.next_element = temp_next

                current = current.next_element
                counter += 1

    def get_position(self, position):
        current = self.head
        counter = 1
        found_value = None
        while current:
            if position == counter:
                found_value = current.value
            
            counter += 1
            current = current.next_element

        return found_value        

    def __str__(self):
        current = self.head
        chain = ''
        while current:
            chain += str(current.value)+' -> '
            current = current.next_element
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








                
