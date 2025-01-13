class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
    
    #Devuelve el valor guardado en el nodo, podria evaluar devolver el nodo
    def front(self):
        if self.head is not None:
            return self.head.data
        else:
            return None
    
    def back(self):
        if self.head is not None:
            temp = self.head
            while temp.next:
                temp = temp.next
            return temp.data
        else:
            return None
    
    #Preferiria usar len pero se mantiene por estandar del curso    
    def size(self):
        temp = self.head
        size = 0
        while temp:
            size+=1
            temp = temp.next
        return size 
    
    #retorna un bool
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def push_front(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def push_back(self,data):
        new_node = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.next = None

    def clear(self):
        if self.head is None:
            return
        else:
            while self.head:
                temp = self.head
                head = self.head.next
                del temp
            return
    def pop_back(self):
        if self.head is None:
            return
        elif self.head.next is None:
            del self.head
            head = None
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            del temp.next
            temp.next = None
    
    def pop_front(self):
        if self.head is not None:
            temp = self.head
            self.head = self.head.next
            del temp 
    #Index va de 0 hasta size-1
    def getitem(self,index):
        if index < self.size:
            temp = self.head
            for _ in range(index+1):
                temp = temp.next
            return temp.data
