class PriorityQueue():
    head=None

class PriorityNode():
    value=None
    nextNode=None
    priority=None


#encola un nodo en una cola de prioridad
def enqueue_priority(Q,element,priority):
    #Creo el nodo a insertar
    Node=PriorityNode()
    Node.value=element
    Node.priority=priority

    currentNode=Q.head
    position=0
    #Caso del primer nodo, vacio o con menor prioridad
    if currentNode==None or (currentNode.priority>=priority):
        Node.nextNode=currentNode
        Q.head=Node
        return position
    else:
        while currentNode!=None:
            if (currentNode.nextNode!=None) and (currentNode.nextNode.priority>=priority):
                Node.nextNode=currentNode.nextNode
                currentNode.nextNode=Node
                return position
            elif currentNode.nextNode==None:
                currentNode.nextNode=Node
                return position
            position+=1
            currentNode=currentNode.nextNode        


#desencola el elemento con mayor prioridad
def dequeue_priority(Q):
    currentNode=Q.head
    if currentNode==None:
        return None
    else:
        if currentNode.nextNode==None:
            priority=currentNode.priority
            Q.head=None
            return priority
        while currentNode!=None:
            if currentNode.nextNode.nextNode==None:
                priority=currentNode.nextNode.priority
                currentNode.nextNode=None
                return priority
            currentNode=currentNode.nextNode            