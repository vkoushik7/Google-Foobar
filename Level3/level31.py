def solution(x, y):
    # Your code here
    a = int(x)
    b = int(y)
    c = 0
    if (a==1 or b==1):
        if (b==1):
            return str(a-1)
        else:
            return str(b-1)
    else:
        if (a>b):
            c = a//b
            a = a%b
        else:
            c = b//a
            b = b%a

    while(a>0 and b>0):
        if (a>b):
            a = a-b
        else:
            b = b-a
        c = c+1
        if (a==1 and b==1):
            return str(c)
    if (a!=1 and b!=1):
        return "impossible"
    return str(c)
x = input()
y = input()
print(solution(x,y))
