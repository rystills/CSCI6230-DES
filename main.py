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
    print(frombits(decryptExt(encryptExt(tobits(testString)))))

def decrypt(bits):
    return bits

def decryptExt(bitArr):
    decBits = []
    for i in range(0,len(bitArr),8):
        decBits += decrypt(bitArr[i:i+8])
    return decBits

def encrypt(bits):
    return bits

def encryptExt(bitArr):
    encBits = []
    for i in range(0,len(bitArr),8):
        encBits += encrypt(bitArr[i:i+8])
    return encBits

if __name__ == "__main__":
    main()