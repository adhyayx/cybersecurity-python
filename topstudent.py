highest_marks = 0
topstudent =""
with open ("marks.txt","r") as f:
    for line in f: 
        data = line.split ()
        name =data[0]
        marks =int(data[1])

        if marks > highest_marks :
            highest_marks=marks
            topstudent = name 

print("Top student :",topstudent)
print("Marks",highest_marks)