#Copy one file data into another file
'''with open('emp_email.txt','r') as file_read:
    data = file_read.read()

    with open(r'C:\Pycharm_Projects\pythonProject\FileHandling\emp_email_copy.csv','w') as file_write:
        data_file = file_write.write(data)'''

#read file
with open(r'C:\Pycharm_Projects\pythonProject\FileHandling\emp_email_copy.csv','r') as read_file:
    data = read_file.read()
    print(data)