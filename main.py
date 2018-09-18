#constants
initialPermutation = [2,6,3,1,4,8,5,7]
keyPermutation = [3,5,2,7,4,10,1,9,8,6]
KeyPermutation8Bit = [6,3,7,4,8,5,10,9]
inverseInitialPermutation = [4,1,3,5,7,2,8,6]

#utility methods from https://stackoverflow.com/questions/10237926/convert-string-to-list-of-bits-and-viceversa
def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def frombits(bits):
    chars = []
    for b in range(len(bits) // 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

def main():
    testString = "secret"
    testKey = [0,0,1,0,1,1,0,1,0,1]
    print(frombits(decryptExt(encryptExt(tobits(testString),testKey),testKey)))

def decrypt(bits,key):
    return bits

def decryptExt(bitArr,bitKey):
    decBits = []
    for i in range(0,len(bitArr),8):
        decBits += decrypt(bitArr[i:i+8],bitKey)
    return decBits

def encrypt(bits,key):
    #1. apply initial permutation
    encBits = [0,0,0,0,0,0,0,0]
    for i in range(len(encBits)):
        encBits[i] = bits[initialPermutation[i]-1]
    
    #2. split bits
    lbits = encBits[:4]
    rbits = encBits[4:]
    
    #3. apply key permutation
    keyBits = [0,0,0,0,0,0,0,0,0,0]
    for i in range(len(keyBits)):
        keyBits[i] = key[keyPermutation[i]-1]
    
    #4. split key
    lkey = key[:5]
    rkey = key[5:]
    
    #5. left shift key halves
    lkey.pop(0)
    lkey.append(0)
    rkey.pop(0)
    rkey.append(0)
    
    #6. recombine into 8 bit key k1
    k1 = [0,0,0,0,0,0,0,0]
    for i in range(len(k1)):
        k1[i] = lkey[KeyPermutation8Bit[i]-1] if KeyPermutation8Bit[i]-1 < 5 else rkey[KeyPermutation8Bit[i]-1-5]
    
    #7. call F with k1
    F(lbits,rbits,k1)
    
    #8. split k1
    lk1 = k1[:4]
    rk1 = k1[4:]
    
    #9. left shift k1 halves
    lk1.pop(0)
    lk1.append(0)
    rk1.pop(0)
    rk1.append(0)
    
    #10. recombine into 8 bit key k2
    k2 = lk1 + rk1
    
    #11. call F with k2
    F(lbits,rbits,k2)
    
    #12. apply inverse permutation
    bitsFinal = [0,0,0,0,0,0,0,0]
    for i in range(len(bitsFinal)):
        bitsFinal[i] = lbits[inverseInitialPermutation[i]-1] if inverseInitialPermutation[i]-1 < 4 else rbits[inverseInitialPermutation[i]-1-4]
    
    #done
    return bitsFinal

def encryptExt(bitArr,bitKey):
    encBits = []
    for i in range(0,len(bitArr),8):
        encBits += encrypt(bitArr[i:i+8],bitKey)
    return encBits

if __name__ == "__main__":
    main()