from student_package.student_module import Student

Student.school_name="Global School"
Student.school_address="Pune"


Student1= Student(101,"Shubham", "shubham@gmail.com", 88.2)
print(Student1.student_name)


student2=Student(student_name="Peter")
print(student2.student_name)


print(Student1.get_name_with_percentage)

print(Student.get_school_details)