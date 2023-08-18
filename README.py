import csv
def addtxt() :
    f=open("rrr.txt","a")
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
    f=open("rrr.txt","r")
    st=f.readlines()
    for line in st :
        print(line,end='')
    f.close()
def txt() :
    f=open("rrr.txt","w")
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
    f=open("rrr.csv","a",newline="")
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
        
