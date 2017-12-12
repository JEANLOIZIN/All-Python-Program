#Jean Loizin
#Cs 100 Section 6
#HW 00, January 26,2015


print("Integers are fix numbers range from 0 to any non decimal number"'\n\n')                             # screen output
Variable1=int(input("Please enter first integer:"'\n'))                                                    # first input
Variable2=int(input("Please enter second integer:"'\n'))                                                   # second input
Variable3=int(input("please enter third interget"':\n'))                                                   # Third input
month=Variable1+Variable2+Variable3                                                                        # adding all inputs and assigning input to new variable  
print("month=",month)                                                                                      # Printing new variable from input calculation
                                                                                                           # skipping unreadable line      
print('\n'"float numbers are negative or positive decimal number"'\n\n')                                   # Scren instruction print out
Float1=float(input("Please enter a float number:"'\n'))                                                    # First input
Float2=float(input("Please enter a second float number:"'\n'))                                             # second input
Float3=float(input("Please enter a third float number:"'\n'))                                              # Third input
height=Float1+Float2+Float3                                                                                # adding all inputs and assigning solution a new variable
print("height=",height)                                                                                    # printing new variable
                                                                                                           # skipping unreadable line
print('\n'"Strings are workds"'\n\n')                                                                      # screen instruction output
string1=str(input("Please enter a word:"'\n'))                                                             # first input
string2=str(input("Please enter a second word:"'\n'))                                                      # second input
string3=str(input("Please enter a third word:"'\n'))                                                       # third input
manFromUncle=string1+string2+string3                                                                       # calculation of all input and assigning result to new variable
print("manFromUncle=",manFromUncle)                                                                        # printing out new variable
                                                                                                           # skipping unreadable line
                                                                                                           # skipping unreadable line
# Exercises
#2.12

# A
# The sum of the fist seven positive integers
addition=1+2+3+4+5+6+7
print(" Adding 7 odd numbers :" ,addition)

#B) The average afe of Sara(age 65),Faima(57),Mark(age 45)
ages=65+57+45
average=ages/3
print("average of all ages: " ,average)

#C 2 to the 20th power
print("2 to the power of 20: ", 2**20)

#D The number of times 61 goes into 4356
print("The number of times 61 goes into 4356: ", 4356/61)

#E The remainder when 4365 is divided by 61
print("The remainder when 4356 by 61: ", 4365%21)


#2.13
s1='-'
s2='+'
print(s1+s2,'\n')
print(s2+s1*2,'\n')
print((s2+s1*2)*10)


#2.14

s='abcdefghijklmnopqrstuvwxyz'
print(s[0])
print(s[2])
print(s[-1])
print(s[-2])
print(s[-10])


#2.15
#A
s='goodbye'
print('g'in s)
print('g'==s[7]) #output would be error, because goodbye only contain 6 characters, therefore the string will be out of reach.
print(s[0]==s[-1])


#2.17
addition=(17+(-9))
print(addition<10)

a=6
b=7
print(6.75<=a,6.75>=b,6.75>=a,6.75<=b)
