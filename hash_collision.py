import hashlib
import os

def hash_collision(k):
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
   
    #Collision finding code goes here
    x = b'\x00'
    y = b'\x00'
    x = os.urandom(64)
    y = os.urandom(64)
    scale = 16 ## equals to hexadecimal

    xBitsTotal=bin(int(hashlib.sha256(x).hexdigest(), scale))[2:]
    yBitsTotal=bin(int(hashlib.sha256(y).hexdigest(), scale))[2:]
    
    match=False
    while(match==False):
        newK=len(xBitsTotal)-k
        yLastKbits=yBitsTotal[newK:len(yBitsTotal)]
        xLastKbits=xBitsTotal[newK:len(xBitsTotal)]

        if(yLastKbits==xLastKbits):
            match=True
        else:
            y = os.urandom(64)
            yBitsTotal=bin(int(hashlib.sha256(y).hexdigest(), scale))[2:]
    print(xBitsTotal)
    print(yBitsTotal)
    return( x, y )


hash_collision(20)