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

    scale=16
    num_of_bits = 8
    xHash = hashlib.sha256()
    yHash = hashlib.sha256()
    xBitsTotal=""
    yBitsTotal=""
  
    for i in x:
        xHash.update(str(bin(i)[2:].zfill(num_of_bits)).encode('utf-8'))

    for m in y:
        yHash.update(str(bin(m)[2:].zfill(num_of_bits)).encode('utf-8'))
        
    for xNum in xHash.hexdigest():
        xBitsTotal=xBitsTotal+bin(int(xNum,scale))[2:].zfill(4)
        
    for yNum in yHash.hexdigest():
        yBitsTotal=yBitsTotal+bin(int(yNum,scale))[2:].zfill(4)
        
    match=False
    while(match==False):
        newK=len(xBitsTotal)-k
        yLastKbits=yBitsTotal[newK:len(yBitsTotal)]
        xLastKbits=xBitsTotal[newK:len(xBitsTotal)]
        # print("yLastKbits",yLastKbits)
        # print("xLastKbits",xLastKbits)
        if(yLastKbits==xLastKbits):
            match=True
        else:
            y = os.urandom(64)
            yBitsTotal=""
            
            for o in y:
                yHash = hashlib.sha256("0".encode('utf-8'))
                yHash.update(str(bin(o)[2:].zfill(num_of_bits)).encode('utf-8'))
            
            for yNumRep in yHash.hexdigest():
                yBitsTotal=yBitsTotal+bin(int(yNumRep,scale))[2:].zfill(4)
            
    x=xBitsTotal.encode('utf-8')
    y=yBitsTotal.encode('utf-8')
    return( x, y )

# hash_collision(5)


