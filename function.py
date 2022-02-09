from class_stack import Stack

def balans(my_string: str):
    s = Stack()
    index = 0
    while index < len(my_string):
        el_st = my_string[index]
        if (el_st == ')' or el_st == ']' or el_st == '}') and index == 0:
            return print('Несбалансировано')
        elif el_st == ')' and s.peek() == '(':
            s.pop()
        elif el_st == '}'and s.peek() == '{':
            s.pop()
        elif el_st == ']' and s.peek() == '[':
            s.pop()
        else:
            s.push(0, el_st)
        index = index + 1
    if s.isEmpty() == False:
        return print('Сбалансировано')
    else:
        return print('Несбалансировано')
