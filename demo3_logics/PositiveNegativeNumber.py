# num=int(input("Enter the number:"))
# if num<0:
#     print("Number is negative",num)
# elif num>0:
#     print("Number is positive",num)
# else:
#     print("Number is Zero", num)



# num between 100 and 200.
# num=int(input("Enter the page number:"))
# if num>=100:
#     if num<=200:
#         print("Number is between 100 and 200.")
#     else:
#         print("Number is not between 100 and 200.")
# else:
#     print("Number is not between 100 and 200.")



# Mark Grading System.
mark=int(input("Enter the Marks:"))
if mark<=100 and mark>=0:
    if mark<=100 and mark>=90:
        print("Grade A")
    elif mark<=89 and mark>=80:
        print("Grade B")
    elif mark<=79 and mark>=60:
        print("Grade C")
    else:
        print("Grade F")
else:
    print("Enter mark between 0 to 100")