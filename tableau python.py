# minim valeur d un tableau
def minim(T):
 min=T[0]       
 for i in T :
  if i<min:
     min=i
 print("le valeur minimal est",min)         
         
T = [3, 5, 8, 13, 19, 2, 6]
minim(T)

# max valeur d un tableau
def maxim(T):
 max =T[0]
 for i in T: 
  if i>max:
    max=i
    
 print("le max est",max)
  
  
T = [3, 5, 8, 13, 19, 2, 6]
maxim(T)
# existance d un valeur dans un tableau
def exist(T,K):
 exist=0
 for i in T:
   if i==K :
     exist=1
     break
   
 if exist == 1:
   print("exist")
 else:
   print("n existe pas")
     
T = [3, 5, 8, 13, 19, 2, 6]
K=5
exist(T,K)
# les valeurs positifs d un tableau
def positif(T):
 for i in T:
  if i>=0:
    print(i)
    
T = [3, 5, 8, -13, -19, 2, 6]
positif(T)

def somme(T):
  som =0
  for i in T:
   som+=i
   #la somme des éléments du tableau
  print ("la somme est",som)
T = [12, 5, 8, 13, 19, 2, 6]
somme(T)
# le produit des éléments du tableau
def produit (T):
  prod=1
  for i in T:
   prod*=i
  print ("le produit est",prod)
T = [1, 5, 2, 2, 1, 1, 1]
produit(T)

#les nombres pairs
def pairs(T):
  for i in T:
    if i%2==0: print("le nombre pair sont",i)
T = [12, 5, 8, 13, 19, 2, 6]
pairs(T)
      
     # liste des nombres pairs 
def pairslist(T):
  nombrepair=''
  for i in T:
    if i%2==0:
      nombrepair+=str(i)+', '
  print("la liste des nombres pairs est",nombrepair)
T = [12, 5, 8, 13, 19, 2, 6]
pairslist(T)




# Saisir la taille actuelle du tableau
N = int(input("Saisir le nombre d'éléments : "))
 
# intialiser la taille de tableau avec N
tab=[0]*N;
 
# Saisir les éléments du tableau source
for i in range(N):
    tab[i]=int(input("Saisir l'élement {0} : ".format(i+1)))
 
# afficher les éléments négatifs du tableau tab
for i in range(N):
  if(tab[i]<0):
    print(tab[i],end=', ')
  # calcul somme 2  
    
    # Saisir la taille actuelle du tableau
N = int(input("Saisir le nombre d'éléments : "))
 
# intialiser la taille de tableau avec N
tab=[0]*N;
 
# Saisir les éléments du tableau source
for i in range(N):
    tab[i]=int(input("Saisir l'élement {0} : ".format(i+1)))
 
# Ajouter chaque élément du tableau à somme
somme=0
for i in range(N):
    somme = somme + tab[i]
 
print("Somme de tous les éléments du tableau = ",somme)
# min,max

N = int(input("saisir le nombre d'éléments: "))
tab=[0]*N
for i in range(N):
  tab[i]=int(input("saisir l'élément {1}: ".format(i)))
max=tab[0]
min=tab[0]

for i in range(N):
 if(tab[i]>max):
   max=tab[i]
 if(tab[i]<min):
   min=tab[i]
print("maximum= ",max)
print("minimum= ",min)


#nombre des pairs et impairs

# Saisir la taille actuelle du tableau
N = int(input("Saisir le nombre d'éléments : "))
 
# intialiser la taille de tableau avec N
tab=[0]*N
 
# Saisir les éléments du tableau source
for i in range(N):
    tab[i]=int(input("Saisir l'élement {0} : ".format(i+1)))
 
 
# En supposant qu'il y a 0 éléments pairs et impairs
pair = 0
impair = 0
 
for i in range(N):
    # Si l'élément courant du tableau est pair, incrémenter le nombre pair
    if (tab[i] % 2 == 0):
        pair+=1
    else:
        impair+=1
 
print("Total des éléments pairs: ",pair)
print("Total des éléments impairs : " ,impair)



# afficher les éléments négatifs

# Saisir la taille actuelle du tableau
N = int(input("Saisir le nombre d'éléments : "))
 
# intialiser la taille de tableau avec N
tab=[0]*N;
 
# Saisir les éléments du tableau source
for i in range(N):
    tab[i]=int(input("Saisir l'élement {0} : ".format(i+1)))
 
print("Les éléments négatifs du tableau sont : ")
for i in range(N):
    # Si l'élément de tableau actuel est négatif */
    if (tab[i] < 0):
        print(tab[i],end=", ")