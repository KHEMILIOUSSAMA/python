#guess the number


import random
number = random.randint(1,20)
guess =int(input("Je pense à un chiffre de 1 à 20. Qu'est-ce que c'est?"))
while guess != number:
    if guess < number:
        print("Votre nombre était trop bas...")
    else:
        print("Votre nombre était trop élevé...")
    guess = int(input("Veuillez réessayer..."))
print("Toutes nos félicitations! Bonne réponse!")


#randint

from random import *
n= randint(1,16)
print(n)


#random,uniform
from random import *
n=random ()
print(n)
x=uniform(1,9)
print(x)
#chice 

from random import *
liste=["oussama","hamza","razi","bilel"]
résultat = choice(liste)
print(résultat)

#sample

from random import *
lettres = ["a","b","c","d","e"]
résultat = choices(lettres , k=10)
print(résultat)
résultat2 = sample(lettres,k=3)
print(résultat2)

#shufffle

from random import *
liste= ["a","b","c","d"]
shuffle(liste)
print(liste)

#table de multiplication

from random import *
score=0
for i in range (10:
  a=randint(0,10)
  b=randint(0,10)
  
  c=int(input(str(a)+"*"+str(b)+"=?"))
  if c==a*b:
    score+=1
    print("bravo","score="+str(score))
  else:
    score-=1
    print("faux","score="+str(score))
    
    
    # probabilite d'obtenir 6
    
    from random import *
c=0
n=int(input("entrer le nombre des lancers"))
for i in range (n):
  
 D1= randint(1,6)
 D2= randint(1,6)
 if D1+D2==6:
   c=c+1
print(c/n)