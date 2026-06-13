import hashlib

password = input("Enter Password : ")
hash_password = hashlib.sha256(password.encode()).hexdigest()
file = open("hashed_password.txt","a")

file.write("Password : " + hash_password +"\n")
file.close()