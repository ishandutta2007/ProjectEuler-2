# -------------------------------------------------------- XOR decryption ------------------------------------------------------------- #
#                                                                                                                                       #
#       Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for          #
#       Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.                              #
#                                                                                                                                       #
#       A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value,           #
#       taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text,          #
#       restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.                                                    #
#                                                                                                                                       #
#       For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes.       #
#       The user would keep the encrypted message and the encryption key in different locations, and without both "halves",             #
#       it is impossible to decrypt the message.                                                                                        #
#                                                                                                                                       #
#       Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key.                 #
#       If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message.            #
#       The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.           #
#                                                                                                                                       #
#       Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt                   #
#       (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain       #
#       text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.          #
# ------------------------------------------------------------------------------------------------------------------------------------- #
import time
from collections import Counter
from itertools import product
            
def eu59(code):
    COMMON_LETTERS = [' ', 'e', 't', 'a', 'o', 'i']

    best_key = 0, 0
    for key in product([chr(ord('a') + i) for i in range(ord('z') - ord('a') + 1)], repeat = 3):
        new_code = [chr(code[i] ^ ord(key[i % 3])) for i in range(len(code))]

        freq = Counter(new_code)

        rank = sum([freq.most_common()[i][0] in COMMON_LETTERS for i in range(5)])
        if rank > 3:
            alnum_c = sum([1 for c in new_code if c.isalnum()])

            if alnum_c > best_key[1]:
                best_key = key, alnum_c

            
    msg = [chr(code[i] ^ ord(best_key[0][i % 3])) for i in range(len(code))]
    
    return sum([ord(c) for c in msg])

if __name__ == "__main__":
    startTime = time.clock()
    fsock = open("eu59.txt", "r")
    code = fsock.read()
    fsock.close()
    code = code.split(",")
    code = [int(n) for n in code]
    print (eu59(code))
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")


