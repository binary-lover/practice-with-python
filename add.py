#***********Very simple way without using function
num1 = int(input("Enter 1st num"))
num2 = int(input("Enter 2nd num"))
sum = num1 + num2
print("Sum is", sum)
#or
print("Sum is",num1+num2)


#********By using function
def add(a,b):
	return a+b
num1 = int(input("Enter 1st num"))
num2 = int(input("Enter 2nd num"))
print("Sum is",add(num1,num2))