import pickle

def read():
    
    file = open("binary.dat",'rb')
    # s = pickle.load(file)
    while True:
        try:
            s = pickle.load(file)
            for i in s:
                print(i)
        except pickle.UnpicklingError:
            break
        except EOFError as e:
            print(e)
            break
    file.close()
        
    # s = s + pickle.load(file)
    # s = s + pickle.load(file)
    # s = s + pickle.load(file)
    # s = s + pickle.load(file)
    # s = s + pickle.load(file)
    # s = s + pickle.load(file)
    # print(s)
    # for i in s:
    #     print(i)
    
       
    # while True:
    #     try:
    #         s = pickle.load(file)
    #         for i in s:
    #             print(i)
    #     except EOFError:
    #         break;
    # file.close()
    
def write():
    file =open("binary.dat","wb")
    data =[]
    while True:
        name = input("Enter name here: ")
        Class =int(input("Enter class: "))
        sec = input("Enter section: ")
        data.append([name,Class,sec])
        
        x = input("do you want to enter more y/n")
        if x =='n':
            break

    pickle.dump(data,file)
    file.close()

def append():
    file = open("binary.dat","ab")
    data =[]
    while True:
        name = input("Enter name here: ")
        Class =int(input("Enter class: "))
        sec = input("Enter section: ")
        temp = [name,Class,sec]
        data.append(temp)
        x = input("do you want to enter more y/n")
        if x =='n':
            break
    pickle.dump(data,file)
    file.close()
    
def update():
    file = open("binary.dat","rb+")
    s = pickle.load(file)
    while True:
        try:
            s+= pickle.load(file)
        except Exception:
            break
    
    found = 0
    rno = input("Enter name wholse record you want to update")
    for i in s:
        if i[0] == rno:
            print("currnet name is: ",i[0])
            i[0] = input("Enter new name: ")
            found = 1
    if found == 0:
        print("Record Not Found: ")
    else:
        file.seek(0)
        pickle.dump(s,file)
    file.close()

def search():
    file =open("binary.dat","rb")
    s = pickle.load(file)
    while True:
        try:
            s+= pickle.load(file)
        except Exception :
            break
    found = 0
    name = input("Enter name for record you want to search: ")
    for i in s:
        if i[0] == name:
            print("Record found in data..!")
            print(i)
            found = 1
    if found !=1:
        print("Record not found")



# write()
# read()
# append()
# read()
# update()
# read()
# search()
# read()