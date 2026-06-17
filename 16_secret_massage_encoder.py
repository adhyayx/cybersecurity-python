massage = input("Enter a Massage : ")
encrypted = ""
for letter in massage:
    encrypted = encrypted + chr(ord(letter) + 3 )

print("Encrypted Massage : ", encrypted)