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



#alternate
import csv

def CreateFile() :
     fc=open("employee.csv","w+")
     truthval= input("Do you want to enter another record ? (y/n) : ")
     while truthval == "y" or truthval== "Y" :
         fcwriter=csv.writer(fc)
         empno = int(input("enter employee number : "))
         name = input("enter employee name : ")
         sal = int(input("enter salary : "))
         rec=[empno, name, sal]
         fcwriter.writerow(rec)
         truthval= input("Do you want to enter records ? (y/n) : ")
     fc.close()


def search() :
    with open("employee.csv","r+",newline="\r\n") as fc :
        fcreader=csv.reader(fc)
        empsearch = int(input("Enter the employee number required : "))
        global count
        count=0
        for rec in fcreader :
            if int(rec[0])==int(empsearch) :
                print("For EmpID = ",empsearch, " | Name : ",rec[1]," | Salary : ",rec[2])
                count+=1
                
        if count ==0 :
            print("employee not found")
        
        
    
    
    
CreateFile()
search()
