class Employee:
    Employee_Count=0
    avg_salary=0
    def __init__(self,name,family,salary,department):
        self.name=name
        self.family=family
        self.salary=salary
        self.department=department
        Employee.Employee_Count+=1
        Employee.avg_salary+=salary

    def Avg_Sal(self):
        avg=Employee.avg_salary/Employee.Employee_Count
        return avg
class FullTimeEmployee(Employee):
    def __init__(self,First_Name,LastName):
        self.First_Name=First_Name
        self.LastName=LastName

P1=FullTimeEmployee("vamshi","Jakkula")
s1=Employee("vamshi","jakkula",36,"manager")
s2=Employee("vamshi","jakkula",38,"java")
s3=Employee("vamshi","jakkula",34,"IMSDB")

print(s3.Avg_Sal())
print(Employee.Employee_Count)
print(Employee.avg_salary)




