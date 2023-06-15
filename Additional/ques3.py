#Distract the Trainers
'''
Distract the Trainers=====================

The time for the mass escape has come, and you need to distract the bunny trainers so that the workers can make it out! Unfortunately for you, they're watching the bunnies closely. Fortunately, this means they haven't realized yet that the space station is about to explode due to the destruction of the LAMBCHOP doomsday device. Also fortunately, all that time you spent working as first a minion and then a henchman means that you know the trainers are fond of bananas. And gambling. And thumb wrestling.The bunny trainers, being bored, readily accept your suggestion to play the Banana Games.You will set up simultaneous thumb wrestling matches. In each match, two trainers will pair off to thumb wrestle. The trainer with fewer bananas will bet all their bananas, and the other trainer will match the bet. The winner will receive all of the bet bananas. You don't pair off trainers with the same number of bananas (you will see why, shortly). You know enough trainer psychology to know that the one who has more bananas always gets over-confident and loses. Once a match begins, the pair of trainers will continue to thumb wrestle and exchange bananas, until both of them have the same number of bananas. Once that happens, both of them will lose interest and go back to supervising the bunny workers, and you don't want THAT to happen!For example, if the two trainers that were paired started with 3 and 5 bananas, after the first round of thumb wrestling they will have 6 and 2 (the one with 3 bananas wins and gets 3 bananas from the loser). After the second round, they will have 4 and 4 (the one with 6 bananas loses 2 bananas). At that point they stop and get back to training bunnies.How is all this useful to distract the bunny trainers? Notice that if the trainers had started with 1 and 4 bananas, then they keep thumb wrestling! 1, 4 -> 2, 3 -> 4, 1 -> 3, 2 -> 1, 4 and so on.Now your plan is clear. You must pair up the trainers in such a way that the maximum number of trainers go into an infinite thumb wrestling loop!Write a function solution(banana_list) which, given a list of positive integers depicting the amount of bananas the each trainer starts with, returns the fewest possible number of bunny trainers that will be left to watch the workers. Element i of the list will be the number of bananas that trainer i (counting from 0) starts with.The number of trainers will be at least 1 and not more than 100, and the number of bananas each trainer starts with will be a positive integer no more than 1073741823 (i.e. 2^30 -1). Some of them stockpile a LOT of bananas.

Languages=========
To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases==========
Your code should pass the following test cases.Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:solution.solution([1, 7, 3, 21, 13, 19])Output:    0

Input:solution.solution(1,1)Output:    2
-- Java cases --
Input:solution.solution(1,1)Output:    2

Input:Solution.solution([1, 7, 3, 21, 13, 19])Output:    0
'''
from math import gcd

def loops(x, y):
    res = (x+y)/gcd(x,y)
    return bool(res & (res - 1))

def remove(guards, ref):
    for i in range(len(guards)):
        j = 0 
        while j < len(guards[i]):
            if(guards[i][j]==ref):
                guards[i].pop(j)
            j+=1 
    guards[ref]=[-1]

def solution(banana_list):
    #Your code here
    guards= [[] for i in range(len(banana_list))]
    bad=0
    
    for i in range(len(guards)):
        for j in range(len(guards)):
            if(loops(banana_list[i], banana_list[j])):
                guards[i].append(j)

    to_process=len(banana_list)
    while(to_process>0):

        min_num=0
        for i in range(len(guards)):
            if(i!=0 and (len(guards[i])<len(guards[min_num]) or guards[min_num]
                == [-1]) and guards[i]!=[-1]):
                min_num=i

        if((len(guards[min_num])) == 0 or (len(guards[min_num])==1 and
                guards[min_num][0] == guards[min_num]) and guards[min_num] !=
                [-1]):
            remove(guards, min_num)
            to_process-=1
            bad+=1
        else:
            min_node=guards[min_num][0]
            for i in range(len(guards[min_num])):
                if(i!=0 and guards[min_num][i]!=min_num and len(guards[guards[min_num][i]])<len(guards[min_node])):
                    min_node=guards[min_num][i]
            if(guards[min_node]!=[-1]):
                remove(guards, min_num)
                remove(guards, min_node)
                to_process-=2

    return bad
