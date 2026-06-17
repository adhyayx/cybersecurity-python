massage = input("Enter Encrypted Massage :")
decrypted = ""

for letter in massage:
    decrypted = decrypted + chr(ord(letter) - 3)

print("Decrypted Massage : ",decrypted)