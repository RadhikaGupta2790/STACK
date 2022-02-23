class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items
        # return len(self.items)==0

    def push(self, var):
        self.items.append(var)

    def pop(self):
        return(self.items.pop())

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):  #if you don't add this function the it return the address of the instance
        return str(self.items)

#We use if _ name _ =='__main__'
#so, that it only runs the part of code below it if we run this file,
# if it is called from another file then it only access the class.

if __name__ == '__main__':
    s = Stack()  # create the object and call the constructor
    print(s)
    s.push(3)
    print(s)
    s.push(2)
    print(s.peek())
    s.push(4)
    print(s)
    s.pop()
    print(s)
    print(s.is_empty())


    # o/p with str on
    # []
    # [3]
    # 2
    # [3, 2, 4]
    # [3, 2]

    # o/p with str off
    # <__main__.Stack object at 0x14cf5c663748>
    # <__main__.Stack object at 0x14cf5c663748>
    # 2
    # <__main__.Stack object at 0x14cf5c663748>
    # <__main__.Stack object at 0x14cf5c663748>
