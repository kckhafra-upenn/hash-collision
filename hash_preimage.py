import hashlib
import os

def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return
    nonce = b'\x00'
    x = os.urandom(64)
    scale=16
    length = len(target_string)
    xBitsTotal=bin(int(hashlib.sha256(x).hexdigest(), scale))[2:]
    # targetStringBits=bin(int(hashlib.sha256(target_string.encode("utf-8")).hexdigest(), scale))[2:]
    # print("Target: ",target_string)
    # print("xBitsTotal: ",xBitsTotal)
    # print("Length: ",length)
    # print("Length2: ",len(xBitsTotal))
    match=False
    newLen=len(xBitsTotal)-length
    # print(newLen)
    while(match==False):
        xLastKbits=xBitsTotal[newLen:len(xBitsTotal)]

        if(target_string==xLastKbits):
            match=True
        else:
            x = os.urandom(64)
            xBitsTotal=bin(int(hashlib.sha256(x).hexdigest(), scale))[2:]
    print(x)
    return(x)

# hash_preimage("01011100")