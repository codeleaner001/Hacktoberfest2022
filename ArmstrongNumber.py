# Python program to check if the number is an Armstrong number or not

# input from user
n = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = n
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if n == sum:
   print(n,"is an Armstrong number")
else:
   print(n,"is not an Armstrong number")
