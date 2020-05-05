'''An assortment of functions useful in crypto'''

import base64


def xor(s1, s2):
    '''takes two strings of equal length and produces their XOR combination'''
    if len(s1) == len(s2):
        return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))
    return False


def xorstr(message, key):
    '''Encrypts message with key using XOR'''
    if len(key) < len(message):
        ekey = (key * (len(message)/len(key)+1))[:len(message)]
    else:
        ekey = key
    return xor(message, ekey)


def hamming_dist(s1, s2):
    '''Compute the Hamming distance of two strings

    Takes two strings s1, s2 and determines the number of bits where they
    differ. See https://en.wikipedia.org/wiki/Hamming_distance for additional
    background.
    '''
    s = xor(s1, s2)
    bits = 0

    if s:  # they are in fact the same length
        for c in s:
            bits += sum(bit == '1' for bit in bin(ord(c))[2:])
        return bits
    else:
        return False


def keysize(message):
    '''Calculate key size and distance for a string, return as tuple'''
    # `message` must be a base64-encoded string
    ciphertext = base64.b64decode(message)

    min_keysize, min_distance = 0, 1000

    for k in range(2, 256):
        # Hamming dist between block 1 and block 2
        d1 = float(hamming_dist(ciphertext[k*0:k*1], ciphertext[k*1:k*2])) / k
        # Hamming dist between block 2 and block 3
        d2 = float(hamming_dist(ciphertext[k*2:k*3], ciphertext[k*3:k*4])) / k
        # Hamming dist between block 3 and block 4
        d3 = float(hamming_dist(ciphertext[k*4:k*5], ciphertext[k*5:k*6])) / k
        distance = (d1+d2+d3)/3
        if distance < min_distance:
            min_keysize, min_distance = k, distance

    return min_keysize, min_distance
