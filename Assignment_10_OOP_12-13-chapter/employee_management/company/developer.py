from company.employee import Employee

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def get_details(self):
        return f"{super().get_details()}, Language: {self.programming_language}"
