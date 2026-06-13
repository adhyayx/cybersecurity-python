total_marks =0
student_count = 0

with open ("marks.txt","r") as f:
    for line in f:
        data = line.split()
        marks = int(data[1])
        total_marks = total_marks +marks
        student_count = student_count +1
average = total_marks/student_count
print("Total Marks:", total_marks)
print("Students:", student_count)
print("Average:", average)