import os

def fileCreation():
    path = os.path.abspath("StudentsFile.txt")
    isExixts = os.path.exists(path)
    if not isExixts:
        f = open("StudentsFile.txt","w")
        f.write(" Name|Age|Class|Section\n ")
        f.close()
        myfunction()
    else:
        myfunction()

def writing():
    print("Enter the student name")
    stuName = input()
    print("Enter the student age")
    stuAge = input()
    print("Enter the student class")
    stuClass = input()
    print("Enter the student section")
    stuSection = input()
    f = open("StudentsFile.txt","a")
    f.write(stuName+"|"+stuAge+"|"+stuClass+"|"+stuSection+"\n ")
    f.close()
    myfunction()

def reading():
    f = open("StudentsFile.txt","r")
    print(f.read())
    f.close()
    myfunction()

def myfunction():
    print("Press 1 to read the file\nPress 2 to enter the student details\nPress 3 to exit")
    num = getinput()
    if num==1:
        reading()
    elif num==2:
        writing()
    elif num==3:
        print("Terminating.")
        os._exit(0)

def getinput():
    num = 0
    try:
        num = int(input())
        if num in [1,2,3]:
            return num
        else:
            print("Invalid input\n")
            getinput()
    except:
        print("Invalid input\n")
        getinput()



fileCreation()
	  
