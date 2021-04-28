#Ingresa un Array y un element
#Busca la primera instancia del element
#Si encuentra el element devuelve la position, sino devuelve None
def search(Array, element):
  n=len(Array)
  for i in range(0,n):
    if Array[i]==element:
      return i
  return None    


#Ingrea un Array, un element y una position
#positiona el element el la position ingresada
#Devuelve el Array modificado, None si no existe la position
def insert(Array,element,position):
  n=len(Array)
  if position<0 or position>=n:
    return None
  else:
    for i in range(n-1,position,-1):
      Array[i]=Array[i-1]
    Array[position]=element
  return position  


#Ingresa un Array y un element
#Busca y elimina la primera instacia del element ingresado
#Devuelve la position si existe dicho element, de lo contrario devuelve None
def delete(Array,element):
  n=len(Array)
  existe=False

  for i in range(0,n):
    if Array[i]==element:
      if existe==False:
        position=i
      existe=True

  if existe==True:
    for i in range(position,n-1):
      Array[i]=Array[i+1]
    Array[n-1]=None
    return position
  return None    

#Ingresa un Array
#Cuenta la cantidad de elements no vacios
#Devuelve la cantidad de elements no vacios
def length(Array):
  n=len(Array)
  full=0
  for i in range(0,n):
    if Array[i]!=None:
      full+=1
  return full     