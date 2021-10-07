import pickle
import os

path = os.path.join(os.path.dirname(__file__), "student.dat")
def get_data():
    try:
        f = open(path, "rb")
        file = pickle.load(f)
        return file
    except Exception as e:
        print(e)
# I have assumed here that the data is stored in a list of dictionaries (refer question_10.py)

# Function to show records with marks above 75
def show_records():
    data = get_data()
    count = 0
    for i in data:
        if i["marks"] > 75:
            print(i)
            count += 1
    print("The count of people above 75%  ", count)
