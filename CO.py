import sys
import fileinput
d={"add":"10000","sub":"10001","mov":"10010", "ld": "10100", "st": "10101", "mul":"10110","div":"10111", "rs":"11000","ls":"11001","xor":"11010","or": "11011","not":"11101","cmp":"11110","jmp":"11111","jlt":"01100","jgt":"01101","je":"01111","hlt":"01010","R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
labels=[]
variables=[]
errornumbers=0
t=1
haltcount=0
labelcountdict={}
linenumber=-1
abcd=[]
def errorhandling(x):
    global variables
    global labels
    global d
    global errornumbers
    varcount=0
    linecount=-1
    hltcount=0
    global abcd
    for line in fileinput.input():
        abcd.append(line.rstrip())
    #print(abcd)
    n=len(abcd)
    errorlinecount=0
    assemblylist=[]
    for i in range(0,n):
        #print(i)
        assemblylist=abcd[i].split()
        #print(assemblylist,"here")
        u=len(assemblylist)
        x=[]
        a=''
        b=''
        for i in range(0,u):
            a=assemblylist[i].rstrip()
            assemblylist[i]=a
            errorlinecount=errorlinecount+1
        linecount=linecount+1
        for j in range(0,u):
            a=assemblylist[j].rstrip()
            a=assemblylist[j].rstrip()
            assemblylist[j]=a
            b=len(assemblylist)
            check=assemblylist[j]
            checkn=len(check)
            check=assemblylist[j][checkn-1:checkn]
            ll=len(assemblylist[0])

            if assemblylist[j][0:1]=="$" and assemblylist[j][1:].rstrip().isdecimal():
                e=int(assemblylist[j][1:].rstrip())
                if len(bin(e)[2:])>8:
                    errornumbers=1
                    print("Error: Immediate value more than 8 bits at",assemblylist,"in",assemblylist[j])
                
            if check==":" and len(assemblylist)>1:
                labels=labels+[assemblylist[j][0:checkn-1]]
                if assemblylist[j+1]=="add" or "sub" or "mul" or "xor" or "or" or "and":
                    if len(assemblylist)>5 or len(assemblylist)<5 and assemblylist[0][ll-1:ll]!=":":
                        errornumbers=1
                        print("Error: Number of operands may be more or less than required at",assemblylist,"in",assemblylist[j])
                elif assemblylist[j+1]=="mov" or "ld" or "st" or "div" or "ls" or "rs" or "not" or "cmp" or "jmp" or "jlt" or "jgt" or "je":
                    if len(assemblylist)>4 or len(assemblylist)<4:
                        errornumbers=1
                        print("Error: Number of operands may be more or less than required at",assemblylist,"in",assemblylist[j])
                elif assemblylist[j+1] not in d:
                    errornumbers=1
                    print("Error: Label call invalid at",assemblylist,"in",assemblylist[j])

            if len(assemblylist)==1:
                if assemblylist[j] not in labels and assemblylist[j]!="hlt" and assemblylist[j] not in d:
                    errornumbers=1
                    print("Error: Label call invalid at",assemblylist,"in",assemblylist[j])
                if check==":":
                    if assemblylist[j][0:checkn-1] in variables:
                        errornumbers=1
                        print("Error: Invalid use of variable as label at",assemblylist,"in",assemblylist[j])

            if assemblylist[j]=="var":
                if len(assemblylist)>2:
                    errornumbers=1
                    print("Error: More than one variable at ",assemblylist,"in",assemblylist[j])
                if len(assemblylist)==2:
                    varcount=varcount+1
                    p=[assemblylist[j+1].rstrip()]
                    variables=variables+p
            if varcount==0:
                errornumbers=1
                print("Error: Variables not defined in the begining at",assemblylist,"in",assemblylist[j])
                varcount=varcount+1

            if assemblylist[j]=="hlt":
                hltcount=hltcount+1
                if n-linecount>1:
                    errornumbers=1
                    print("Error: hlt command not in the end at",assemblylist,"in",assemblylist[j])

            if assemblylist[j]==assemblylist[j-1] and len(assemblylist)>1:
                errornumbers=1
                print("Error: Repeatation of operand",assemblylist[j-1])
            if assemblylist[j] in d:
                if assemblylist[j] in ["add","sub","mul","xor","or","and"]:
                    if len(assemblylist)>4 or len(assemblylist)<4:
                        if assemblylist[0][ll-1:ll]!=":":
                            errornumbers=1
                            print("Error: Number of operands may be more or less than required at",assemblylist,"in",assemblylist[j])
                    for w in range(0,b):
                        checkdollar=assemblylist[w]
                        if checkdollar[0]=="$":
                            errornumbers=1
                            print("Error: Immediate value cannot be operated in this command at",assemblylist,"in",assemblylist[j])
                if assemblylist[j] in ["mov","ld","st","div","ls","rs","not","cmp"]:
                    ll=len(assemblylist[0])
                    if len(assemblylist)>3 or len(assemblylist)<3:
                        if assemblylist[0][ll-1:ll]!=":":
                            errornumbers=1
                            print("Error: Number of operands may be more or less than required at",assemblylist,"in",assemblylist[j])
                    if assemblylist[j] in ["div","not","cmp","ld","st"]:
                        for w in range(0,b):
                                checkdollar=assemblylist[w]
                                if checkdollar[0]=="$":
                                    errornumbers=1
                                    print("Error: Immediate value cannot be operated in this command at",assemblylist,"in",assemblylist[j])
                    if len(assemblylist)==3:
                        if assemblylist[j]=="mov" or "rs" or "ls":
                            if assemblylist[j] in ["ls","rs"]:
                                if assemblylist[j+2][0:1] != "$":
                                    errornumbers=1
                                    print("Error: Invalid immediate value at",assemblylist,"in",assemblylist[j])
                        if assemblylist[j] in ["ld","st"]:
                            if assemblylist[j+2] in labels :
                                errornumbers=1
                                print("Error: Invalid use of label instead of variable at",assemblylist,"in",assemblylist[j])
                            if assemblylist[j+2] not in variables not in labels:
                                errornumbers=1
                                print("Error: Use of undefined variables at",assemblylist,"in",assemblylist[j])
                if assemblylist[j] in ["jmp","jlt","je","jgt"]:
                    if len(assemblylist)>1:
                        if assemblylist[j+1] not in labels:
                            errornumbers=1
                            print("Error: Invalid memory address operand")
                    if len(assemblylist)>2 or len(assemblylist)<2:
                        errornumbers=1
                        print("Error: Number of operands may be more or less than required at",assemblylist,"in",assemblylist[j])       
            lengthlab=len(assemblylist[j])
            if assemblylist[j] not in d and assemblylist[j][0:1]!="$" and assemblylist[j][lengthlab-1:lengthlab] not in [":"] and assemblylist[j] not in labels and assemblylist[j] not in variables and assemblylist[j]!="var":
                errornumbers=1
                print("Error: check for typo at",assemblylist,"in",assemblylist[j])
            if assemblylist[j]=="FLAGS":
                if assemblylist[j-1]!="mov":
                    errornumbers=1
                    print("Error: Illegal use of FLAGS at",assemblylist,"in",assemblylist[j])
    if hltcount==0:
        errornumbers=1
        print("Error: No hlt instruction given")
    if errornumbers==0:
        print("NO ERRORS DETECTED , WE DONE BOYS!!!")
    return errornumbers
def testvar(n):
    varcount=0
    global abcd
    n=len(abcd)
    for i in range(0,n):
        w=''
        MachineLanguage=''
        assemblylistq=abcd[i].split()
        u=len(assemblylistq)
        x=[]
        a=''
        b=''
        for i in range(0,u):
            a=assemblylistq[i].strip()
            assemblylistq[i]=a
            b=len(assemblylistq)
            if a=="var":
                varcount=varcount+1
    return varcount
varcount=testvar(1)
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
x=errorhandling(1)
if x==0:
    n=len(abcd)
    for i in range(0,n):
        w=''
        MachineLanguage=''
        assemblylist=abcd[i].split()
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
            if assemblylist[0]!="var":
                linenumber=linenumber+1
            c=0
            for i in range(0,2):
                labelcount=len(assemblylist[i])
                if (assemblylist[i][labelcount-1:labelcount])==":":
                    labelcountdict[str(assemblylist[0][0:n-1])]=int(linenumber)
                if assemblylist[i]=="var":
                    binaryconversion=bin(n-varcount)[2:]
                    varcount=varcount-1
                    d[assemblylist[i+1].rstrip()]=str(binaryconversion.zfill(8))
                    break
                if assemblylist[i] in d:
                    c=1
                    w=str(assemblylist[i])
                    MachineLanguage=MachineLanguage+Identify(w.rstrip())
                if assemblylist[i] in labelcountdict:
                    c=1
                    akshay=bin(labelcountdict[assemblylist[i]])
                    MachineLanguage=MachineLanguage+str(akshay[2:].zfill(8))
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
