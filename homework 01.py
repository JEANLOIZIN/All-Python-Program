# Jean Loizin
# CS 100
# Section 006




#2.18
#A) print statements are written under assignment, to make it available to the user to see the result of the code.

flowers=['rose','bougainvillea','yucca','marigold','daylilly','lilly of the valley']
#B  boolean expression
'potato'in flowers
#print('potato'in flowers)

#C
thorny=flowers[:3]
#print(thorny)

#D
poisonous=flowers[-1]
#print(poisonous)

#E
dangerous= thorny,poisonous
#print(dangerous)


#2.19

import math

radius=input("input radius, or 10 for default:")
x=int(input("please input value for x: "))
y=int(input("Please input value for y: "))
distance=math.sqrt(x**2 + y**2)
print(distance)
if distance:
    print("hit")
else:
    print("miss")

#2.21
s='top'
print(s.reverse)

    
