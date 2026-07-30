OPERATORS = set(['+','-','*','/','(',')','^'])
PRIORITY = {'+':1,'-':1,'*':2,'/':2,'^':3}
def infix_to_postfix(ex):
    stack=[]
    output=" "
    for i in ex:
        if i not in OPERATORS:
            output+=i
        elif i =='(':
            stack.append('(')
        elif i ==')':
            while stack and stack[-1]!='(':
                output+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='(' and PRIORITY[i]<=PRIORITY[stack[-1]]:
                output+=stack.pop()
            stack.append(i)
    while stack:
        output+=stack.pop()
    return output

ex = input("Enter an infix expression:")
print("Infix expression:",ex)
print("Postfix expression:",infix_to_postfix(ex))
