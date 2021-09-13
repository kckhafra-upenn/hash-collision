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
    # yBitsTotal=""
    # xBitsTotal=""
    # print("RANDOM1: ",x)
    # print("RANDOM2: ",y)
    scale = 16 ## equals to hexadecimal
    num_of_bits = 8
    xHash = hashlib.sha256()
    yHash = hashlib.sha256()
    xBitsTotal=""
    yBitsTotal=""
    # xBitsTotal=bin(int(hashlib.sha256(x).hexdigest(), scale))[2:].zfill(num_of_bits)
    # yBitsTotal=bin(int(hashlib.sha256(y).hexdigest(), scale))[2:].zfill(num_of_bits)
    for i in x:
        # print(str(bin(i)[2:].zfill(num_of_bits)).encode('utf-8'))
        xHash.update(str(bin(i)[2:].zfill(num_of_bits)).encode('utf-8'))
    for m in y:
        # print(str(bin(m)[2:].zfill(num_of_bits)).encode('utf-8'))
        yHash.update(str(bin(m)[2:].zfill(num_of_bits)).encode('utf-8'))
        # bin(int(hashlib.sha256(x[i]).hexdigest(), scale))[2:].zfill(num_of_bits)
        #     ybits = bin(y[i])[2:].zfill(8)
        #     xbits = bin(x[i])[2:].zfill(8)
    # print(xHash.hexdigest())
    for xNum in xHash.hexdigest():
        # print("J",bin(int(j,scale))[2:].zfill(4))
        xBitsTotal=xBitsTotal+bin(int(xNum,scale))[2:].zfill(4)
        
    for yNum in yHash.hexdigest():
        # print("L",bin(int(l,scale))[2:].zfill(4))
        yBitsTotal=yBitsTotal+bin(int(yNum,scale))[2:].zfill(4)
        # print("yBitsTotal",yBitsTotal)
    # # xBitsTotal=bin(int(xHash.hexdigest(), scale))[2:].zfill(num_of_bits)
    # # yBitsTotal=bin(int(hashlib.sha256(y).hexdigest(), scale))[2:].zfill(num_of_bits)
    print("X-BITS-TOTAL: ",xBitsTotal)
    print("Y-BITS-TOTAL: ",yBitsTotal)
    match=False
    while(match==False):
        # print("X-HASH",xBitsTotal)
        # print("Y-HASH",yBitsTotal)
        newK=len(xBitsTotal)-k
        yLastKbits=yBitsTotal[newK:len(yBitsTotal)]
        xLastKbits=xBitsTotal[newK:len(xBitsTotal)]
        print("yLastKbits",yLastKbits)
        print("xLastKbits",xLastKbits)
        if(yLastKbits==xLastKbits):
            match=True
        else:
            y = os.urandom(64)
            yBitsTotal=""
            print("REPeat-Y: ",y)
            for o in y:
                yHash = hashlib.sha256("0".encode('utf-8'))
                yHash.update(str(bin(o)[2:].zfill(num_of_bits)).encode('utf-8'))
            print("YYY-HASH: ",yHash.hexdigest())
            for yNumRep in yHash.hexdigest():
                # print("L",bin(int(l,scale))[2:].zfill(4))
                yBitsTotal=yBitsTotal+bin(int(yNumRep,scale))[2:].zfill(4)
            print("YYY-TOTAL: ",yBitsTotal) 
        # print("yRepeat",yBitsTotal)
        print("MATCH",match)
        
        
    # print("B",bin(3)[2:].zfill(8))
    # print("Y",y)
    # for i in range(k,len(x)):
    #     m.update(x)
    
    # print("HASH",hashlib.sha256(y).hexdigest())
        # hashlib.sha256(x[i].encode('utf-8')).hexdigest()
    # if()
    # }
    # byte_str = str.encode('utf-8')
    # print("Final-X",xBitsTotal.encode('utf-8'))
    # print("Final-Y",yBitsTotal.encode('utf-8'))
    x=xBitsTotal.encode('utf-8')
    y=yBitsTotal.encode('utf-8')
    return( x, y )

hash_collision(15)


