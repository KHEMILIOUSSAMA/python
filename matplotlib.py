
#y=cos(x) +3sin(2x)

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4,4,100)
y = np.cos(x)+3*np.sin(2*x)
plt.plot(x,y)
plt.show()

#y=x**2-4x+4

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,3,100)
y = -2*x+3
plt.plot(x,y)
y = x**2 - 4*x + 4
plt.plot(x,y)
    
plt.show()

#y=cos(nx)

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi,np.pi,100)
for n in range(1,5):
    y = np.cos(n*x)
    plt.plot(x,y, label="n="+str(n))
    
plt.legend(loc="lower right")
plt.show()

#bar

import matplotlib.pyplot as plt
import numpy as np


x = [3, 5, 6, 7]
y = [4, 1, 3, 4]
plt.bar(x,y)

plt.show()

#bar ,liste

import matplotlib.pyplot as plt
import numpy as np
from random import *

liste =[randint(1,6)+randint(1,6) for _ in range(1000)]
plt.hist(liste,10)

plt.show()
#bar2,scatter

import matplotlib.pyplot as plt
import numpy as np

x = [ 1, 3, 2, 1]
y = [ 2, 4, 9, -2]
plt.scatter(x,y)

plt.show()

#ex1
import matplotlib.pyplot as plt
import numpy as np
from math import *

x = np.linspace(-2,4,1000)
y = x**3+2*x**2-9*x+1
plt.plot(x,y)
plt.show()

#ex2

import matplotlib.pyplot as plt
import numpy as np
from math import *

abscisses = np.linspace(-4,4,100)
ordonnées = [3*cos(2*x) -2*sin(3*x) for x in abscisses]
plt.plot(abscisses,ordonnées)
plt.show()

#ex3

import matplotlib.pyplot as plt
import numpy as np
from math import *

 

x = np.linspace (-2,4,100)
for n in range (-3,4):
  y= (1-n*x)/(x-1) 
  plt.plot(x,y, label="n="+str(n) )
plt.ylim(-8,8)
plt.legend(loc="upper left")
plt.show()