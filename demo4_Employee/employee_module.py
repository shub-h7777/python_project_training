class Employee:
    company_name = None  # static variable or class variable - already loaded in memory
    company_location = None

    def __init__(self):
        self.emp_id = None  # non-static variable or instance variable - not loaded in memory
        self.emp_name = None
        self.emp_salary = None
        self.emp_performance = None
