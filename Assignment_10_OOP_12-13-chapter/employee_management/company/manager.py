from company.employee import Employee

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return f"{super().get_details()}, Team Size: {self.team_size}"
