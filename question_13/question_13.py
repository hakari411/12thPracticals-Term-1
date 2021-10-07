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
