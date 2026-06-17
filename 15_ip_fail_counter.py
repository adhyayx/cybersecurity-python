import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
password = ""
lenght = int (input("Enter Password Lenght : "))
for i in range (lenght):
    password = password + random.choice(characters)

print("Genrate Password : ", password)
print("Password Length : ",len(password))