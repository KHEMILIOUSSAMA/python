# SAISIE UN NOMBRE DANS UN intervalle 
 nb = int (input("saisir un nombre "))
while nb <10 or nb >20:
    if nb<10: 
      nb = int(input("plus grand  "))
    else:
      nb = int(input("plus petit  ")) 

print("bravo")


# NOMBRE PREMIER
N=int(input("saisir un nombre - ")) 
etat=True
for i in range (2,N//2) :
    if N%i==0 : 
        etat=False
        break
		
# nombre factorielle using for
a= int(input("saisir un nombre"))
p=1
for i in range(2,a+1):
    p*=i

print("le factoriel de ",a,"est",p)

