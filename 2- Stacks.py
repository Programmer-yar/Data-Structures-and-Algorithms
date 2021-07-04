class Element():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f'{self.value}\n{self.next}'


class Stack():
    def __init__(self, head=None):
        self.head = head

    def push(self, element):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = element
        else:
            self.head = element

    def pop(self):
        """ Deletes the last node """
        if self.head.next == None:
            self.head = None
        else:
            current = self.head
            while current.next:
                temp_prev = current
                current = current.next
            temp_prev.next = None
                
       

    def __str__(self):
        current = self.head
        chain = ''
        while current:
            chain += str(current.value)+' -> '
            current = current.next
        return chain + 'None'

if __name__ == '__main__':

    e1 = Element(2)
    e2 = Element(4)
    e3 = Element(6)

    st1 = Stack(e1)
    st1.push(e2)
    st1.push(e3)
    print('STACK 1:', st1)
    st1.pop()
    print('STACK 1:', st1)
    st1.pop()
    print('STACK 1:', st1)
    st1.pop()
    print('STACK 1:', st1)

