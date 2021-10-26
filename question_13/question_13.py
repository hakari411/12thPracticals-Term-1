import csv
import os
path = "question_13/sports.csv"
# Open the CSV file
def open_csv():
    with open(path, newline='') as csvfile:
        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter='\t')
        # Displays the contents of the file
        for row in csvreader:
            print(row)
def main():
    open_csv()
if __name__ == '__main__':
    main()

    
    
#alternate
import csv

def CreateFile() :
     fc=open("sports.csv","w+")
     truthval= input("Do you want to enter another event ? (y/n) : ")
     while truthval == "y" or truthval== "Y" :
         fcwriter=csv.writer(fc,delimiter = "\t")
         sname = input("enter name of sport : ")
         competitions = input("enter competition : ")
         prizes = input("enter the prizes won : ")
         rec=[sname, competitions, prizes]
         fcwriter.writerow(rec)
         truthval= input("Do you want to enter records ? (y/n) : ")
     fc.close()


def csvPrinter() :
    with open("sports.csv","r+",newline="\r\n") as fc :
        fcreader=csv.reader(fc,delimiter = "\t")
        for rec in fcreader :
            print(rec)
    
    
    
CreateFile()
csvPrinter()
