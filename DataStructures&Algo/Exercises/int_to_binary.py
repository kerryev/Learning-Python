class Stack():
    def __init__(self):
        self.items = [] #Initailized list

    def push(self, item):
        self.items.append(item) #Adds item to dataset/stack		

    def pop(self):
        return self.items.pop() #Removes item at the top of the stack

    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty(): #Peek reads the top value in the data set 
            return self.items[-1]

    def get_stack(self):
        return self.items

#---------------------------------------------

def binary_conversion(stack, num):

    while num != 0:
        mod_2 = num % 2
        num = int(num / 2)
        stack.push(mod_2)

    binary = ''
    while not stack.is_empty():
        binary += str(stack.pop())

    return binary


stack = Stack()
print(binary_conversion(stack, 242))
