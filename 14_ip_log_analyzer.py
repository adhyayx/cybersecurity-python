success = 0
failed = 0
failed_ip = ""

file = open("ip_logs.txt", "r")

for line in file:

    line = line.strip()
    
    parts = line.split()

    ip = parts[0]

    status = parts[1]

    if status == "SUCCESS":
        success = success + 1 
        
    elif status == "FAILED":
        failed = failed + 1
        failed_ip = ip 

file.close()

print("Total success : ",success)
print("Total failed : ",failed)

if failed >= 3:
    print("Possible attacker IP",failed_ip)





