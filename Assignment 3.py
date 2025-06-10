
#Task 1: Calculate Factorial Using a Function 

def factorial(n):
     
    if n<2:
        return 1
    else:
        return n * (factorial(n-1))
n=int(input("enter your no. "))  
result =  factorial(n)
print("factorial =",result)

#Task 2: Using the Math Module for Calculations

import math

num=float(input("enter your number: "))

if num>0:
   square_root=math.sqrt(num)
   natural_log=math.log(num)
   sin_value=math.sin(num)

   print(f" square root ={square_root}: ")
   print(f" natural log ={natural_log}: ")
   print(f" sin value ={sin_value}: ")

else:
    print("Logarithm and square root are not defined for zero or negative numbers.")








































