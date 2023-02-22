class Student():
    school_name = None
    school_address = None

    def __init__(self, student_id=None, student_name=None, student_mailid=None, student_percentage=None):
        self.student_id = student_id
        self.student_name = student_name
        self.student_mailid = student_mailid
        self.student_percentage = student_percentage

    @property
    def get_student_name(self):
        return self.student_name

    @property   #Decorator
    def get_name_with_percentage(self):
        return "Hi, " + self.student_name + "- Your Percentage is " + str(self.student_percentage)

    # on calling Class-Student Static method will be loaded in memory.
    @staticmethod  # Decorator
    def get_school_details():
        return Student.school_name + " is located at " + Student.school_address
