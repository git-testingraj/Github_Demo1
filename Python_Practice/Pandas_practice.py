import pandas as pd

py_list = {'Name':['Sunil','Ramesh','Naresh','Khilesh'],
           'Age':[20,25,46,21],
           'City':['Pune','Delhi','Bhopal','Indore']}
var = pd.DataFrame(py_list)
print(var)