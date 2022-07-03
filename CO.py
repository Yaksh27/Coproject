from ast import Num
d={"add":"10000","sub":"10001","mov":"10010", "ld": "10100", "st": "10101", "mul":"10110","div":"10111", "rs":"11000","ls":"11001","xor":"11010","or": "11011","not":"11101","cmp":"11110","jmp":"11111","jlt":"01100","jgt":"01101","je":"01111","hlt":"01010","R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
variabledictionary={}
t=-1
haltcount=0
labels=[]
labelcountdict={}
linenumber=0
variables=[]
errornumbers=0

def errorhandling(x):
    global variables
    global labels
    global d
    global errornumbers
    varcount=0
    linecount=-1
    hltcount=0
    file=open("Coproject.txt")
    assemblylist=file.readlines()
    n=len(assemblylist)
    file.close()
    file=open("Coproject.txt")
    for i in range(0,n):
        assemblylist=file.readline().split(" ")
        u=len(assemblylist)
        x=[]
        a=''
        b=''
        linecount=linecount+1
        for j in range(0,u):
            a=assemblylist[j].rstrip()
            a=assemblylist[j].rstrip()
            assemblylist[j]=a
            b=len(assemblylist)
            check=assemblylist[j]
            checkn=len(check)
            check=assemblylist[j][checkn-1:checkn]

            if assemblylist[j][0:1]=="$":
                e=int(assemblylist[j][1:].rstrip())
                if len(bin(e)[2:])>8:
                    errornumbers=1
                    print("Error: Immediate value more than 8 bits")
                
            if check==":" and len(assemblylist)>1:
                labels=labels+[assemblylist[j][0:checkn-1]]
                if assemblylist[j+1]=="add" or "sub" or "mul" or "xor" or "or" or "and":
                    if len(assemblylist)>5 or len(assemblylist)<5:
                        errornumbers=1
                        print("Error: Number of operands may be more or less than required")
                elif assemblylist[j+1]=="mov" or "ld" or "st" or "div" or "ls" or "rs" or "not" or "cmp" or "jmp" or "jlt" or "jgt" or "je":
                    if len(assemblylist)>4 or len(assemblylist)<4:
                        errornumbers=1
                        print("Error: Number of operands may be more or less than required")
                elif assemblylist[j+1] not in d:
                    errornumbers=1
                    print("Error: Label call invalid")

            if len(assemblylist)==1:
                if assemblylist[j] not in labels and assemblylist[j]!="hlt" and assemblylist[j] not in d:
                    errornumbers=1
                    print("Error: Label call invalid")
                if check==":":
                    if assemblylist[j][0:checkn-1] in variables:
                        errornumbers=1
                        print("Error: Invalid use of variable as label")

            if assemblylist[j]=="var":
                if len(assemblylist)>2:
                    errornumbers=1
                    print("Error: More than one variable ")
                if len(assemblylist)==2:
                    varcount=varcount+1
                    p=[assemblylist[j+1].rstrip()]
                    variables=variables+p
            if varcount==0:
                errornumbers=1
                print("Error: Variables not defined in the begining")
                varcount=varcount+1

            if assemblylist[j]=="hlt":
                hltcount=hltcount+1
                if n-linecount>1:
                    errornumbers=1
                    print("Error: hlt command not in the end")

            if assemblylist[j]==assemblylist[j-1] and len(assemblylist)>1:
                errornumbers=1
                print("Error: Repeatation of operand",assemblylist[j-1])
            if assemblylist[j] in d:
                print(assemblylist[j])
                if assemblylist[j]==["add","sub","mul","xor","or","and"]:
                    print(assemblylist[j])
                    if len(assemblylist)>4 or len(assemblylist)<4:
                        errornumbers=1
                        print("Error: Number of operands may be more or less than required",assemblylist[j],assemblylist)
                    for w in range(0,n):
                        checkdollar=assemblylist[w]
                        if checkdollar[0]=="$":
                            errornumbers=1
                            print("Error: Immediate value cannot be operated in this command",assemblylist[j],assemblylist)
                if assemblylist[j]=="mov" or "ld" or "st" or "div" or "ls" or "rs" or "not" or "cmp" or "jmp" or "jlt" or "jgt" or "je":
                    if len(assemblylist)>3 or len(assemblylist)<3:
                        errornumbers=1
                        print("Error: Number of operands may be more or less than required")
                    if assemblylist[j]=="div" or "not" or "cmp" or "ld" or "st":
                        for w in range(0,n):
                                checkdollar=assemblylist[w]
                                if checkdollar[0]=="$":
                                    errornumbers=1
                                    print("Error: Immediate value cannot be operated in this command")
                    if len(assemblylist)==3:
                        if assemblylist[j]=="mov" or "rs" or "ls":
                            if assemblylist[j+2][0:1] != "$":
                                errornumbers=1
                                print("Error: Invalid immediate value ")
                        if assemblylist[j+2] in labels and assemblylist[j]=="ld" or "st" :
                            errornumbers=1
                            print("Error: Invalid use of label instead of variable")
                            if assemblylist[j+2] not in variables not in labels:
                                errornumbers=1
                                print("Error: Use of undefined variables")
            if assemblylist[j] not in d:
                errornumbers=1
                print("Error: check for typo")
            if assemblylist[j]=="FLAGS":
                if assemblylist[j-1]!="mov":
                    errornumbers=1
                    print("Error: Illegal use of FLAGS")  
    return errornumbers
def final(MachineLanguage):
    n=len(MachineLanguage)
    h=16-n
    if h==0:
        return MachineLanguage
    if h==5:
        assemblylist=MachineLanguage[0:5]
        b=MachineLanguage[5:n]
        y=''
        y=y+assemblylist
        y=y+"00000"
        y=y+b
        return y
    if h==2:
        assemblylist=MachineLanguage[0:5]
        b=MachineLanguage[5:n]
        y=''
        y=y+assemblylist
        y=y+"00"
        y=y+b
        return y
    if h==3:
        assemblylist=MachineLanguage[0:5]
        b=MachineLanguage[5:n]
        y=''
        y=y+assemblylist
        y=y+"000"
        y=y+b
        return y
def Identify(assemblystatement):
    for i in d:
        if i==assemblystatement:
            return(d[i])
        elif assemblystatement[0]=="$":
            n = len(assemblystatement)
            x = int(assemblystatement[1:n])
            s = ""
            y = assemblystatement[0]
            if y == "$": 
                p=str(bin(x))
            n=len(p)
            b=''
            for i in range(2,n):
                b=b+p[i]
            empty = len(b)
            h = 8 - empty
            res = b.zfill(h + len(b))
            return(str(res))
errornumbers=0
if errornumbers==0:
    file=open("Coproject.txt")
    assemblylist=file.readlines()
    n=len(assemblylist)
    file.close()
    file=open("Coproject.txt")
    for i in range(0,n):
        w=''
        MachineLanguage=''
        assemblylist=file.readline().split(" ")
        u=len(assemblylist)
        x=[]
        a=''
        b=''
        for i in range(0,u):
            a=assemblylist[i].strip()
            assemblylist[i]=a
            b=len(assemblylist)
        if b==5:
            linenumber=linenumber+1
            for h in range(0,5):
                labelcount=len(assemblylist[h])
                if (assemblylist[h][labelcount-1:labelcount])==":":
                    labelcountdict[assemblylist[h][0:labelcount-1]]=linenumber
                if assemblylist[h] in d:
                    w=str(assemblylist[h])
                    MachineLanguage=MachineLanguage+Identify(w.rstrip())   
            print(final(MachineLanguage))
        if b==4:
            linenumber=linenumber+1
            for i in range(0,4):
                labelcount=len(assemblylist[i])
                if (assemblylist[i][labelcount-1:labelcount])==":":
                    print("yes")
                    labelcountdict[str(assemblylist[0][0:n-1])]=int(linenumber)
                if assemblylist[i] in d:
                    w=str(assemblylist[i])
                    MachineLanguage=MachineLanguage+Identify(w.rstrip()) 
            print(final(MachineLanguage))
        elif b==3:
            linenumber=linenumber+1
            for i in range(0,3):
                labelcount=len(assemblylist[i])
                if (assemblylist[i][labelcount-1:labelcount])==":":
                    print("yes")
                    labelcountdict[str(assemblylist[0][0:n-1])]=int(linenumber)
                if assemblylist[i] in d:
                    w=assemblylist[i].rstrip()
                    MachineLanguage=MachineLanguage+Identify(w.rstrip())
                check=assemblylist[i]
                if check[0]=="$":
                    w=assemblylist[i].rstrip()
                    MachineLanguage=MachineLanguage+Identify(w.rstrip())    
            print(final(MachineLanguage))
        elif b==2:
            linenumber=linenumber+1
            c=0
            for i in range(0,2):
                labelcount=len(assemblylist[i])
                if (assemblylist[i][labelcount-1:labelcount])==":":
                    print("yes")
                    labelcountdict[str(assemblylist[0][0:n-1])]=int(linenumber)
                if assemblylist[i]=="var":
                    linenumber=linenumber-1
                    binaryconversion=bin(n+t)[2:]
                    d[assemblylist[i+1].rstrip()]=str(binaryconversion.zfill(8))
                    break
                if assemblylist[i] in d:
                    c=1
                    w=str(assemblylist[i])
                    MachineLanguage=MachineLanguage+Identify(w.rstrip())    
            if c==1:
                print(final(MachineLanguage))
        elif b==1:
            linenumber=linenumber+1
            haltcount=1
            for i in range(0,1):
                if assemblylist[i] in labelcountdict:
                    akshay=bin(labelcountdict[assemblylist[i]])
                    MachineLanguage=MachineLanguage+str(akshay[2:].zfill(8))
                if assemblylist[i] in d:
                    w=str(assemblylist[i])
                    MachineLanguage=MachineLanguage+Identify(w.rstrip())
                    MachineLanguage=MachineLanguage+"00000000000"
                print(MachineLanguage)
if haltcount==0:
    print("Error: Missin hlt instruction")