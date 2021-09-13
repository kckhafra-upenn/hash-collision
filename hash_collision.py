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
    x = os.urandom(64)
    y = os.urandom(64)
    scale = 16 ## equals to hexadecimal
    num_of_bits = 8
    xBitsTotal=bin(int(hashlib.sha256(x).hexdigest(), scale))[2:].zfill(num_of_bits)
    yBitsTotal=bin(int(hashlib.sha256(y).hexdigest(), scale))[2:].zfill(num_of_bits)

    
    match=False
    while(match==False):
        newK=len(xBitsTotal)-k
        yLastKbits=yBitsTotal[newK:len(yBitsTotal)]
        xLastKbits=xBitsTotal[newK:len(xBitsTotal)]
        if(yLastKbits==xLastKbits):
            match=True
        else:
            y = os.urandom(64)
            yBitsTotal=bin(int(hashlib.sha256(y).hexdigest(), scale))[2:].zfill(num_of_bits)
        
    x=xBitsTotal.encode('utf-8')
    y=yBitsTotal.encode('utf-8')
    return( x, y )

hash_collision(5)


