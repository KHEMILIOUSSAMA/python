# calcul volume 
from math import *
h= float(input("hateur:"))
r=float(input("rayon:"))
v=1/3*pi*r**2*h
print(v)


#calcul surface

from math import *
rExt = float(input("entrerle rayon exterieur:"))
rInt = float(input("entrerle rayon interne:"))
sExt= pi*rExt**2
sInt=pi*rInt**2
surface=sExt-sInt
print(surface)

#comparaison

val1 = int(input("saisir une valeur1: "))
val2 = int (input("saisir une valeur2: "))
if val1<val2:
  print ("la valeur la plus petite est ", val1)
else:
    print("la valeur la plus petite est ",val2)

#comparaison chaine

chaine1 = input("chaine 1: ")
chaine2 = input("chaine 2: ")
if len(chaine1)<len(chaine2):
 print ("la chaine la plus petite est:", chaine1)
else: 
  print("la chaine la plus petite est:", chaine2)

# multiple

nombre = int (input("entrer un nombre: "))
modulo2=nombre%2
modulo3=nombre%3
if modulo2==0:
  print("ce nombre est pair")
elif modulo3==0:
  print("ce nombre est multiple de 3")
else:
  print("ce nombre est impair et non multiple de 3")    