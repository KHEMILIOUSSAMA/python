
L = ["laptop" , "ipad" , "iphone" , "tablette" , "imprimante"]
 
# première méthode
print("\npremière méthode\n-------------")
for x in L:
    print(x)


def swapList(L):
    # obtenir le dernier élément de la liste
    swap = L[-1]
    
    # remplacer le dernier élément de la liste par le premier
    L[-1] = L[0]
    
    # remplacer  le premier élément de la liste par le dernier
    L[0] = swap
    return L
    
    
# Exemple   
L = L = ["Python" , "Java" , "C++" , "Javascript"]
print(swapList(L))
# La sortie est  : ['Javascript', 'Java', 'C++', 'Python']
 
 # moyenne
def moyList(L):
    
    m = 0
    for x in L:
        m = m + x
    
    m = m/len(L)
    return m
    
 
L = [3, 7 , 8 , 19]
print("la moyenne est : m = " , moyList(L))



#multiplier liste
 
def listMultiply(L,n):
    # initialisation de la liste souhaitée
    l_mult = []
    # parcourir et multiplier les éléments de la liste par n
    for x in L:
        l_mult.append(n*x)
        
    return l_mult
 
# Exemple
n = 5
L = [3, 9 , 5 , 23]
print(listMultiply(L,n)) # affiche [6, 18, 10, 46]



#differenceSymetrique
 
#coding: utf-8
def differenceSymetrique(L1 , L2):
    # initialiser la liste difference sysmétrique de L1 et L2
    diffSym = []
    for x in L1:
        if x not in L2:
            diffSym.append(x)
    for x in L2:
        if x not in L1:
            diffSym.append(x)
    return diffSym
#Exemple
L1 = [11 , 3 , 22 , 7 , 13 , 23 , 9]
L2 = [5 , 9 , 19 , 23 , 22 , 23 , 13]
print("La différence symétrique de L1 et L2 est : " , differenceSymetrique(L1 , L2))
# La différence symétrique de L1 et L2 est :  [11, 3, 7, 5, 19]


#liste dupliquées
def listduplicate (L):
  listduplicate=[]
  for x in L:
     if L.count(x) > 1 and x not in listduplicate :
        listduplicate.append(x)
  return listduplicate

L= [25,36,25,32,31,5,31,36,55]
print("la liste des éléments dupliquées est",listduplicate (L))

#mélanger une liste

from random import shuffle
laptop = ['HP', 'Acer', 'Dell', 'Lenovo', 'Thomson', 'Asus']
# mélanger les éléments de la liste avec le module shuffle
shuffle(laptop)
# afficher le résultat
print(laptop)


#couple <10
def s_couple (L):
  s_couple=[]
  for m in L:
    for n in L:
      if m+n<10:
        s_couple.append((m,n))
  return s_couple
L= [4,36,7,1,2,5,31,6,3]
print("la liste des couples est ",s_couple (L))
