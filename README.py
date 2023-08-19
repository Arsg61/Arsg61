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
while True :
        print('''1.TXT FILE\n2.BINARY FILE\n3.CSV FILE\n4.OUEIT''')
        c=int(input("ENTER (1/2/3/4) :"))
        while True :
            if c==1 :
                print('''1.WRITE\n2.READ\n3.ADD\n4.QUIET''')
                b=int(input("enter (1/2/3/4)"))
                if b==1 :
                    writetxt()
                    continue
                elif b==2 :
                    readtxt()
                    continue
                elif b==3 :
                    addtxt()
                    continue
                else :
                    pass
            if c==2 :
                print('''1.WRITE\n2.READ\n3.ADD\n4.QUIET''')
                b=int(input("enter (1/2/3/4)"))
                if b==1 :
                        writebin()
                        continue
                elif b==2 :
                        readbin()
                        continue
                elif b==3 :
                        addbin()
                        continue
                else :
                        pass
            if c==3 :
                print('''1.WRITE\n2.READ\n3.ADD\n4.QUIET''')
                b=int(input("enter (1/2/3/4)"))
                if b==1 :
                    writecsv()
                    continue
                elif b==2 :
                    readcsv()
                    continue
                elif b==3 :
                    addcsv()
                    continue
                else :
                    pass
            else :
                break
        else :
            break
        

