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
    yBitsTotal=""
    xBitsTotal=""
    # print("RANDOM1: ",x)
    print("RANDOM2: ",y)
    match=False
    while(match==False):
        yBitsTotal=""
        xBitsTotal=""
        # print("YY",y)
        for i in range(0,len(y)):
            ybits = bin(y[i])[2:].zfill(8)
            xbits = bin(x[i])[2:].zfill(8)
            yBitsTotal = yBitsTotal+ybits
            xBitsTotal = xBitsTotal+xbits
            # print(i,bits)
        #y=y[k:len(x)]
        # print("XBITS: ",xBitsTotal)
        # print("YBITS: ",yBitsTotal)
        newK=k*8
        yLastKbits=yBitsTotal[newK:len(yBitsTotal)]
        xLastKbits=xBitsTotal[newK:len(xBitsTotal)]
        print("LAST-Y: ",yLastKbits)
        print("LAST-X: ",xLastKbits)
        # print("COND",yLastKbits==xLastKbits)
        if(yLastKbits==xLastKbits):
            match=True
        else:
            y = os.urandom(64)
        # print("y",y)
        # print("MATCH",match)
        
        
    # print("B",bin(3)[2:].zfill(8))
    # print("Y",y)
    # for i in range(k,len(x)):
    #     m.update(x)
    print("HASH",hashlib.sha256(x).hexdigest())
    print("HASH",hashlib.sha256(y).hexdigest())
    # print("HASH",hashlib.sha256(y).hexdigest())
        # hashlib.sha256(x[i].encode('utf-8')).hexdigest()
    # if()
    # }
    # byte_str = str.encode('utf-8')
    print("Final-X",xBitsTotal.encode('utf-8'))
    print("Final-Y",yBitsTotal.encode('utf-8'))
    x=xBitsTotal.encode('utf-8')
    y=yBitsTotal.encode('utf-8')
    return( x, y )




