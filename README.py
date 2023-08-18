import csv
import pickle as pic
def addtxt() :
    f=open("file.txt","a")
    l=[]
    while True :
        st=input("enter string :")
        f.write(st+"\n")
        l.append(st)
        y=input("do you want to continue (yes/no):")
        if y=='no' :
            break
    print(l)
    f.close()
def readtxt():
    f=open("file.txt","r")
    st=f.readlines()
    for line in st :
        print(line,end='')
    f.close()
def writetxt() :
    f=open("file.txt","w")
    l=[]
    while True :
        st=input("enter string :")
        f.write(st+"\n")
        l.append(st)
        y=input("do you want to continue (yes/no):")
        if y=='no' :
            break
    print("data you have filled recently : ")
    print( l)
    f.close()
def writrecsv() :
    f=open("file.csv","w",newline="")
    w=csv.writer(f) 
    while True :
        n=input("enter name :")
        r=int(input("enter roll no. "))
        m=int(input("enter marks :"))
        l=[n,r,m]
        w.writerow(l)
        n=input("enter yes or no :")
        if n=="yes" :
            break
    f.close()
def addcsv() :
    f=open("file.csv","a",newline="")
    w=csv.writer(f) 
    while True :
        n=input("enter name :")
        r=int(input("enter roll no. "))
        m=int(input("enter marks :"))
        l=[n,r,m]
        w.writerow(l)
        n=input("enter yes or no :")
        if n=="yes" :
            break
    f.close()
def readcsv() :
    f=open("file.csv","r")
    file=csv.reader(f)
    for row in file :
        print(row)
    f.close()
def writebin():
    f=open("file.dat","wb")
    while True :
        n=input("enter name :")
        r=int(input("enter roll no. "))
        m=int(input("enter marks :"))
        l={'Name':n,"Roll no.":r,"Marks":m}     
        pic.dump(l,f)
        c=input("do you want to continue (yes/no):")
        if c=="no"  :
            break
    f.close()
def addbin() :
    f=open("file.dat","ab")
    while True :
        n=input("enter name :")
        r=int(input("enter roll no. "))
        m=int(input("enter marks :"))
        l={'Name':n,"Roll no.":r,"Marks":m}     
        pic.dump(l,f)
        c=input("do you want to continue (yes/no):")
        if c=="no"  :
            break
    f.close()
def readbin() :
    f=open("file.dat","rb")
    while True :
        try : 
            d=pic.load(f)
            print(d)
        except EOFError:
            break
    f.close()
            print(d)
        except EOFError:
            break
    f.close()
  
