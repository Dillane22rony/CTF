cipher_text = input("Enter the cipher text:")


def substitution(word, i):
    word = word.lower()
    word = list(word)
    decrypt = ""
    for j in word:
        if j.isalpha():
            if (ord(j) - i) < 97:
                l = ord(j) - i + 26
            else:
                l = ord(j) - i
            decrypt = decrypt + chr(l)
        else:
            decrypt = decrypt + j
    return decrypt


def force(word):
    texts = []
    for i in range(1, 26):
        texts.append(substitution(word, i))
    return texts


print("The possibilities are :")
for i, possibility in enumerate(force(cipher_text)):
    print("key " + str(i+1) + " " + str(possibility))
