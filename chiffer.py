key = 0
letters = []
crypt = []
meny = 0
while meny != 3:
    print("1. Kryptera")
    print("2. Dekryptera")
    print("3. Avsluta")
    meny = int(input("Vad vill du göra? "))   
    if meny == 1:
        word = input("Vad vill du kryptera? ")
        key = input("vad vill du ha för nyckel? ")
        for letter in word:
            letters.append(ord(letter) + key)
        print(letters)
    if meny == 2:
        for l in letters:
            crypt.append(chr(l - key))
        print(crypt)
        break
