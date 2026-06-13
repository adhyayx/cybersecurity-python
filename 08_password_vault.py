website = input("Website Name : ")
username = input("Username : ")
password = input("Password : ")
file = open ("password.txt","a")

file.write("Website : " + website + "\n")
file.write("username : " + username + "\n")
file.write("password : " + password + "\n")
file.write("..................................")

file.close()
print ("Password saved successfilly")
