from mylinkedlist import *

class AVLTree:
    root = None

class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    balanceFactor = None
    height = None

#Realiza una rotación a la izquierda
def rotateLeft(Tree,avlnode):
    if avlnode.rightnode!=None:
        avlnode.rightnode.parent = avlnode.parent
        avlnode.parent = avlnode.rightnode
        if avlnode.rightnode.leftnode!=None:
            avlnode.rightnode = avlnode.rightnode.leftnode
            avlnode.rightnode.parent = avlnode
        else:
            avlnode.rightnode = None
        avlnode.parent.leftnode = avlnode
        if avlnode == Tree.root:
            Tree.root = avlnode.parent
        update_heigth(avlnode)
        update_bf(avlnode)

#Realiza una rotación a la derecha
def rotateRight(Tree,avlnode):
    if avlnode.leftnode!=None:
        avlnode.leftnode.parent = avlnode.parent
        avlnode.parent = avlnode.leftnode
        if avlnode.leftnode.rightnode!=None:
            avlnode.leftnode = avlnode.leftnode.rightnode
            avlnode.leftnode.parent = avlnode
        else:
            avlnode.leftnode = None
        avlnode.parent.rightnode = avlnode
        if avlnode == Tree.root:
            Tree.root = avlnode.parent
        update_heigth(avlnode)
        update_bf(avlnode)

#Balancea un arbol binario al encontrar un nodo bf!= 1,0,-1
#Aciende a través del padre de un nodo hasta encontrarlo o llegar a la raiz del árbol
def reBalance(AVLTree, Node):
    if Node == None:
        return
    else:
        if Node.balanceFactor==0 or Node.balanceFactor==1 or Node.balanceFactor==-1:
            return reBalance(AVLTree,Node.parent)
        elif Node.balanceFactor<0:
            if Node.rightnode.balanceFactor>0:
                rotateRight(AVLTree,Node.rightnode)
                rotateLeft(AVLTree,Node)
            else:
                rotateLeft(AVLTree,Node)
        elif Node.balanceFactor>0:
            if Node.leftnode.balanceFactor<0:
                rotateLeft(AVLTree,Node.leftnode)
                rotateRight(AVLTree,Node)
            else:
                rotateRight(AVLTree,Node)


#Actualiza la altura de un arbol
def updateheigth(Tree):
    if Tree.root==None:
        return
    else:
        currentNode = Tree.root
        updateheigthR(currentNode)


def updateheigthR(Node):
    if Node.rightnode==None and Node.leftnode==None:
        Node.height = 0
    else:
        if Node.rightnode!=None and Node.leftnode!=None:
            hleft = updateheigthR(Node.leftnode)
            hright = updateheigthR(Node.rightnode)
            if hleft >= hright:
                Node.height = hleft+1
            else:
                Node.height = hright+1
        elif Node.rightnode==None and Node.leftnode!=None:
            Node.height = updateheigthR(Node.leftnode) +1
        else:
            Node.height = updateheigthR(Node.rightnode) +1
    return Node.height


#Inserta un nuevo nodo en un arbol binario y asegura su balanceo
def insertBT(B,element,key):
    Node = AVLNode()
    Node.key = key
    Node.value = element
    if B.root==None:
        B.root = Node
        Node.height = 0
        Node.balanceFactor = 0
    else:
        insertR(Node,B.root)
        reBalance(B,Node.parent)
              

#Busca la posicion donde insertar un nodo
#Si la key ya existe devuelve un error
#Actualiza la altura y el balance factor de cada nodo afectado
def insertR(newNode,currentNode):
    if newNode.key>currentNode.key:
        if currentNode.rightnode==None:
            currentNode.rightnode = newNode
            newNode.parent = currentNode
            update_heigth(newNode)
            update_bf(newNode)
            return newNode.key
        else:
            return insertR(newNode,currentNode.rightnode)
    elif newNode.key<currentNode.key:
        if currentNode.leftnode==None:
            currentNode.leftnode = newNode
            newNode.parent = currentNode
            update_heigth(newNode)
            update_bf(newNode)
            return newNode.key
        else:
            return insertR(newNode,currentNode.leftnode)
    else:
        return None


#Actualiza el balance factor de un nodo y de sus nodos padres
def update_bf(Node):
    if Node==None:
        return

    elif (Node.leftnode==None) and (Node.rightnode==None):
        Node.balanceFactor=0

    elif Node.leftnode!=None and Node.rightnode==None:
        Node.balanceFactor = Node.height

    elif Node.leftnode==None and Node.rightnode!=None:
        Node.balanceFactor = - Node.height

    else:
        Node.balanceFactor = Node.leftnode.height - Node.rightnode.height
    return update_bf(Node.parent)

#Actualiza la altura de un nodo y de sus nodos padres
def update_heigth(currentNode):

    if currentNode==None:
        return None

    elif currentNode.leftnode==None and currentNode.rightnode==None:
        currentNode.height=0

    elif currentNode.leftnode!=None and currentNode.rightnode==None:
        currentNode.height = currentNode.leftnode.height+1

    elif currentNode.leftnode==None and currentNode.rightnode!=None:
        currentNode.height = currentNode.rightnode.height+1

    else:
        if currentNode.leftnode.height>=currentNode.rightnode.height:
            currentNode.height = currentNode.leftnode.height + 1
        else:
            currentNode.height = currentNode.rightnode.height + 1
    return update_heigth(currentNode.parent)


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
    parent = currentNode.parent
    #Prime caso: nodo sin hijos
    if currentNode.leftnode==None and currentNode.rightnode==None:
        if currentNode.parent==None:
            B.root=None
        elif currentNode.parent.leftnode==currentNode:
            currentNode.parent.leftnode=None
        else:
            currentNode.parent.rightnode=None
        update_bf(parent)
        update_heigth(parent)
        reBalance(B,parent)

    #Segundo caso: El nodo tiene solamente un hijo
    #Caso que el hijo este a la derecha
    elif currentNode.leftnode!=None and currentNode.rightnode==None:
        if currentNode.parent==None:
            B.root=currentNode.leftnode
        elif currentNode.parent.leftnode==currentNode:
            currentNode.parent.leftnode=currentNode.leftnode
        else:
            currentNode.parent.rightnode=currentNode.leftnode
        update_bf(parent)
        update_heigth(parent)
        reBalance(B,parent)
    #Caso que el hijo este a la izquierda
    elif currentNode.leftnode==None and currentNode.rightnode!=None:
        if currentNode.parent==None:
            B.root=currentNode.rightnode
        elif currentNode.parent.leftnode==currentNode:
            currentNode.parent.leftnode=currentNode.rightnode
        else:
            currentNode.parent.rightnode=currentNode.rightnode
        update_bf(parent)
        update_heigth(parent)
        reBalance(B,parent)
    
    #Caso que el nodo tenga dos hijos
    else:
        #Busca el mayor de los menores
        findNode=currentNode.leftnode
        while findNode.rightnode!=None:
            findNode=findNode.rightnode
        currentNode.value=findNode.value
        return delete_nodeBT(B,findNode)
    return currentNode.key

###########################################
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