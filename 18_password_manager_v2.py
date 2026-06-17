import hashlib

website = input("Website : ")
username = input("Username : ")
password = input("Password : ")

hash_password = hashlib.sha256(password.encode()).hexdigest()
file = open("secure_password.txt","a")

file.write("website  : " + website + "\n")
file.write("username :" + username  + "\n")
file.write("password  : " + hash_password+ "\n")
file.write(" .............................\n")
file.close()
