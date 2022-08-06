import sys
import fileinput
d={"add":"10000","sub":"10001","mov":"10010", "ld": "10100", "st": "10101", "mul":"10110","div":"10111", "rs":"11000","ls":"11001","xor":"11010","or": "11011","not":"11101","cmp":"11110","jmp":"11111","jlt":"01100","jgt":"01101","je":"01111","hlt":"01010","R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
register={"PC":-1,"000":0,"001":0,"010":0,"011":0,"100":0,"101":0,"110":0,"111":0000000000000000}
memory={}
final=[]
output=[]
def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return(decimal)
def identifyop(line):
    if line[0:5] == "10000":
        return ("add")
    if line[0:5] == "10001":
        return ("sub")
    if line[0:5] == "10010":
        return ("movI")
    if line[0:5] == "10011":
        return ("mov")
    if line[0:5] == "10100":
        return ("ld")
    if line[0:5] == "10101":
        return ("st")
    if line[0:5] == "10110":
        return ("mul")
    if line[0:5] == "10111":
        return ("div")
    if line[0:5] == "11000":
        return ("rs")
    if line[0:5] == "11001":
        return ("ls")
    if line[0:5] == "11010":
        return ("xor")
    if line[0:5] == "11011":
        return ("or")
    if line[0:5] == "11101":
        return ("not")
    if line[0:5] == "11110":
        return ("cmp")
    if line[0:5] == "11111":
        return ("jmp")
    if line[0:5] == "01100":
        return ("jlt")
    if line[0:5] == "01101":
        return ("jgt")
    if line[0:5] == "01111":
        return ("je")
    if line[0:5] == "01010":
        return ("hlt")
def simulator(line):
    global PC
    global flag
    global final
    global register
    global memory
    global abcd
    global output
    global linecount
    register["PC"]=linecount
    #TYPE A
    if identifyop(line) == "add":
        register[line[13:16]]=register[line[7:10]]+register[line[10:13]]
        if register[line[13:16]]>=2**16:
            register[line[13:16]]=register[line[13:16]]%2**16
            register["111"]="0000000000001000"
            return(0)
        register["111"]="0000000000000000"
        final+=[str(register)]
        output+=[[bin(register["PC"])[2:].zfill(8),bin(register["000"])[2:].zfill(16),bin(register["001"])[2:].zfill(16),bin(register["010"])[2:].zfill(16),bin(register["011"])[2:].zfill(16),bin(register["100"])[2:].zfill(16),bin(register["101"])[2:].zfill(16),bin(register["110"])[2:].zfill(16),(register["111"])]]
        return(0)

    if identifyop(line) == "sub":
        register[line[13:16]]=register[line[7:10]]-register[line[10:13]]
        if register[line[13:16]]<0:
            register[line[13:16]]=register[line[13:16]]%2**16
            register["111"]="0000000000001000"
            return(0)
        register["111"]="0000000000000000"
        final+=[str(register)]
        output+=[[bin(register["PC"])[2:].zfill(8),bin(register["000"])[2:].zfill(16),bin(register["001"])[2:].zfill(16),bin(register["010"])[2:].zfill(16),bin(register["011"])[2:].zfill(16),bin(register["100"])[2:].zfill(16),bin(register["101"])[2:].zfill(16),bin(register["110"])[2:].zfill(16),(register["111"])]]
        return(0)

    if identifyop(line) == "mul":
        register[line[13:16]]=register[line[7:10]]*register[line[10:13]]
        if register[line[13:16]]>=2**16:
            register[line[13:16]]=register[line[13:16]]%2**16
            register["111"]="0000000000001000"
            return(0)
        register["111"]="0000000000000000"
        final+=[str(register)]
        output+=[[bin(register["PC"])[2:].zfill(8),bin(register["000"])[2:].zfill(16),bin(register["001"])[2:].zfill(16),bin(register["010"])[2:].zfill(16),bin(register["011"])[2:].zfill(16),bin(register["100"])[2:].zfill(16),bin(register["101"])[2:].zfill(16),bin(register["110"])[2:].zfill(16),register["111"]]]
        return(0)

    if identifyop(line) == "xor":
        register[line[13:16]]=register[line[7:10]]^register[line[10:13]]
        register["111"]="0000000000000000"
        final+=[str(register)]
        output+=[[bin(register["PC"])[2:].zfill(8),bin(register["000"])[2:].zfill(16),bin(register["001"])[2:].zfill(16),bin(register["010"])[2:].zfill(16),bin(register["011"])[2:].zfill(16),bin(register["100"])[2:].zfill(16),bin(register["101"])[2:].zfill(16),bin(register["110"])[2:].zfill(16),register["111"]]]
        return(0)

    if identifyop(line) == "or":
        register[line[13:16]]=register[line[7:10]]|register[line[10:13]]
        register["111"]="0000000000000000"
        final+=[str(register)]
        output+=[[bin(register["PC"])[2:].zfill(8),bin(register["000"])[2:].zfill(16),bin(register["001"])[2:].zfill(16),bin(register["010"])[2:].zfill(16),bin(register["011"])[2:].zfill(16),bin(register["100"])[2:].zfill(16),bin(register["101"])[2:].zfill(16),bin(register["110"])[2:].zfill(16),register["111"]]]
        return(0)

    if identifyop(line) == "and":
        register[line[13:16]]=register[line[7:10]]&register[line[10:13]]
        register["111"]="0000000000000000"
        final+=[str(register)]
        output+=[[bin(register["PC"])[2:].zfill(8),bin(register["000"])[2:].zfill(16),bin(register["001"])[2:].zfill(16),bin(register["010"])[2:].zfill(16),bin(register["011"])[2:].zfill(16),bin(register["100"])[2:].zfill(16),bin(register["101"])[2:].zfill(16),bin(register["110"])[2:].zfill(16),register["111"]]]
        return(0)

    #TYPE B 
    if identifyop(line) == "mov":
        register[line[13:16]]=int(register[line[10:13]])

        register["111"]="0000000000000000"
        final+=[str(register)]
        output+=[[bin(register["PC"])[2:].zfill(8),bin(register["000"])[2:].zfill(16),bin(register["001"])[2:].zfill(16),bin(register["010"])[2:].zfill(16),bin(register["011"])[2:].zfill(16),bin(register["100"])[2:].zfill(16),bin(register["101"])[2:].zfill(16),bin(register["110"])[2:].zfill(16),register["111"]]]
        print(register)
        return(0)

    if identifyop(line) == "rs":
        register[line[5:8]]=register[line[8:11]]>>register[line[11:14]]
        register["111"]="0000000000000000"
        final+=[str(register)]
        output+=[[bin(register["PC"])[2:].zfill(8),bin(register["000"])[2:].zfill(16),bin(register["001"])[2:].zfill(16),bin(register["010"])[2:].zfill(16),bin(register["011"])[2:].zfill(16),bin(register["100"])[2:].zfill(16),bin(register["101"])[2:].zfill(16),bin(register["110"])[2:].zfill(16),register["111"]]]
        return(0)

    if identifyop(line) == "ls":
        register[line[5:8]]=register[line[8:11]]<<register[line[11:14]]
        register["111"]="0000000000000000"
        final+=[str(register)]
        output+=[[bin(register["PC"])[2:].zfill(8),bin(register["000"])[2:].zfill(16),bin(register["001"])[2:].zfill(16),bin(register["010"])[2:].zfill(16),bin(register["011"])[2:].zfill(16),bin(register["100"])[2:].zfill(16),bin(register["101"])[2:].zfill(16),bin(register["110"])[2:].zfill(16),register["111"]]]
        return(0)

    #TYPE C
    if identifyop(line) == "movI":
        register[line[5:8]]=binaryToDecimal(int(line[8:16]))
        register["111"]="0000000000000000"
        final+=[str(register)]
        output+=[[bin(register["PC"])[2:].zfill(8),bin(register["000"])[2:].zfill(16),bin(register["001"])[2:].zfill(16),bin(register["010"])[2:].zfill(16),bin(register["011"])[2:].zfill(16),bin(register["100"])[2:].zfill(16),bin(register["101"])[2:].zfill(16),bin(register["110"])[2:].zfill(16),register["111"]]]
        return(0)

    if identifyop(line) == "div":
        register["000"]=register[line[10:13]]/register[line[13:16]]
        register["001"]=register[line[10:13]]%register[line[13:16]]
        register["111"]="0000000000000000"
        final+=[str(register)]
        output+=[[bin(register["PC"])[2:].zfill(8),bin(register["000"])[2:].zfill(16),bin(register["001"])[2:].zfill(16),bin(register["010"])[2:].zfill(16),bin(register["011"])[2:].zfill(16),bin(register["100"])[2:].zfill(16),bin(register["101"])[2:].zfill(16),bin(register["110"])[2:].zfill(16),register["111"]]]
        return(0)

    if identifyop(line) == "not":
        register[line[13:16]]=~register[line[10:13]]
        register["111"]="0000000000000000"
        final+=[str(register)]
        output+=[[bin(register["PC"])[2:].zfill(8),bin(register["000"])[2:].zfill(16),bin(register["001"])[2:].zfill(16),bin(register["010"])[2:].zfill(16),bin(register["011"])[2:].zfill(16),bin(register["100"])[2:].zfill(16),bin(register["101"])[2:].zfill(16),bin(register["110"])[2:].zfill(16),register["111"]]]
        return(0)

    if identifyop(line) == "cmp":
        register["111"]="0000000000000000"

        if register[line[10:13]]>register[line[13:16]]:
            register["111"]="0000000000000010"

        elif register[line[10:13]]<register[line[13:16]]:
            register["111"]="0000000000000100"

        elif register[line[10:13]]==register[line[13:16]]:
            register["111"]="0000000000000001"

        final+=[str(register)]
        output+=[[bin(register["PC"])[2:].zfill(8),bin(register["000"])[2:].zfill(16),bin(register["001"])[2:].zfill(16),bin(register["010"])[2:].zfill(16),bin(register["011"])[2:].zfill(16),bin(register["100"])[2:].zfill(16),bin(register["101"])[2:].zfill(16),bin(register["110"])[2:].zfill(16),(register["111"])]]
        return(0)

    #TYPE D
    if identifyop(line) == "ld":
        if line[8:16] not in memory:
            memory[line[8:16]]=0
        register[line[5:8]]=memory[line[8:16]]
        register["111"]="0000000000000000"
        final+=[str(register)]
        output+=[[bin(register["PC"])[2:].zfill(8),bin(register["000"])[2:].zfill(16),bin(register["001"])[2:].zfill(16),bin(register["010"])[2:].zfill(16),bin(register["011"])[2:].zfill(16),bin(register["100"])[2:].zfill(16),bin(register["101"])[2:].zfill(16),bin(register["110"])[2:].zfill(16),register["111"]]]
        return(0)

    if identifyop(line) == "st":
        if line[8:16] not in memory:
            memory[line[8:16]]=0
        memory[line[8:16]]=register[line[5:8]]
        register["111"]="0000000000000000"
        final+=[str(register)]
        output+=[[bin(register["PC"])[2:].zfill(8),bin(register["000"])[2:].zfill(16),bin(register["001"])[2:].zfill(16),bin(register["010"])[2:].zfill(16),bin(register["011"])[2:].zfill(16),bin(register["100"])[2:].zfill(16),bin(register["101"])[2:].zfill(16),bin(register["110"])[2:].zfill(16),register["111"]]]
        return(0)

    #TYPE E 
    if identifyop(line) == "jmp":
        final+=[str(register)]
        register["111"]="0000000000000000"
        output+=[[bin(register["PC"])[2:].zfill(8),bin(register["000"])[2:].zfill(16),bin(register["001"])[2:].zfill(16),bin(register["010"])[2:].zfill(16),bin(register["011"])[2:].zfill(16),bin(register["100"])[2:].zfill(16),bin(register["101"])[2:].zfill(16),bin(register["110"])[2:].zfill(16),register["111"]]]
        return(binaryToDecimal(int(line[8:16])))
        
    if identifyop(line) == "jlt":
        final+=[str(register)]
        if register["111"]=="0000000000000100":
            register["111"]="0000000000000000"
            output+=[[bin(register["PC"])[2:].zfill(8),bin(register["000"])[2:].zfill(16),bin(register["001"])[2:].zfill(16),bin(register["010"])[2:].zfill(16),bin(register["011"])[2:].zfill(16),bin(register["100"])[2:].zfill(16),bin(register["101"])[2:].zfill(16),bin(register["110"])[2:].zfill(16),register["111"]]]
            return(binaryToDecimal(int(line[8:16])))
        else:
            register["111"]="0000000000000000"
            output+=[[bin(register["PC"])[2:].zfill(8),bin(register["000"])[2:].zfill(16),bin(register["001"])[2:].zfill(16),bin(register["010"])[2:].zfill(16),bin(register["011"])[2:].zfill(16),bin(register["100"])[2:].zfill(16),bin(register["101"])[2:].zfill(16),bin(register["110"])[2:].zfill(16),register["111"]]]
            return(0)
    if identifyop(line) == "jgt":
        final+=[str(register)]
        if register["111"]=="0000000000000010":
            register["111"]="0000000000000000"
            output+=[[bin(register["PC"])[2:].zfill(8),bin(register["000"])[2:].zfill(16),bin(register["001"])[2:].zfill(16),bin(register["010"])[2:].zfill(16),bin(register["011"])[2:].zfill(16),bin(register["100"])[2:].zfill(16),bin(register["101"])[2:].zfill(16),bin(register["110"])[2:].zfill(16),register["111"]]]
            jumpnum=binaryToDecimal(int(line[8:16]))
            return(jumpnum)
        else:
            register["111"]="0000000000000000"
            output+=[[bin(register["PC"])[2:].zfill(8),bin(register["000"])[2:].zfill(16),bin(register["001"])[2:].zfill(16),bin(register["010"])[2:].zfill(16),bin(register["011"])[2:].zfill(16),bin(register["100"])[2:].zfill(16),bin(register["101"])[2:].zfill(16),bin(register["110"])[2:].zfill(16),register["111"]]]
            return(0)
    if identifyop(line) == "je":
        print("OUTHERE",register["111"])
        final+=[str(register)]
        if register["111"]=="0000000000000001":
            register["111"]="0000000000000000"
            output+=[[bin(register["PC"])[2:].zfill(8),bin(register["000"])[2:].zfill(16),bin(register["001"])[2:].zfill(16),bin(register["010"])[2:].zfill(16),bin(register["011"])[2:].zfill(16),bin(register["100"])[2:].zfill(16),bin(register["101"])[2:].zfill(16),bin(register["110"])[2:].zfill(16),register["111"]]]
            return(binaryToDecimal(int(line[8:16])))
        else:
            register["111"]="0000000000000000"
            output+=[[bin(register["PC"])[2:].zfill(8),bin(register["000"])[2:].zfill(16),bin(register["001"])[2:].zfill(16),bin(register["010"])[2:].zfill(16),bin(register["011"])[2:].zfill(16),bin(register["100"])[2:].zfill(16),bin(register["101"])[2:].zfill(16),bin(register["110"])[2:].zfill(16),register["111"]]]
            return(0)
    #TYPE F
    if identifyop(line) == "hlt":
        register["111"]="0000000000000000"
        final+=[str(register)]
        output+=[[bin(register["PC"])[2:].zfill(8),bin(register["000"])[2:].zfill(16),bin(register["001"])[2:].zfill(16),bin(register["010"])[2:].zfill(16),bin(register["011"])[2:].zfill(16),bin(register["100"])[2:].zfill(16),bin(register["101"])[2:].zfill(16),bin(register["110"])[2:].zfill(16),register["111"]]]
        return(0)
abcd=[]
for line in fileinput.input():
        abcd.append(line.rstrip())
lengthlist=len(abcd)
for i in range(0,lengthlist):
    a=abcd[i].rstrip()
    abcd[i]=a
res = []
linecount=0
while abcd[linecount]!="0101000000000000":
    result=simulator(abcd[linecount])
    if result==0:
        linecount+=1
    else:
        linecount=result
    
finallines=0
for i in output:
    for j in i:
        print(j,end=" ")
    print()
print(bin(linecount)[2:].zfill(8),bin(register["000"])[2:].zfill(16),bin(register["001"])[2:].zfill(16),bin(register["010"])[2:].zfill(16),bin(register["011"])[2:].zfill(16),bin(register["100"])[2:].zfill(16),bin(register["101"])[2:].zfill(16),bin(register["110"])[2:].zfill(16),register["111"])
for key in memory.keys() :
    res.append(memory[key])
for i in abcd:
    finallines+=1
    print(i)
rep=0
if len(res)!=0:
    rep=res[0]
    del res[0]
if len(res)!=0:
    for i in res:
        finallines+=1
        print(bin(int(i))[2:].zfill(16))
if rep!=0:
    finallines+=1
    print(bin(int(rep))[2:].zfill(16))
'''print(bin(int(res[length-1]))[2:].zfill(16))'''
for i in range(0,256-finallines):
    print("0000000000000000")
