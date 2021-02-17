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