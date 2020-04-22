def pXOR(x,y,z):                    #XOR for 3 input 
    val=(( ~x & y )|(x & ~y ))  
    return ((~val & z)|(val & ~z))

def cXOR(p,q,r,s):                  #XOR for 4 input 
    val=(( ~p & q )|(p & ~q ))
    val1=(( ~r & s )|(r & ~s )) 
    return ((~val & val1)|(val & ~val1))

def concat(a, b ,c):                #concatinating integers i.e c3c2c1
    return int(f"{a}{b}{c}")
def binaryToDecimal(binary):        #convert binary code to decimal
      
    (binary1) = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return(decimal)

# program to do error detection 
def main():
    l=[]
    length=int(input("Enter length of hamming code:"))
    for i in range(length):
        code=int(input("Enter single bit of  hamming code:"))
        l.append(code)

    p1=l[0]
    p2=l[1]
    d1=l[2]
    p3=l[3]
    d2=l[4]
    d3=l[5]
    d4=l[6]

    print ("p1=",p1)
    print("p2=",p2)
    print("d1=",d1)
    print("p3=",p3)
    print("d2=",d2)
    print("d3=",d3)
    print("d4=",d4)
    print("\nValue of p1=",pXOR(d1,d2,d4))
    print("Value of p2=",pXOR (d1,d3,d4))
    print("Value of p3=",pXOR (d2,d3,d4))
    print("\nValue of c1=",cXOR(d1,d2,d4,p1))
    print("Value of c2=",cXOR(d1,d3,d4,p2))
    print("Value of c3=",cXOR(d2,d3,d4,p3))

    check_parity=concat(cXOR(d1,d2,d4,p1),cXOR(d1,d3,d4,p2),cXOR(d2,d3,d4,p3))
    if check_parity ==000:
        return 0
    else:
        res= binaryToDecimal(check_parity)
        return res
def transmit():
    print("Transmitted code")  
    res=  main()
    if res==0:
        print("Error free so no error correction required")
    else:
          print("Error at position",res)
def receive():
    print("Received code")  
    res=main()
    if res==0:
        print("Error free so no error correction required")
    else:
        print("Error at position",res)
        

transmit()
receive()
end


    
