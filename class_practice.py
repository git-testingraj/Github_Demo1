'''class wish:
    def temp(self):
        return 'Hi'

obj = wish()
r = obj.temp()
print(r)'''

'''class employee:
    pass

emp_1 = employee()
emp_2 = employee()

emp_1.first = 'Rajendra'
emp_1.last = 'Patle'
emp_1.email = 'Rajpatle@gmail.com'

print(emp_1.email)'''

'''
class Employee:
    Company_name = 'Infosys'
    def __init__(self,name,age,add):
        self.n = name
        self.a = age
        self.ad = add
    def show(self):
        print('Name is :',self.n)
        print('Age is:',self.a)
        print('Address is:',self.ad)
        print(Employee.Company_name)

s1 = Employee('Rajendar',30,'Nagpur')
#s1.show()
print('\n')
s2 = Employee('Nogit',31,'Katangi')
s2.show()'''



class cal:
    def __init__(self,total_amt):
        self.t = total_amt
    def sub(self,m1):
        global current_amt
        self.m1 = m1
        current_amt = self.t-self.m1
        return f'current amount {current_amt}'

    def add(self,m2):
        self.m2 = m2
        add_amt = current_amt+self.m2
        return f'current amount add {add_amt}'

var = cal(1000)
print(var.sub(350))
print(var.add(600))