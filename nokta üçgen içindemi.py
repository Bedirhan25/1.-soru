from random import randint
import math
from matplotlib import pyplot as plt


x1=randint(0,100)
y1=randint(0,100)
x2=randint(0,100)
y2=randint(0,100)
x3=randint(0,100)
y3=randint(0,100)
print(x1,y1)
print(x2,y2)
print(x3,y3)

while(1):
   x4=int(input("bir x koordinatı giriniz"))
   y4=int(input("bir y koordinatı giriniz"))
   if x4==0 and y4==0:
      break
   A= (((x4-x1)*(y2-y3))+((y4-y1)*(x3-x2))+(((x2-x1)*(y3-y1))-((y2-y1)*(x3-x1))))/(((x2-x1)*(y3-y1))-((y2-y1)*(x3-x1)))
   B= ((x4-x1)*(y3-y1)-(y4-y1)*(x3-x1))/(((x2-x1)*(y3-y1))-((y2-y1)*(x3-x1)))
   C= ((x2-x1)*(y4-y1)-(x4-x1)*(y2-y1))/(((x2-x1)*(y3-y1))-((y2-y1)*(x3-x1)))
   if (A>0 and B>0 and C>0 and A<1 and B<1 and C<1 ):
      print ("Noktamız üçgen içindedir")
      print("Çıkmak için 0,0 noktasını tuşlayınız")
   else:
      print("Noktamız üçgen içinde değildir")
      print("Çıkmak için 0,0 noktasını tuşlayınız")
   x=[x1,x2,x3,x1,x4]
   y=[y1,y2,y3,y1,y4]
   plt.plot(x, y)
   plt.show()
