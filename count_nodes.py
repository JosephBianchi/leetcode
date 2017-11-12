# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from extratypes import Tree  # library with types used in the task


def solution(T):
    if (T == None):
        return 0;
    return solution(T.l) + solution(T.r) + 1



'''
(1)using recursion have the function check if the nodes == None
(2)return 0 if so
(3)else recurse:

left side from node and two node children
sol(5)
sol(3) + sol(10) + 1
sol(20) + sol(21) + 1
sol(None)or0 + sol(None)or0 + 1
sol(None)or0 + sol(None)or0 + 1
(((0 + 0 + 1(2)) + 1) + 1)

right side from node
sol(1) + sol(None)or0 + 1
sol(None) + sol(None)or0 + 1
(0 + 0 + 1) + 1

**could also user a counter method to count the number of recursions

'''
