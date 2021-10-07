# Write a python program to create CSV file and store empno,name,salary  in it.
import csv
import os
path = "question_14/emp.csv"
def create_csv():
    if os.path.exists(path):
        pass
    else:
        with open(path, 'w', newline='') as outcsv:
            writer = csv.writer(outcsv, delimiter=',')
            writer.writerow(i for i in ['empno', 'name', 'salary'])

# add data to csv file
def add_data_csv(empno, name, salary):
    create_csv()
    with open(path, 'a', newline='') as outcsv:
        writer = csv.writer(outcsv, delimiter=',')
        writer.writerow(i for i in [empno, name, salary])

# Take  empno from the user and display the corresponding name, salary from the file. 
def display_data_csv(empno):
    with open(path, 'r', newline='') as incsv:
        reader = csv.reader(incsv, delimiter=',')
        res = []
        for row in reader:
            if row[0] == empno:
                res.append(row)
        if len(res) == 0:
            print("No data found")
        else:
            for i in res:
                print(i)
add_data_csv(1, 'ramesh', 10000)