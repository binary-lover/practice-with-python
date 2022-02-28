#Simple calculator...

num1 = float(input("Enter 1st num))
op  = input("+\n-\n*\n/)
num2 = float(input("Enter 2nd num))
if op == "+":
	pirnt(num1,"+",num2,"=",num1+num2)
elif op == "-":
	pirnt(num1,"-",num2,"=",num1-num2)				   
elif op == "*":
	pirnt(num1,"*",num2,"=",num1*num2)				   
elif op == "/":
	pirnt(num1,"/",num2,"=",num1/num2)				   
                   
