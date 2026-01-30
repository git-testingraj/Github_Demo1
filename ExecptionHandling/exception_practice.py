'''a = 10
b= 0
try:
    c = a/b
    print(c)
except ZeroDivisionError as msg:
    print('please enter valid denominator:', msg)'''

#wap during read a file and it is not available in the directory
'''try:
    with open(r'C:\Pycharm_Projects\pythonProject\FileHandling\emp_email_copy.csv','r') as file_read:
        data = file_read.read()
        print(data)
except FileNotFoundError as msg:
    print('Error:',msg)'''

#example 2:
a = 10
b = 5
try:
    c = a/b
    print(c)
    with open('f.txt','r') as fp:
        data = fp.read()
        print(data)
except ZeroDivisionError as msg:
    print('Error:', msg)
except FileNotFoundError as msg1:
    print('File Error:', msg1)