from Stack_Implentation import Stack

def rev_string(inp,my_stack):
    the_reversed = ''
    for i in range(len(inp)):
        my_stack.push(inp[i])
    while not my_stack.is_empty():
        curr = my_stack.pop()
        the_reversed+=curr
    return the_reversed

input_string = "leekahs"
my_stack = Stack()
print(rev_string(input_string,my_stack))
