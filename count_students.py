with open ("marks.txt","r") as f :
    for line in f:
        data = line.split()
        name = data[0]
        marks =data[1]
        print("Student",name ,"got",marks,"marks")