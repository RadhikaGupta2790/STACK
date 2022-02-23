
import stack

string = ".sruoy ydaerla s'tI"
reverse_string =""

s = stack.Stack()

for char in string:
    s.push(char)

while not s.is_empty():
    reverse_string += s.pop()

#using stacks
print(reverse_string)

#direct using indices
print(string[::-1])

