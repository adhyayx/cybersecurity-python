# password checker how your password strong is 
print ("password checker how your password strong is \n")

password = input("Enter Your Password : ")

if len(password) < 5:
    print("Weak Password")

elif len(password) <= 7:
    print("Medium Password")

elif len(password) <= 11:
    print("Strong Password")

else:
    print("Very Strong Password")

