from company import Employee, Manager, Developer

def main():
    emp = Employee("Alice", 50000)
    mgr = Manager("Bob", 90000, 5)
    dev = Developer("Charlie", 75000, "Python")

    employees = [emp, mgr, dev]

    for e in employees:
        print(e.get_details())

if __name__ == "__main__":
    main()
