correct_username = "kartik"
correct_password = "1234"

for attempt in range(3):
    
    username = input("username: ")
    password = input("password : ")
    remaining = 3-(attempt +1)
    if username == correct_username and password == correct_password:
        print("Welcome ",correct_username)
        break
    else:
        print("Invalid Credentials")
        if remaining > 0:

            print("Remaining attempts: ",remaining)

else:
    print("Account Locked")
