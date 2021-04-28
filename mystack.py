from mylinkedlist import *

def push(S,element):
    add(S,element)

def pop(S):
    if S.head==None:
        return None
    else:
        element=S.head.value
        S.head=S.head.nextNode
        return element
        