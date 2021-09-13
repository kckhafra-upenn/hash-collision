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
    # xHash = hashlib.sha256()
    # yHash = hashlib.sha256()
    scale = 16 ## equals to hexadecimal
    num_of_bits = 8
    xBitsTotal=""
    yBitsTotal=""
    xHash=hashlib.sha256(x).hexdigest()
    yHash=hashlib.sha256(y).hexdigest()
    # for i in x:
    #     xHash.update(str(bin(i)[2:].zfill(num_of_bits)).encode('utf-8'))

    # for m in y:
    #     yHash.update(str(bin(m)[2:].zfill(num_of_bits)).encode('utf-8'))
    
    # for xNum in xHash:
    #     xBitsTotal=xBitsTotal+bin(int(xNum,scale))[2:].zfill(4)
    #     print(xBitsTotal)
    #     # print(xNum)
        
    # for yNum in yHash:
    #     yBitsTotal=yBitsTotal+bin(int(yNum,scale))[2:].zfill(4)
        # print(yBitsTotal)

    # xBitsTotal=bin(int(xHash.hexdigest(), scale))[2:]
    # yBitsTotal=bin(int(yHash.hexdigest(), scale))[2:]
    
    # print("X: ",xBitsTotal)
    # print("Y: ",yBitsTotal)
    xBitsTotal=bin(int(hashlib.sha256(x).hexdigest(), scale))[2:]
    yBitsTotal=bin(int(hashlib.sha256(y).hexdigest(), scale))[2:]
    
    match=False
    while(match==False):
        newK=len(xBitsTotal)-k
        yLastKbits=yBitsTotal[newK:len(yBitsTotal)]
        xLastKbits=xBitsTotal[newK:len(xBitsTotal)]
        # print("YLAST: ",yLastKbits)
        # print("XLAST: ",xLastKbits)
        if(yLastKbits==xLastKbits):
            match=True
        else:
            y = os.urandom(64)
            yBitsTotal=bin(int(hashlib.sha256(y).hexdigest(), scale))[2:]
            
            
            
        
    # x=xBitsTotal.encode('utf-8')
    # y=yBitsTotal.encode('utf-8')
    # print("X: ",x)
    # print("Y: ",y)
    return( x, y )


# hash_collision(5)