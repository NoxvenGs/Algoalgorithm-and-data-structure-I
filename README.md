# Algoritmo y estructura de datos I
Contiene algunos algoritmos basicos de ordenamiento y estructura de datos

Archives:
  algo1.py helps to redefine the Array and String data structure.
 
 TAD's:
 
   Set.py: TAD que utiliza arreglos para realizar operaciones de conjuntos
      Requisitos: Utiliza algo1.py
      Operaciones de SET:
          Create_Set:       Crea un arreglo que representa el TAD set, ingresando un array y eliminando los elementos repetidos.
          check_duplicates: Determina si en un Set existen elementos repetidos, devuelve True o False respectivamente.
          Union:            Realiza la union de dos SETs sin elementos repetidos.
          Intersection:     Lee dos SETs y busca la interseccion entre ellos, genera un nuevo SET.
          Difference:       Lee dos SETs y busca la diferencia entre ellos, genera un nuevo SET.

  myarray.py: TAD que opera sobre estructura de datos Array.
      Operaciones de Array:
          search: Busca la primera instancia de un elemento, retorna la poscicion o None respectivamente.
          insert: Lee un arreglo, un elemento y una posicion, inserta el elementos en la posicion. Si no es posible retorna None.
          delete: Busca la primera instancia de un elemento y lo elimina, devuelve la posicion del elementos eliminados o None.
                  Desplaza las posiciones y la ultima queda en None en caso de que se elimine un elemento.
          length: Cuenta la cantidad de elementos no vacios.

  mylinkedlist: TAD del opera sobre la estructura de datos Linked List.
      Estructuras del TAD:
          class LinkedList():
              head=None

          class Node():
              value=None
              nextNode=None

      Operaciones sobr Linked List:
          add: añade nodos del tipo Node.
          search: Busca la primera instancia de un elemento, devuelve la posicion donde se encuentra o None.
          insert: Inserta un elemento en la posicion definida, devuelve la posicion donde se inserto o None.
          delete: Elimina la primera instancia de un elemento, devuelve None si no se encuentra el elemento.
          lenght: Calcula la cantidad de nodos de una linked list.
          access: Accede a un elemento en la posiciondeterminada, devuelve el elemento en la posicion.
          update: Actualiza un elemento en la posicion determinada, devuelve la posicion donde se actualizo o None.
          printL: Imprime la Linked List.
          reverse: Invierte la Linked List.
          
          
          
    
          
