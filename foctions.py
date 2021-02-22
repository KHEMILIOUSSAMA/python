#elimination 

def elimine1(L):
  P=[]
  for e in L:
    if e not in P:
      P.append(e)
  print (P)
  
L= [1,2,2,1,2,1]
elimine1(L)
# div par 5

def isDivisibleBy5(n):
  return not n % 5
print(isDivisibleBy5(5))
print(isDivisibleBy5(-5))
print(isDivisibleBy5(3))
 
 # get last element
 
 def getLast(liste):
 return liste[-1]
print(getLast([1, 2, 3]))
print(getLast(["A", "B", "C"]))
print(getLast([10, "WayToLearnX", True]))

#calcul du carre

def carre(a):
	return a*a

# Testez le code
print(carre(2))
print(carre(4))

#check if plural
def checkIsPlural(str):
  return str.endswith ('s')
print(checkIsPlural("enfants"))
print(checkIsPlural("filles"))
print(checkIsPlural("fille"))
print(checkIsPlural("enfant"))
 
 #check if impair
 
 def check(n):
  return 'impair' if n % 2 else 'pair'
print(check(2))
print(check(7))
print(check(22))
#obtenir le difference

def getDiff(*args):
  return max(args)-min(args)
print(getDiff(200, 10, 90))
print(getDiff(56, 29, 3))
print(getDiff(2, 10, 5))


#divisibilité

def div(a,b):
  return a/b if b!=0 else "erreur"
print(div(4,2))
print(div(11,2))
print(div(1,0))


# get first , last element
def getFirstLast(liste):
  return [liste[0],liste[-1]]
print(getFirstLast([1, 2, 3, 4, 5, 6, 7]))
print(getFirstLast(["A", "B", "C", "D"]))
print(getFirstLast(["A", 2, True, None]))
# calcul de somme

somme, nombreTotal, nombreGrands = 0, 0, 0

x = int(input("x (0 pour terminer) ?"))
while x > 0:
    somme += x
    nombreTotal += 1
    if x > 100:
        nombreGrands += 1
    x = int(input("x (0 pour terminer) ?"))

print("\nSomme :", somme)
print(nombreTotal, "valeur(s) en tout, dont", nombreGrands, "supérieure(s) à 100")
  #calcul de nombre de fois de div par 2

n = int(input("Entrez un entier strictement positif :"))
while n < 1:
    n = int(input("Entrez un entier STRICTEMENT POSITIF, s.v.p. :"))
save = n

cpt = 0
while n%2 == 0:
    n /= 2
    cpt += 1

print(save, "est", cpt, "fois divisible par 2.")

#calcul  de nombre des diviseurs
n = int(input("Entrez un entier strictement positif :"))
while n < 1:
    n = int(input("Entrez un entier STRICTEMENT POSITIF, s.v.p. :"))

i = 2 # plus petit diviseur possible de n
cpt = 0 # initialise le compteur de divisions
p = n/2 # calculé une fois dans la boucle

print("Diviseurs propres sans répétition de", n, " :", end=' ')
while i <= p :
    if n%i == 0:
        cpt += 1
        print(i, end=' ')
    i += 1

if not cpt :
    print("aucun ! Il est premier.")
else :
    print("(soit", cpt, "diviseurs propres)")
    
    S =0
    
  #foction  
    
for j in range (4 ,11):
  S = S +2** j
print( S )
#div par7
compteur =0
for k in range (1 ,101):
 if ( k %7==0):
   compteur = compteur +1
print( compteur )