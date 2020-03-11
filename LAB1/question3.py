class Flight:
    def __init__(self,flight_name, flight_number):
        self.flight_name = flight_name
        self.flight_number = flight_number

    def flight_display(self):
        print('flight_name: ', self.flight_name)
        print('flight_number: ', self.flight_number)

class Employee:
    def __init__(self, emp_id, emp_name, emp_age, emp_gender):
        self.__emp_id = emp_id  # private variable
        self.emp_name = emp_name
        self.emp_age = emp_age
        self.emp_gender =  emp_gender
    def emp_display(self):
        print('employee_id: ', self.__emp_id)
        print("employee_name: ", self.emp_name)
        print('employee_age: ',self.emp_age)
        print('employee_gender: ', self.emp_gender)

class Passenger:
    def __init__(self):
        Passenger.__passport_number = input("Enter the passport number of passenger: ") #private variable;since it has to be unique
        Passenger.first_name = input('Enter the first name of passenger: ')
        Passenger.last_name=input('Enter the Last name of passenger')
        Passenger.age = int(input('Enter the age of passenger: '))#should be an integer
        Passenger.class_type = input('Select B for Business class or E for Economy class: ')

class Luggage():
    Baggage_Fare = 0 #initially kept 0
    def __init__(self, Total_Checkin_Bags):
        self.Total_Checkin_Bags = Total_Checkin_Bags
        if Total_Checkin_Bags > 2 :
            Luggage.Baggage_Fare = (Total_Checkin_Bags-2)*60
        else:
            pass

class Fare(Luggage): #inheritance
    offline = 150
    online = 180
    total_fare=0
    def __init__(self):
        super().__init__(int(input('enter the number of check-in bags: '))) #super call
        x = input('bought ticket through online or offline: ')
        if x == 'online':
            Fare.total_fare = Fare.online + Luggage.Baggage_Fare
        elif x == 'offline':
            Fare.total_fare = Fare.offline + Luggage.Baggage_Fare
        else:
            pass

class Ticket(Passenger, Fare): #inheritance
    def __init__(self):
        print("Passenger first name:",Passenger.first_name)
        if Passenger.class_type == "B":
            str = "business"
            Fare.total_fare+=80
        else:
            str = "economy"
            pass

        print("Passenger class type:",str)
        print("Total fare:",Fare.total_fare)



f1=Flight('AA','AA134JV')
f1.flight_display()

emp1 = Employee('779769','vamshi','jakkula',24)
emp1.emp_display()

p1 = Passenger()

fare1=Fare()

t= Ticket()