success = 0
failed =0
file = open("login_logs.txt","r")
for line in file:
    line = line.strip()
    if line == "SUCCESS":
        success = success +1
    elif line == "FAILED":
        failed =failed +1 

file.close()

if failed >= 3:
    print("Possible brute force attack detected")
else:
    print("No brute force attack detected")