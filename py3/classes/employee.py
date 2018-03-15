# class variables

 
class Employee:
    num_of_employee = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_employee += 1

    def __str__(self):
        return '{} {} - {}'.format(self.first, self.last, self.pay)

    # def __repr__(self):
    #     return (f'Employee({self.first!r, self.second!r, self.pay!r})')


print(Employee.__dict__)
