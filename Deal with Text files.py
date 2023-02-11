
#**********************File Handling*************************
# file = open("lucky.txt","r")
#*******Reading from file****
# print(file.read())
# for item in file:
#     print(item)

# print(file.readline())

# print(file.readline(10))
# file.seek(4)
# print(file.tell())

# print(file.readline(5))

# print(file.readlines(40))


#********Writing into file***************
# file = open("lucky.txt","w")
# myinfo = "my name is khan and i am not a terreorist\n"

# # file.write("my name is not lucky\n")
# # file.write("i do not live in delhi")

# file.write(myinfo)

# file.writelines(["lucky ansari "," anas ansari\n"])
# file.writelines("lucky ansari")

# var = (3,)
# print(type(var))
# print(var)

#**************Appending File***********
# file = open('lucky.txt','a')
# file.write("my name is khan\n")
# file.writelines(["lucky\n","aman\n","sahil\n"])


# with open('lucky.txt','r') as file:
#     print(file.read())
# file.close()




#***********************Binary files*********************
import pickle
#**********dump***********
# file = open('lucky.dat','wb')
# x = [1,2,3,4,533,6]
# y = [1,2]
# pickle.dump(x,file)
# file.close()

#*************load**********
file = open('lucky.dat','rb')
print(pickle.load(file))

file.close()



#********** Rough code*******************
# a =10
# b = 0
# try:
#     print("program open")
#     print(a/b)
#     k = int(input("Enter num"))
# except ValueError:
#     print("plese enter a valid num")
    
# except ZeroDivisionError:
#     print("you can not divide by 0")

# except SyntaxError:
#     print("please check the syntax")
    
# except Exception:
#     print("unexpected error...!")
    
# finally:
#     print("program close")
    
# print("by")


# print("lucky","ansari","from","Delhi",sep="\n",end=" ")
# print("my name is khan")

# this is a function of factorial....
# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*(factorial(n-1))

# n = int(input("Enter num to find factorial:"))
# fact = factorial(n)    
# print(fact)

# print("initial")
# """
# this is multi line  comment
# and this is simlkjdjlkfjkfl
# djfkdjf
# fjkldfd
# jfjd
# """
# print("byyy")







