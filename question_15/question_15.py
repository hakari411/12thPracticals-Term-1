# Write  a  Python  program  to  copy  the  contents  of above file “Medicine.csv” into “Temp.csv”, but with a different delimiter
import csv
def copy_csv():
    with open('question_15/Medicine.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        with open('question_15/Temp.csv', 'w') as f1:
            writer = csv.writer(f1, delimiter='\t')
            for row in reader:
                writer.writerow(row)
if __name__ == '__main__':
    copy_csv()