import hashlib

with open("notes.txt","rb") as file: 
    data = file.read()

current_hash = hashlib.sha256(data).hexdigest()

with open("old_hash.txt","r") as file:
    old_hash = file.read()

if current_hash == old_hash:
    print("File is safe ")
else:
    print("Warning! File modified")

if old_hash =="":
    with open("old_hash.txt","w") as file:
        file.write(current_hash)

    print("Current Hash Saved")    