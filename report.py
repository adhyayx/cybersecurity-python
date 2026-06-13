highest_marks =0
top_student = ""
with open ("marks.txt","r") as f:
    for line in f:
        data = line.split()
        name = data[0]
        marks = int(data[1])

        if marks > highest_marks:
            highest_marks = marks
            top_student = name

with open ("report.txt","w") as f:
    f.write("Top student : " + top_student+"\n")
    f.write ("Highest Marks :" + str(highest_marks))