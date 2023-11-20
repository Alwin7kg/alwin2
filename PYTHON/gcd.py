#To find GCD of 2 numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1<num2:     #Find the min of the 2 numbers
    min=num1
else:
    min=num2
gcd = 1 #Initialize GCD to 1 (as GCD is always at least 1)
#Iterate from 1 to the min of the two numbers
for i in range(1, min + 1):
    if num1 % i == 0 and num2 % i ==0:
        gcd = i
print(f"The GCD of {num1} and {num2} is {gcd}")        
