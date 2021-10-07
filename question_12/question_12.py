import pickle
import os
path = os.path.join(os.getcwd(), "emp.dat")


def get_record():  # using pickle
    # empno ename salary
    empno = int(input("Enter empno: "))
    ename = input("Enter ename: ")
    salary = int(input("Enter salary: "))
    emp = {'empno': empno, 'ename': ename, 'salary': salary}
    return emp


def get_data():
    try:
        f = open(path, "rb")
        file = pickle.load(f)
        return file
    except Exception as e:
        print(e)

def add_record():
    if os.path.exists(path):

        try:
            data = get_data()
            data.append(get_record())
            # append to the file
            f = open(path, "wb")
            pickle.dump(data, f)
            f.close()
            print(get_data())
        except Exception as e:
            print(e)
    else:
        # Create new file
        try:
            f = open(path, "wb")
            data = []
            pickle.dump(data, f)
            f.close()
            print(get_data())
        except Exception as e:
            print(e)

# increase salary by 5000
def update_record(empno):
    if os.path.exists(path):
        try:
            data = get_data()
            for emp in data:
                if emp['empno'] == empno:
                    emp['salary'] += 5000
                    f = open(path, "wb")
                    pickle.dump(data, f)
                    f.close()
                    print(get_data())
                    break
        except Exception as e:
            print(e)
    else:
        print("File not found")
# update_record("Ajay")