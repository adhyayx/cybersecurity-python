import hashlib

try:
    with open("notes.txt", "rb") as file:
        data = file.read()

    hash_value = hashlib.sha256(data).hexdigest()

    print("SHA256:", hash_value)

except FileNotFoundError:
    print("File not found!")