#uses miller-rabin probability test
#finds and returns k and m needed for the miller rabin proability test
def twokm(num,k):
    num = num-1
    remaindernum = num%(2**k)
    test = True
    while test:
        if remaindernum == 0:
            k = k+1
            remaindernum = num%(2**k)
        else:
            numtoreturn = num/(2**(k-1))
            test = False
    return k-1, numtoreturn
#Undergoes step 3 of the process. Returns true if probably prime, and false if not prime
def modulo(somenum, bO, occ):
    if occ>50:
        return False
    if occ ==0:
        if bO%somenum == 1 or bO%somenum == somenum -1:
            return True
        else:
            return modulo(somenum,exponent(bO,2),occ+1)
    if (bO)%somenum == somenum -1:
        return True
    elif(bO)%somenum != 1:
        return modulo(somenum,exponent(bO,2),occ+1)
    else:
        return False
#custom exponent function
def exponent(num, exp):
    if exp == 0:
        return 1
    if exp%2 == 0:
        y = exponent(num,exp/2)
        return y*y
    else:
        y = exponent(num, (exp-1)/2)
        return num*y*y
"""
Prompts the user to enter a number if input does not include a number
Returns not a prime if entered number is less than 1, or a decimal
Performs the three step process if the given number is greater than two, and not a decimal         
"""
def isPrime(somenum):
    try:
        testnum = int(somenum)
        if "." in somenum:
            return "The number, "+ str(somenum) + " is not prime, it is  a decimal"
    except:
        return "Sorry, please enter a number"
    somenum = int(somenum)    
    if somenum <= 1:
        return str(somenum) + " is not prime"
    elif somenum == 2:
        return str(somenum) + " is prime"
    elif somenum%2 == 0:
        return str(somenum) + "is not prime"
    else:
        stuff = twokm(somenum,1)  
        BO = (exponent(2,stuff[1]))%somenum
        if(modulo(somenum,BO, 0)):
            return  str(somenum) + " is prime"
        else:
            return str(somenum) + " is not prime"
            




    