# Stack data structure - reranges the values in a dataset

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

myStack = Stack()
myStack.push("A")
myStack.push("B")
print(myStack.get_stack())
myStack.push("C")
print(myStack.get_stack())
myStack.pop() #Since C is pushed last, it will be removed first from the dataset
print(myStack.get_stack())
print(myStack.is_empty()) #Will return false since there is items in the dataset
print(myStack.peek()) #Returns top value in dataset

#----------------------------------------------------------------------------------

#Balanced vs. Unbalanced Brackets

#([]) -- Balanced
#'(', then '[', then ']', then ')'
#After iterating through this dataset, there is no non - empty stacks

#(() -- Unbalanced
#Even after iterating through this dataset, there is still a non-empty stack

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
                    break
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False

print("String : (((({})))) Balanced or not?")
print(is_paren_balanced("(((({}))))")) #Balanced

print("String : [][]]] Balanced or not?")
print(is_paren_balanced("[][]]]")) #Not balanced

print("String : [][] Balanced or not?")
print(is_paren_balanced("[][]")) #Balanced

#----------------------------------------------------------------------

#Reverse string

input_str = "Educative"
print(input_str[::-1])

#Using algorithm/stack method:

def reverse_string(stack, input_str):
    
    for i in range(len(input_str)):
        stack.push(input_str[i])
    string = ''
    while not stack.is_empty():
        string += stack.pop()

    return string

stack = Stack()
input_str = "!olleH"
print(reverse_string(stack, input_str))

#-----------------------------------------------------------------------

