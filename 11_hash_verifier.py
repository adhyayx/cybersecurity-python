import hashlib
password = input("Enter Password : ")
hash_password = hashlib.sha256(password.encode()).hexdigest()
print(hash_password)
print("Hash length ",len(hash_password))