import random as r
import time as t
import mysql.connector
import os

def began():
    global mydb
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="root")
    global mycursor 
    mycursor = mydb.cursor()
    crtDatabase()
    crtTableHighscore()   
    crtTempTable()
    

# 1) creatind database automatic and not by privious virsions
# 2) short the program
# 3) seprate fucntion for start program "began()"
# 4) performece improvment

def result(rightcount,level,qList,correctAnswer,yourAnswer,score,timetaken,game):
    chkHighScore(score,level,game) 
    tempTable(qList,correctAnswer,yourAnswer)
    a,b = len(str(timetaken)),len(str(score))
    print("\nyour score :",score," "*(10-b),"Result = ",rightcount,"/",10)  
    print("time taken :", timetaken," "*(10-a),"Level :",level)
    query = "select * from temp"
    mycursor.execute(query)
    print("+---------------+--------------------+-----------------+")
    print("¦ Qusetions     ¦    correct ans     ¦   your ans      ¦")
    print("+---------------+--------------------+-----------------+")
    for i in mycursor:
        print(chr(166),end=" ")
        for j in range(3):
            x = len(str(i[j]))
            print(i[j],end=" "*(14-x))
            if j <2:
                print("¦      ",end="")
        print("\b\b\b¦")
    print("+---------------+--------------------+-----------------+")
    print()
    if rightcount == 10:
        print("well done...! All answers are correct...\nKeep practicing")        
    elif rightcount >=7:
        print("Good...! Work more to be batter\nKeep praciting")
    else:
        print("Poor performence...! You need to practice alot\nKeep practicing")


def chkHighScore(score,level,game):
    query = "select max(score) from highscore where level = {} and game = '{}'".format(level,game)
    try:
        mycursor.execute(query)
    except Exception as e:
        print(e)
    for i in mycursor:
        if score >0:
            if i[0]==None:
                name = getName(None)
                insert(game,level,score,name)
            elif i[0] < score:
                name = getName(score)
                update(game,level,score,name)

def highScore():
    show = '''select * from highscore order by game not like 'addition',game not like 'subtraction',
    game not like 'multiplication',game not like 'division',game not like 'miscllaneous',game not like 'Table',level;'''
    mycursor.execute(show)
    tableData = mycursor.fetchall()
    if tableData ==[]:
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~ NO DATA FOUND ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        return
    else:
        print("+----------------+-----------------+-----------------+------------------+")
        print("¦  GAME","¦ LEVEL"," ¦ SCORE",sep=" "*(10),end= "")
        print("           ¦   NAME           ¦")
        print("+----------------+-----------------+-----------------+------------------+")
        for i in tableData:
            print(chr(166),end=" ")
            for j in range(4):
                x = len(str(i[j]))
                print(i[j],end=" "*(15-x))
                if j <3:
                    print("¦  ",end="")
            print(" ¦")
        print("+----------------+-----------------+-----------------+------------------+")
        print()

def pointGen(rightcount,  inetialTime, finalTime):
    timetaken = round(finalTime - inetialTime,2)
    score = round((rightcount*11)-(timetaken))
    return score,timetaken

def getName(mod):
    if mod is None:
        print("\nCongratulations..! you made a record.")
    else:
        print("\nCongratulations..!  you broke a record.")
    names = input("Enter your Name: ")
    return names

def crtDatabase():
    query = "Create database Easemaths;"
    query2 = "use Easemaths;"
    try:
        mycursor.execute(query)
    except mysql.connector.errors.DatabaseError:
        pass
    except Exception as e:
        print("Unexpected error ==> ",e)
    finally:
        mycursor.execute(query2)


def crtTableHighscore():
    create = "create table highscore(game varchar(20), level int(3), score int(3),name varchar(30))"
    try:
        mycursor.execute(create)
    except:
        pass
    
def crtTempTable():
    creat = "create table temp( Q_list varchar(20), Correct_Ans int(3), Your_Ans int(3));"
    try: 
        mycursor.execute(creat)
    except mysql.connector.errors.ProgrammingError:
        pass        
    except Exception as e:
        print(e)
        
def update(game,level,score,name):
    query = "update highscore set score = {}, name = '{}' where level = {} and game = '{}'".format(score,name,level,game)
    mycursor.execute(query)
    mydb.commit()

def insert(game,level,score,name): 
    query = "insert into highscore(game,level,score,name) values('{}',{},{},'{}')".format(game,level,score,name)
    mycursor.execute(query)
    mydb.commit()

def tempTable(qList, correctAnswer, yourAnswer):
    query = "select * from temp;"
    mycursor.execute(query)
    tableData = mycursor.fetchall()
    i = 1
    if tableData == []:
        while i <= 10:
            query = "insert into temp(Q_list, Correct_Ans, Your_Ans) values('{}',{},{})".format(str(i)+") "+qList[i-1],correctAnswer[i-1],yourAnswer[i-1])
            mycursor.execute(query)
            mydb.commit()
            i+=1
    else:
        while i <= 10:
            updateTempTable = "update temp set Q_list = '{}',Correct_Ans = {}, Your_Ans = {} where Q_list like '{}'".format(str(i)+") "+qList[i-1],correctAnswer[i-1],yourAnswer[i-1],str(i)+")%")
            mycursor.execute(updateTempTable)
            mydb.commit()
            i+=1

        
def getNum(op,level):
    if op == '+':
        return addMix(level)
    elif op == '-':
        return subMix(level)
    elif op == '*':
        return mulMix(level)
    elif op == '/':
        return divMix(level)
    else:
        print("unexpected error...!") 

def add(level, rightcount = 0, wrongcount = 0 ):
    game,correctAnswer,yourAnswer,qList = 'Addition',[],[],[]
    qList =[]
    inetialTime = t.time()
    for k in range(10):
        print("Q",k+1,sep="",end=") ")
        a,b = addMix(level)        
        q, answer, rightcount, wrongcount, yourans = adding(a,b,rightcount,wrongcount)
        qList.append(q)
        yourAnswer.append(yourans)
        correctAnswer.append(answer)
    finalTime = t.time()
    score, timetaken = pointGen(rightcount, inetialTime, finalTime)
    result(rightcount,level,qList,correctAnswer,yourAnswer,score,timetaken,game)

def addMix(level):
    if level == 1:
        a = r.randrange(20)
        b = r.randrange(15)
    elif level == 2:
        a = r.randrange(10,41)
        b = r.randrange(5,20)
    elif level == 3:
        a = r.randrange(20,51)
        b = r.randrange(20,30)
    elif level == 4:
        a = r.randrange(40,101,2)
        b = r.randrange(30,60)
    return a,b

def adding(a,b,rightcount,wrongcount):
    op = " + " 
    return qGen(a, b, rightcount, wrongcount,op)

def qGen(a, b, rightcount, wrongcount,op):
    q = str(a)+op+str(b)
    if op == " + ":
        c = a+b
        print(q,"=",end="")
    elif op == " - ":
        c = a-b
        print(q,"=",end="")
    elif op == " * ":
        c = a*b
        print(q,"=",end="")
    elif op == " / ":
        c = a/b
        print(q,"=",end="")
    answer = int(input())
    if answer == c:
        rightcount+=1
    else:
        wrongcount+=1
    return q,c,rightcount,wrongcount,answer

def sub(level, rightcount = 0, wrongcount = 0 ):
    game,correctAnswer,yourAnswer,qList = 'Subtraction',[],[],[]
    inetialTime = t.time()
    for k in range(10):
        print("Q",k+1,sep="",end=") ")
        a,b = subMix(level)
        q, answer, rightcount, wrongcount, yourans = subtracting(a,b,rightcount,wrongcount)
        qList.append(q)
        correctAnswer.append(answer)
        yourAnswer.append(yourans)
    finalTime = t.time()
    score, timetaken = pointGen(rightcount, inetialTime, finalTime)
    result(rightcount,level,qList,correctAnswer,yourAnswer,score,timetaken,game)

def subMix(level):
    if level == 1:
        a = r.randrange(25)
        b = r.randrange(15)
    elif level == 2:
        a = r.randrange(10,36)
        b = r.randrange(20)
    elif level == 3:
        a = r.randrange(20,50)
        b = r.randrange(10,30)
    elif level == 4:
        a = r.randrange(40,111,2)
        b = r.randrange(20,50)
    if a < b:
        a, b = b, a
    return a,b

def subtracting(a,b,rightcount,wrongcount):
    op = " - " 
    return qGen(a, b, rightcount, wrongcount,op)

def mul(level, rightcount = 0, wrongcount = 0): 
    game,correctAnswer,yourAnswer,qList = 'Multiplication',[],[],[]
    inetialTime = t.time()
    for k in range(10):
        print("Q",k+1,sep="",end=") ")
        a,b = mulMix(level)
        q, answer, rightcount, wrongcount, yourans = multipling(a,b,rightcount,wrongcount)
        qList.append(q)
        correctAnswer.append(answer)
        yourAnswer.append(yourans)
    finalTime = t.time()
    score, timetaken = pointGen(rightcount, inetialTime, finalTime)
    result(rightcount,level,qList,correctAnswer,yourAnswer,score,timetaken,game)


def mulMix(level):
    if level == 1:
        a = r.randrange(15)
        b = r.randrange(11)
    elif level == 2:
        a = r.randrange(8,20)
        b = r.randrange(12)
    elif level == 3:
        a = r.randrange(12,25)
        b = r.randrange(1,14)
    elif level == 4:
        a = r.randrange(15,30)
        b = r.randrange(10,21)
    return a,b

def multipling(a,b,rightcount,wrongcount):
    op = " * " 
    return qGen(a, b, rightcount, wrongcount,op)

def div(level, rightcount = 0, wrongcount = 0): 
    game,correctAnswer,yourAnswer,qList = 'Division',[],[],[]
    inetialTime = t.time()
    for k in range(10):
        print("Q",k+1,sep="",end=") ")
        a,b = divMix(level)
        q, answer, rightcount, wrongcount, yourans = dividing(a,b,rightcount,wrongcount)
        qList.append(q)
        correctAnswer.append(answer)
        yourAnswer.append(yourans)
    finalTime = t.time()
    score, timetaken = pointGen(rightcount, inetialTime, finalTime)
    result(rightcount,level,qList,correctAnswer,yourAnswer,score,timetaken,game)
        
def divMix(level):
    if level == 1:
        b = r.randrange(11)
        a = b*r.randrange(1,11)
        if b == 0:
            b = r.randrange(1,100,3)
    elif level == 2:
        b = r.randrange(16)
        a = b*r.randrange(1,14)
        if b == 0:
            b = r.randrange(1,111,9)
    elif level == 3:
        b = r.randrange(12,21)
        a = b*r.randrange(1,17)
    elif level == 4:
        b = r.randrange(14,25)
        a = b*r.randrange(1,21)
    return a,b

def dividing(a,b,rightcount,wrongcount):
    op = " / " 
    return qGen(a, b, rightcount, wrongcount,op)

def table(level, rightcount = 0, wrongcount = 0 ):
    game,correctAnswer,yourAnswer,qList = 'Table',[],[],[]
    inetialTime = t.time()
    for k in range(10):
        print("Q",k+1,sep="",end=") ")
        if level == 1: #practice for table 2 to 10
            a = r.randrange(2,11)
            b = r.randrange(1,11)
        elif level == 2: #practice for table 10 to 20
            a = r.randrange(10,21)
            b = r.randrange(1,11)
        elif level == 3: #practice for table 18 to 25
            a = r.randrange(18,26)
            b = r.randrange(1,11)
        elif level == 4: #pracitce for table 2 to 25
            a = r.randrange(2,26)
            b = r.randrange(1,11)               
        q, answer, rightcount, wrongcount, yourans = multipling(a,b,rightcount,wrongcount)
        qList.append(q)
        correctAnswer.append(answer)
        yourAnswer.append(yourans)
    finalTime = t.time()
    score, timetaken = pointGen(rightcount, inetialTime, finalTime)      
    result(rightcount,level,qList,correctAnswer,yourAnswer,score,timetaken,game)
    
def mix(level, rightcount = 0, wrongcount = 0,correctAnswer = [], yourAnswer = [] ):
    game = 'Miscllaneous'
    li = ['+',"-","*","/"]   
    qList =[]
    inetialTime = t.time()
    for k in range(10):
        op = li[r.randrange(4)]
        a,b = getNum(op,level)
        print("Q",k+1,sep="",end=") ")
        if op == '+':
            q, answer, rightcount, wrongcount, yourans = adding(a, b, rightcount, wrongcount)
            
        elif op == '-':
            q, answer, rightcount, wrongcount, yourans = subtracting(a, b, rightcount, wrongcount)
        
        elif op == '*':
            q, answer, rightcount, wrongcount, yourans = multipling(a, b, rightcount, wrongcount)
            
        elif op == '/':
            q, answer, rightcount, wrongcount, yourans = dividing(a, b, rightcount, wrongcount)
        qList.append(q)
        correctAnswer.append(answer)
        yourAnswer.append(yourans)
    finalTime = t.time()
    score, timetaken = pointGen(rightcount, inetialTime, finalTime)
    result(rightcount,level,qList,correctAnswer,yourAnswer,score,timetaken,game)

def selLvl(game):
    if game == 6:        
        level = int(input("Enter level\n2 to 10 press    1\n10 to 20  press  2\n18 to 25 press   3\n2 to 25 press    4\n---------> "))
    else:
        level = int(input("Enter level\nEasy       1\nNormal     2\nHard       3\nVery Hard  4\n---------> "))
    return level

def showoptn():
    print("\nChoose any option from the following to practice on")
    print("1 Addition \n2 Subtraction \n3 Multiplication")
    print("4 Division \n5 Miscllaneous\n6 Table")
    print("7 Highscor","\n8 About this programe")
    print("\npress 0 to Exit the programe...")

def info():
    print("********************************************************")
    print("********************************************************")
    print("***                                                  ***")
    print("**             MADE BY MOZAHIDUL ISLAM                **")
    print("***                virsion - 2.0.2                   ***")
    print("***                                                  ***")
    print("********************************************************")
    print("********************************************************\n")
    os.system("pause")

def showintro():
    massage = "This progrmam is made by MOZAHIDUL ISLAM \nperpos of ths program is to make your calculation faster" 
    massage+=" regarding to school project\nHope you like it...\n                        Thankyou for using\n"
    print("+----------------------------------------------------------------------------+")
    for i in massage:
        t.sleep(0.037)
        print(i,end="")
    print("+----------------------------------------------------------------------------+")

def showinfo():
    print("```````````````````````````````````````````````````````````````````````````````````````````````````````````")
    print("This project is all about the calculation. It makes your calculation speed faster and perfect.")
    print("By using this program, one can improve their calculation speed and accuracy by just practicing theis game.")
    print("Whether child of 2nd standard or any adult person, all can improve their calculation. ")
    print("It is very easy to use the program. ")
    print("After a while using this, your calculation will improve for sure.")
    print("The main purpose of this program is to learn thing in a interesting way.\n")
    print("```````````````````````````````````````````````````````````````````````````````````````````````````````````")

# showintro()

#************main programe
began()
i = 1
while i !=0:
    showoptn()
    try:
        game = int(input("Enter here: "))
        if bool(game<=8 and game >=0):
            if game == 0:
                break
            elif game == 7:
                highScore()
                continue
            elif game == 8:
                showinfo()
                continue
            level = selLvl(game)    
            if bool(level >0 and level < 5):
                if game == 1:
                    add(level)
                elif game == 2:
                    sub(level)
                elif game == 3:
                    mul(level)
                elif game == 4:
                    div(level)
                elif game == 5:
                    mix(level)
                elif game == 6:
                    table(level)
            else:       
                print("\nChoose correct option...")
        else:
            print("\nChoose correct option...")
    except:
        print("\nChoose correct option...")
        pass
info()