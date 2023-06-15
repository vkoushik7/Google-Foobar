def solution(n):
    # Your code here
    k = int(n)
    i = 0
    while (k>1):
        if (k&1)==0:
            k>>=1
        elif (k&3)==1:
            k-=1
        else:
            k+=1
        i+=1
    return i
print(solution(5))