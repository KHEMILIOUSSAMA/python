
    
    #majeur_mineur

age = int(input("tapez votre age: "))
if (age <18) :
  print("vous etes mineur")
else:
  print("vous etes majeur")
  
  #somme
  
n= int (input("saisir un valeur n: "))
j=1
for i in range (1,n+1):
   j=i+j
print ("la somme est: ",j)
#nombre premier

n=int(input("saisir un nombre n: "))
j=0
for i in range(1,n+1):
  if (n%i==0):
    j=j+1
if(j==2):
  print("le nombre" , n,"est premier")
else:
  print("le nombre", n ,"n'est pas premier")

#position

s=input("tapez s: ")
n=len(s)
for i in range(0,n):
  if(s[i]=='a'):
   print("le caractere 'a' se trouve a la position " , i+1 ,)
   
  # last first 
  
s = "www.tresfacile.net"
n=len(s)
first=s[0]
last=s[n-1]
s1=[1,n-1]
s2==last +s1 +first
print(s2)



# Lire la variable string s
s = input("Tapez une chaine s : ")

# obtenir l'inverse de la chaine s
s1 = s[::-1]

print("L'inverse de la chaine : '",s,"' est : ", s1)