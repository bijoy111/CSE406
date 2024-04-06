from BitVector import *
import time

Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

def xor(array1: list, array2: list) -> list:
    # array1 and array2 are list of hex values
    return [hex(int(a, 16) ^ int(b, 16)) for a, b in zip(array1, array2)]

#translateIntohex function take a string as input and return the corresponding hex value's list
def translateIntohex(string: str) -> list: 
    return list(map(lambda c: hex(ord(c)), string))

#stringToword function first convert a string into hex values and then divide them into group of word
def stringToword(string: str) -> list:
    key = translateIntohex(string)
    tot_word = 4
    matrix = []
    for i in range(0, len(key), 4):
        matrix.append(key[i:i + 4])
    while len(matrix) < tot_word:
        matrix.append(['0x00'] * 4)
    return matrix[:tot_word]

#roundConstant function returns the round constant for the given round
def roundConstant(round: int) -> int:
    if round == 1:
        return 0x01 
    prevRoundConst = 0x01
    for _ in range(2, round + 1):
        prevRoundConst = (prevRoundConst << 1) ^ (0x11b & -(prevRoundConst >> 7))  # here a bitwise left shift of the prevRoundConst variable by 1 position is done followed by a XOR operation with the result of bitwise AND between the constant 0x11b and the arithmetic right shift and bitwise negation of prevRoundConst's 8th bit
    return prevRoundConst

def g(key: list, round: int) -> list:
    rotated_key = key[1:] + key[:1] # rotates the key by 1 byte
    sbox_applied = [hex(Sbox[int(x, 16)]) for x in rotated_key] # applies the sbox to each byte
    sbox_applied[0] = hex(int(sbox_applied[0], 16) ^ roundConstant(round)) # add the round constant
    return sbox_applied

# convertion of the given key to 128 bits
def checkedKeysize(key: str) -> str:
    keysize = 16  # assuming a block size is 128 bits or 16 bytes
    if len(key) < keysize:
        return key.ljust(keysize, '0')
    elif len(key) > keysize:
        return key[:keysize]
    return key

# generates the next round's key from the previous round's key
def generateRoundKey(round: int, previouskey: list) -> list:
    w = [xor(previouskey[0], g(previouskey[3], round))]
    for i in range(1, len(previouskey)):
        currentkey = xor(w[i - 1], previouskey[i])
        w.append(currentkey)
    return w

# generates all round keys from the initial key
def allRoundkeys(key: str) -> list:
    key = checkedKeysize(key) # checkedKeysize make the key 128 bit
    keys = [stringToword(key)] # stringToword function make the text version key into hex and also divided the hex value into matrix
    for i in range(1, 11):
        keys.append(generateRoundKey(i, keys[i - 1]))
    return keys

def stateMatrix(string: str) -> list:
    string = checkedKeysize(string)
    matrix = stringToword(string)
    # Transpose the matrix for column major order
    transposed_matrix = []
    for i in range(len(matrix[0])):
        column = [row[i] for row in matrix]
        transposed_matrix.append(column)
    return transposed_matrix

# addRoundKey function add given round key with the given stateMatrix where stateMatrix is in column major order and roundKey is in row major order
def addRoundKey(stateMatrix: list, roundKey: list) -> list:
    roundKey = [list(x) for x in zip(*roundKey)]  # Transposing the round key
    updatedstateMatrix = []
    for i in range(len(stateMatrix)):
        updatedstateMatrix.append(xor(stateMatrix[i], roundKey[i]))
    return updatedstateMatrix

# Sbox is applied to each byte in the stateMatrix to get the updatestateMatrix
def substitutionBytes(stateMatrix: list) -> list:
    updatedstateMatrix = []
    for row in stateMatrix:
        new_row = [hex(Sbox[int(x, 16)]) for x in row]
        updatedstateMatrix.append(new_row)
    return updatedstateMatrix

def shiftRow(stateMat: list):
    updatedstateMatrix = []
    for i, row in enumerate(stateMat):
        new_row = row[i:] + row[:i]  # Circular shift left by i positions
        updatedstateMatrix.append(new_row)
    return updatedstateMatrix

def mixColumn(stateMatrix: list) -> list:
    Mixer = [
        [0x02, 0x03, 0x01, 0x01],
        [0x01, 0x02, 0x03, 0x01],
        [0x01, 0x01, 0x02, 0x03],
        [0x03, 0x01, 0x01, 0x02]
    ]
    updatedstateMatrix = []
    for i in range(len(Mixer)):
        row = []
        for j in range(len(stateMatrix[0])):
            dotProd = 0
            for k in range(len(Mixer)):
                bv1 = Mixer[i][k]
                bv2 = int(stateMatrix[k][j], 16)
                dotProd ^= AESModulusMultiply(bv1, bv2)
            row.append(hex(dotProd))
        updatedstateMatrix.append(row)
    return updatedstateMatrix

# AESModulusMultiply function multiply two values according to AES modulus
def AESModulusMultiply(a, b):
    p = 0
    for _ in range(8):
        if b & 1:
            p ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        a &= 0xFF
        if hi_bit_set:
            a ^= 0x1B
        b >>= 1
    return p

def aesEncryption(plainText: str, keys: list) -> str:
    blocksize = 16  # assuming a block size is 128 bit or 16 byte
    if len(plainText) != blocksize:
        plainText=plainText.ljust(16, '0')
    statematrix = stateMatrix(plainText)
    statematrix = addRoundKey(statematrix, keys[0])
    #print(statematrix)
    for i in range(1, 10):
        statematrix = substitutionBytes(statematrix)
        statematrix = shiftRow(statematrix)
        statematrix = mixColumn(statematrix)
        statematrix = addRoundKey(statematrix, keys[i])
        #print(statematrix)
    statematrix = substitutionBytes(statematrix)
    statematrix = shiftRow(statematrix)
    statematrix = addRoundKey(statematrix, keys[10])
    cipherText=''
    for col in range(len(statematrix[0])):
        for row in range(len(statematrix)):
            cell = statematrix[row][col]
            cipherText += format(int(cell, 16), '02x')
    return cipherText

def invStateMatrix(cipherText: str) -> list:
    cipherText = cipherText[:128].ljust(128, '0') # Pad or truncate the cipher text to 128 bits
    matrix = [cipherText[i:i + 2] for i in range(0, len(cipherText), 2)]  # Split the cipher text into pairs of characters
    result_matrix = []
    for col in range(4):
        result_matrix.append(matrix[col * 4: col * 4 + 4])
    # Transpose the matrix to make it column major order
    transposed_matrix = []
    for col in range(4):
        transposed_matrix.append([result_matrix[row][col] for row in range(4)])
    return transposed_matrix

def invShiftRow(stateMatrix: list):
    tot_word = 4
    updatedstateMatrix = []
    for i in range(tot_word):
        row = stateMatrix[i]
        new_row = row[-i:] + row[:-i]  # Perform circular shift to the right by 'i' positions
        updatedstateMatrix.append(new_row)
    return updatedstateMatrix

#invSbox is applied to each byte in the stateMatrix
def invSubBytes(stateMatrix: list) -> list:
    tot_word = 4
    updatedstateMatrix = []
    for i in range(tot_word):
        new_row = []
        for x in stateMatrix[i]:
            decimal_value = int(x, 16)  # Convert hex to decimal
            inv_sbox_value = InvSbox[decimal_value]  # Get value from the inverse Sbox
            new_row.append(hex(inv_sbox_value))  # Convert the value back to hex and append
        updatedstateMatrix.append(new_row)
    return updatedstateMatrix

def invMixColumn(stateMatrix: list) -> list:
    InvMixer = [
        [0x0e, 0x0b, 0x0d, 0x09],
        [0x09, 0x0e, 0x0b, 0x0d],
        [0x0d, 0x09, 0x0e, 0x0b],
        [0x0b, 0x0d, 0x09, 0x0e]
    ]
    updatedstateMatrix = []
    for i in range(len(InvMixer)):
        row = []
        for j in range(len(stateMatrix[0])):
            dotProd = 0
            for k in range(len(InvMixer)):
                bv1 = InvMixer[i][k]
                bv2 = int(stateMatrix[k][j], 16)
                dotProd ^= AESModulusMultiply(bv1, bv2)
            row.append(hex(dotProd))
        updatedstateMatrix.append(row)
    return updatedstateMatrix

def aesDecryption(cipherText: str, keys: list) -> str:
  statematrix = invStateMatrix(cipherText)
  statematrix = addRoundKey(statematrix, keys[10])
  for i in range(9, 0, -1):
    statematrix = invShiftRow(statematrix)
    statematrix = invSubBytes(statematrix)
    statematrix = addRoundKey(statematrix, keys[i])
    statematrix = invMixColumn(statematrix)
  statematrix = invShiftRow(statematrix)
  statematrix = invSubBytes(statematrix)
  statematrix = addRoundKey(statematrix, keys[0])
  hextext = ''
  tot_word = 4
  for i in range(tot_word):
    for j in range(4):
      tmp = statematrix[j][i][2:]
      if len(tmp) == 1:
        tmp = "0" + tmp
      hextext += tmp
  plainText = bytearray.fromhex(hextext).decode() # hex to ascii
  return plainText

def divide_into_substrings(text):
    return [text[i:i+16] for i in range(0, len(text), 16)]

def divide_into_subHex(text):
    return [text[i:i+32] for i in range(0, len(text), 32)]

def xor_strings(s,t):
    """xor two strings together"""
    return "".join(chr(ord(a)^ord(b)) for a,b in zip(s,t))

def main():
    Key="BUET CSE19 Batch"
    Key=str(Key)
    print("Key:")
    print("In ASCII: " + Key)
    print("In HEX: " , end = "")
    hex_key=translateIntohex(Key)
    for i, item in enumerate(hex_key):
        print(item[2:], end=" ")  # Print the current item
        # Check if the next element exists and if the current index is not the last one
        if (i + 1) % 2 == 0 and i != len(hex_key) - 1:
            print("", end="")  # Print a space after every two elements
    print()
    print()
    KS_1=time.time()
    keys=allRoundkeys(Key)
    KS_2=time.time()
    Plaintext="Never Gonna Give you up"
    Plaintext=str(Plaintext)
    print("Plain Text:")
    print("In ASCII: " + Plaintext)
    print("In HEX: " , end = "")
    Plaintexts=divide_into_substrings(Plaintext)
    hex_text=translateIntohex(Plaintext)
    for i, item in enumerate(hex_text):
        print(item[2:], end=" ")
        if (i + 1) % 2 == 0 and i != len(hex_text) - 1:
            print("", end="")
    print()
    print()
    ET_1=time.time()
    IV = "0" * 16
    cipherText=''
    for Plaintext in Plaintexts:
        Plaintext=Plaintext.ljust(16)      
        Plaintext=xor_strings(Plaintext,IV)      
        ciph=aesEncryption(Plaintext,keys)
        cipherText+=ciph
        IV=ciph
    ET_2=time.time()
    #print(cipherText)
    hex_ciph=translateIntohex(cipherText)
    print("Ciphered Text:")
    print("In HEX: " , end = "")
    for i, item in enumerate(hex_ciph):
        print(item[2:], end=" ")
        if (i + 1) % 2 == 0 and i != len(hex_ciph) - 1:
            print("", end="")
    print()
    print("In ASCII: " , end = "")
    ascii_ciph = bytes.fromhex(str(cipherText)).decode('ascii', errors='ignore')
    print(ascii_ciph)
    DT_1=time.time()
    plaintext=''
    IV = "0" * 16 
    cipherTexts=divide_into_subHex(cipherText)
    for cipherText in cipherTexts:
        ciph=aesDecryption(cipherText,keys)
        ciph=xor_strings(ciph,IV)
        IV=cipherText
        plaintext+=ciph
    DT_2=time.time()
    print()
    print("Deciphered Text:")
    hex_deciph=translateIntohex(plaintext)
    print("In HEX: " , end = "")
    for i, item in enumerate(hex_deciph):
        print(item[2:], end=" ")
        if (i + 1) % 2 == 0 and i != len(hex_deciph) - 1:
            print("", end="")
    print()
    print("In ASCII: " , end = "")
    print(plaintext)
    print("Execution Time Details:")
    print("Key Schedule Time: ",end="")
    print((KS_2-KS_1)*1000)
    print("Encryption Time: ",end="")
    print((ET_2-ET_1)*1000)
    print("Decryption Time: ",end="")
    print((DT_2-DT_1)*1000)

#main()