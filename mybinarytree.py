from mylinkedlist import *

class BinaryTree:
    root=None

class BinaryTreeNode:
    key=None
    value=None
    leftnode=None
    rightnode=None
    parent=None

#Inserta un nuevo nodo en un arbol binario
def insertBT(B,element,key):
    Node = BinaryTreeNode()
    Node.key = key
    Node.value = element
    if B.root==None:
        B.root = Node
    else:
        insertR(Node,B.root)

#Busca la posicion donde insertar un nodo
#Si la key ya existe devuelve un error
def insertR(newNode,currentNode):
    if newNode.key>currentNode.key:
        if currentNode.rightnode==None:
            currentNode.rightnode = newNode
            newNode.parent = currentNode
            return newNode.key
        else:
            return insertR(newNode,currentNode.rightnode)
    elif newNode.key<currentNode.key:
        if currentNode.leftnode==None:
            currentNode.leftnode = newNode
            newNode.parent = currentNode
            return newNode.key
        else:
            return insertR(newNode,currentNode.leftnode)
    else:
        return None


#Busca la primera instancia de un elemento en un arbol binario
#Si lo encuentra devuelve la Key sino devuelve None
def searchBT(B,element):
    if B.root==None:
        return None
    else:
        return searchBTR(B.root,element)

def searchBTR(currentNode,element):
    if currentNode.value==element:
        return currentNode.key
    else:
        if currentNode.leftnode!=None:
            Left = searchBTR(currentNode.leftnode,element)
            if Left!=None:
                return Left
        if currentNode.rightnode!=None:
            Right = searchBTR(currentNode.rightnode,element)
            if Right!=None:
                return Right
 
#Elimina la primera instancia de un elemento 
def deleteBT(B,element):
    if B.root==None:
        return None
    else:
        return deleteR(B,B.root, element)

def deleteR(B,currentNode, element):
    if currentNode.value==element:
        return delete_nodeBT(B,currentNode)
    else:
        if currentNode.leftnode!=None:
            Left = deleteR(B,currentNode.leftnode,element)
            if Left!=None:
                return Left
        if currentNode.rightnode!=None:
            Right = deleteR(B,currentNode.rightnode,element)
            if Right!=None:
                return Right

def delete_nodeBT(B,currentNode):
    #Prime caso: nodo sin hijos
    if currentNode.leftnode==None and currentNode.rightnode==None:
        if currentNode.parent==None:
            B.root=None
        elif currentNode.parent.leftnode==currentNode:
            currentNode.parent.leftnode=None
        else:
            currentNode.parent.rightnode=None

    #Segundo caso: El nodo tiene solamente un hijo
    #Caso que el hijo este a la derecha
    elif currentNode.leftnode!=None and currentNode.rightnode==None:
        if currentNode.parent==None:
            B.root=currentNode.leftnode
        elif currentNode.parent.leftnode==currentNode:
            currentNode.parent.leftnode=currentNode.leftnode
        else:
            currentNode.parent.rightnode=currentNode.leftnode
        
    #Caso que el hijo este a la izquierda
    elif currentNode.leftnode==None and currentNode.rightnode!=None:
        if currentNode.parent==None:
            B.root=currentNode.rightnode
        elif currentNode.parent.leftnode==currentNode:
            currentNode.parent.leftnode=currentNode.rightnode
        else:
            currentNode.parent.rightnode=currentNode.rightnode
    
    #Caso que el nodo tenga dos hijos
    else:
        #Busca el mayor de los menores
        findNode=currentNode.leftnode
        while findNode.rightnode!=None:
            findNode=findNode.rightnode
        currentNode.value=findNode.value
        return delete_nodeBT(B,findNode)
    return currentNode.key

#Recorre una arbol en amplitud
#Devuelve una lista enlazada representando el recorrido
def traverseBreadFirst(B):
    if B.root==None:
        return None
    else:
        L=LinkedList()
        insert(L,B.root,0)
        addtraverseBreadFirst(L,L.head,1)
        return L

def addtraverseBreadFirst(L,currentNode,position):
    if currentNode.value.leftnode!=None:
        insert(L,currentNode.value.leftnode,position)
        position+=1
    if currentNode.value.rightnode!=None:
        insert(L,currentNode.value.rightnode,position)
        position+=1
    if currentNode.nextNode!=None:
        addtraverseBreadFirst(L,currentNode.nextNode,position)
    currentNode.value = currentNode.value.value




###    EJERCICIOS ADICIONALES



#Recorre un arbol binario en pre-orden
#Devuelve el recorrido en una lista enlazada
def traverseInPreOrder(B):
    if B.root==None:
        return None
    else:
        L=LinkedList()
        traverseInPreOrderR(L,B.root)
        reverse(L)
        return L

def traverseInPreOrderR(L,currentNode):
    add(L,currentNode.value)
    if currentNode.leftnode!=None:
        traverseInPreOrderR(L,currentNode.leftnode)
    if currentNode.rightnode!=None:
        traverseInPreOrderR(L,currentNode.rightnode)

#Recorre un arbol binario en in-orden
#Devuelve el recorrido en una lista enlazada
def traverseInOrder(B):
    if B.root==None:
        return None
    else:
        L=LinkedList()
        traverseInOrderR(L,B.root)
        reverse(L)
        return L

def traverseInOrderR(L,currentNode):
    if currentNode.leftnode!=None:
        traverseInOrderR(L,currentNode.leftnode)
    add(L,currentNode.value)
    if currentNode.rightnode!=None:
        traverseInOrderR(L,currentNode.rightnode)
         
#Recorre un arbol binario en post-orden
#Devuelve el recorrido en una lista enlazada
def traverseInPostOrder(B):
    if B.root==None:
        return None
    else:
        L=LinkedList()
        traverseInPostOrderR(L,B.root)
        reverse(L)
        return L

def traverseInPostOrderR(L,currentNode):
    if currentNode.leftnode!=None:
        traverseInPostOrderR(L,currentNode.leftnode)
    if currentNode.rightnode!=None:
        traverseInPostOrderR(L,currentNode.rightnode)
    add(L,currentNode.value)


#Elimina un nodo a través de la key
#Devuelve la key del nodo eliminado
def deleteKey(B,key):
    if B.root==None:
        return
    else:
        return deleteKeyR(B,B.root,key)

def deleteKeyR(B,currentNode,key):
    if currentNode.key==key:
        return delete_nodeBT(B,currentNode)
    else:
        if currentNode.leftnode!=None:
            Left = deleteKeyR(B,currentNode.leftnode,key)
            if Left!=None:
                return Left
        if currentNode.rightnode!=None:
            Right = deleteKeyR(B,currentNode.rightnode,key)
            if Right!=None:
                return Right

#Accede a un elemento de un árbol binario a través de una key
#Devuelve None si no puede encontrar dicho elemento
def accessBT(B,key):
    if B.root==None:
        return
    else:
        return accessBTR(B,B.root,key)

def accessBTR(B,currentNode,key):
    if currentNode.key==key:
        return currentNode.value
    else:
        if currentNode.leftnode!=None:
            Left = accessBTR(B,currentNode.leftnode,key)
            if Left!=None:
                return Left
        if currentNode.rightnode!=None:
            Right = accessBTR(B,currentNode.rightnode,key)
            if Right!=None:
                return Right

#Actualiza un elemento en la key seleccionada de un arbol
#Devuelve la key si logra actualizarse, de lo contrario devuelve None
def updateBT(B,element,key):
    if B.root==None:
        return None
    else:
        return updateBTR(B.root,element,key)

def updateBTR(currentNode,element,key):
    if currentNode.key==key:
        currentNode.value=element
        return key
    if currentNode.leftnode!=None:
        Left = updateBTR(currentNode.leftnode,element,key)
        if Left!=None:
            return Left
    if currentNode.rightnode!=None:
        Right = updateBTR(currentNode.rightnode,element,key)
        if Right!=None:
            return Right


