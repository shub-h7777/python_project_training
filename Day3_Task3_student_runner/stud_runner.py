from Day3_Task3_student_package.student_module import Student

#static variable value.
Student.school_name = "Global School"
Student.school_address = "Chennai"


# instance for the student
stu1 = Student(1001, "jack", "jack@gmail.com", 45.2)
stu2 = Student(1002, "peter", "peter@gmail.com", 85.2)
stu3 = Student(1003, "mark", "mark@gmail.com", 56.5)

#print mail id
print(stu1.student_mailid)
print(stu2.student_mailid)
print(stu3.student_mailid)

#assign the stu1 to stu2
stu2=stu1
print(stu1.student_mailid)
print(stu2.student_mailid)
print(stu3.student_mailid)



#not the Task but it was given during training.
Student1 = Student(101, "Shubham", "shubham@gmail.com", 88.2)
print(Student1.student_name)
student2 = Student(student_name="Peter")
print(student2.student_name)
print(Student1.get_name_with_percentage)
print(Student.get_school_details)
