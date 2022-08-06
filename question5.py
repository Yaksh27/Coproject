#Q5(Bonus Question)
import math
print("-------------------------------------Type 1------------------------------------------")
print()
Dict = {'Bit addressable memory' : 1 ,'Nibble addressable memory' : 4, 'Byte addressable memory' : 8} 

#Type1 

inst_length=int(input("Enter your Instruction Length: "))
reg_length=int(input("Enter Register Length: "))

#Initial input
print()
print("Enter your initial input:")
inp_mem=input("Input Memory Space: ")

mem_unit = {"KB" : 2**10 , "MB" : 2**20 , "GB" : 2**30}
inp_mem=inp_mem.split()
bits=int(inp_mem[0])*(2**10)                      #converting input memory to bits
x = math.log(bits) / math.log(2)                  #x value is the power of input memory after converting into bits which is in the form 2**x
#print(x)
print()
print("1.Bit addressable memory")
print("2.Byte addressable memory")
print("3.Nibble addressable memory")
print("4.Word addressable memory ")
print()
address_type=input("Enter Address Type option: ")
if(address_type=="2"):
    address_pins=2**x/Dict["Byte addressable memory"]                        #Calculating number of initial address pins
    y=math.log(address_pins)/math.log(2)          #y value is the power of address pins which is in the form 2**y

elif(address_type=="3"):
    address_pins=2**x/Dict["Nibble addressable memory"] 
    y=math.log(address_pins)/math.log(2)

elif(address_type=="1"):
    address_pins=2**x/2**1
    y=math.log(address_pins)/math.log(2)

elif(address_type=="4"):
    address_pins=2**x/2**4
    y=math.log(address_pins)/math.log(2)

#print(y)


print()
print("The minimum bits needed for architecture: ", y)
print("The number of bits need by opcode: ",inst_length - y - reg_length)
print("The number of filler bits in Instruction type 2: ",inst_length - (inst_length - y - reg_length) - reg_length)
print("Maximum numbers of instructions this ISA can support: ",2**(inst_length-y-reg_length))
print("Maximum number of registers this ISA can support: ",2**reg_length)
print()

print("Enter current input: ")
bitCPU=int(input("Enter the number bits in CPU: "))
print()
print("1.Bit addressable memory")
print("2.Byte addressable memory")
print("3.Nibble addressable memory")
print("4.Word addressable memory: ")
print()
address_type2=input("Enter the enhanced address type option: ")
if(address_type2=="4"):
    g=math.log(bitCPU)/math.log(2)
    print()
    new_pins=2**x/2**g                  #Calculating the number of new address pins

elif(address_type2=='2'):
    print()
    new_pins=2**x/Dict["Byte addressable memory"]

elif(address_type2=='1'):
    print()
    new_pins=2**x/2

elif(address_type2=='3'):
    print()
    new_pins=2**x/Dict["Nibble addressable memory"]

z=math.log(new_pins)/math.log(2)                       #final number of new address pins
output=y-z                                             #calculating the saved or required amount of pins
if(y>z):
    print("Number of pins saved: -",int(output))

else:
    print("Number of pins required: +",int(output))

print()
print("-------------------------------------Type 2------------------------------------------")
print()
bitCPU = input("Enter the number bits in CPU: ") #Number of bits in CPU
bitCPU = bitCPU.split()
address_pins = input("Enter the number of address pins: ") #Number of address pins
address_pins = address_pins.split()
print()
print("1.Bit addressable memory")
print("2.Byte addressable memory")
print("3.Nibble addressable memory")
print("4.Word addressable memory")
print()
address_memory = input("Enter the type of addressable memory: ") #Type of addressable memory

number_address = 2**int(address_pins[0])  #possible number of memory address

if(address_memory in Dict):
    a = number_address/8             #conversion to bytes
    b = a/1024                       #conversion to KB
    b = b/1024                       #conversion to MB  
    b = b/1024                       #conversion to GB

    print()
    final_output = Dict[address_memory]*b
    print("The size of main memory is: ",int(final_output),'GB')

elif(address_memory == "Word addressable memory"):
    a = number_address/8             #conversion to bytes
    b = a/1024                       #conversion to KB
    b = b/1024                       #conversion to MB  
    b = b/1024                       #conversion to GB

    print()
    final_output = b*int(bitCPU[0])
    print("The size of main memory is: ",int(final_output),"GB")
