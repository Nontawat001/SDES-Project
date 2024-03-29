

FIXED_IP = [2, 6, 3, 1, 4, 8, 5, 7]
FIXED_EP = [4, 1, 2, 3, 2, 3, 4, 1]
FIXED_IP_INVERSE = [4, 1, 3, 5, 7, 2, 8, 6]
FIXED_P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
FIXED_P8 = [6, 3, 7, 4, 8, 5, 10, 9]
FIXED_P4 = [2, 4, 3, 1]

S0 = [[1, 0, 3, 2],
      [3, 2, 1, 0],
      [0, 2, 1, 3],
      [3, 1, 3, 2]]

S1 = [[0, 1, 2, 3],
      [2, 0, 1, 3],
      [3, 0, 1, 0],
      [2, 1, 0, 3]]



def permutate(original, fixed_key):
    new = ''
    for i in fixed_key:
        new += original[i - 1]
    return new


def left_half(bits):
    return bits[:len(bits)//2]


def right_half(bits):
    return bits[len(bits)//2:]


def shift(bits):
    rotated_left_half = left_half(bits)[1:] + left_half(bits)[0]
    rotated_right_half = right_half(bits)[1:] + right_half(bits)[0]
    return rotated_left_half + rotated_right_half


def key1(KEY):
    return permutate(shift(permutate(KEY, FIXED_P10)), FIXED_P8)


def key2(KEY):
    return permutate(shift(shift(shift(permutate(KEY, FIXED_P10)))), FIXED_P8)


def xor(bits, key):
    new = ''
    for bit, key_bit in zip(bits, key):
        new += str(((int(bit) + int(key_bit)) % 2))
    return new


def lookup_in_sbox(bits, sbox):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return '{0:02b}'.format(sbox[row][col])


def f_k(bits, key):
    L = left_half(bits)
    R = right_half(bits)
    bits = permutate(R, FIXED_EP)
    bits = xor(bits, key)
    bits = lookup_in_sbox(left_half(bits), S0) + lookup_in_sbox(right_half(bits), S1)
    bits = permutate(bits, FIXED_P4)
    return xor(bits, L)



def decrypt(cipher_text,key):
    bits = permutate(cipher_text, FIXED_IP)
    temp = f_k(bits, key2(key))
    bits = right_half(bits) + temp
    bits = f_k(bits, key1(key))
    return permutate(bits + temp, FIXED_IP_INVERSE)

cipher_text = [0b10011101,0b1110011,0b11001101,0b1100011,0b11000,0b11001101,0b1100011,0b110,0b11000011,0b1100011,0b110,0b11000,0b11000011,0b11001101,0b11010011,0b1001000,0b11010011,0b10011101,0b11000011,0b10010110,0b11010011,0b110,0b11001101,0b1001000,0b1100011,0b1110011,0b11000011,0b11000,0b110,0b1001000,0b1100011,0b1001000,0b11000011,0b11001101,0b10010110,0b11010011,0b1110011,0b11001101,0b11000,0b10011101,0b110,0b10011101,0b110,0b11000011,0b1001000,0b11000,0b11000,0b1110011,0b110,0b10011101,0b11000011,0b11000011,0b10011101,0b10011101,0b10011101,0b10011101,0b10010110,0b110,0b11010011,0b1001000,0b11000011,0b11000011,0b1110011,0b10011101,0b10010110,0b10011101,0b1110011,0b1110011,0b10011101,0b10011101,0b110,0b11001101,0b11000,0b11000011,0b1001000,0b1100011, ]
student_id = '590610628'
check_id = student_id.encode('utf-8')
check = False
    
for i in range(1024):
    cipherString = []
    for  j in range(len(cipher_text)):
        key = "{0:010b}".format(i)
        cipherString.append(int(decrypt(str('{0:08b}'.format(cipher_text[j])),key),2))
        
    if cipherString[0] == check_id[0] and cipherString[1] == check_id[1] and cipherString[2] == check_id[2] and cipherString[3] == check_id[3] and cipherString[4] == check_id[4] and cipherString[5] == check_id[5]  and cipherString[6] == check_id[6] and cipherString[7] == check_id[7] and cipherString[8] == check_id[8]:
        check = True
    if check == True:
        break
for i in range(len(cipherString)):
    cipherString[i] = cipherString[i] - 48
print(key)
print(cipherString)
           
        
            


