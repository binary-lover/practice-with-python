import csv
#*************Write in csv file********************
# file = open("myscv.csv","w", newline= "")
# myriter = csv.writer(file)
# lucky = ["lucky",19,"Delhi"]
# sahil = ["sahil",20,"Delhi"]
# mohan = ["mohan",20,"bihar"]

# myriter.writerow(["lucky"])
# myriter.writerows(["lucky","lucky"])
# myriter.writerow(sahil)
# myriter.writerow(mohan)

# data=["Name","roll no","Class"]
# myriter.writerow(data)
# for i in range(3):
#     name = input("Enter name: ")
#     roll = int(input("Enter roll no: "))
#     Class =int(input("enter Class:"))
#     data =[name,roll,Class]
#     myriter.writerow(data)

# data =[["lucky",10,12],["sahil",12,12],["adil",10,12]]
# myriter.writerows(data)

# file.close()

#************ Read in csv file*************

file = open("myscv.csv","r")
myreader = csv.reader(file)
for i in myreader:
    print(i)