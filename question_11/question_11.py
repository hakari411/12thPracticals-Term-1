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

    
    
    #alternate
    
import pickle
finalL=[]


def CreateFile() :
     fbw=open("student.dat","wb+") # remeber to write ab+ not wb +
     truthval= input("Do you want to enter records ? (y/n) : ")
     while True :
         if truthval == "y" or truthval== "Y" :
             admn_no = int(input("enter admission number : "))
             name = input("enter name : ")
             percentage = int(input("enter percentage : "))
             tempL = [admn_no, name, percentage]
             finalL.append(tempL)
             truthval= input("Do you want to enter records ? (y/n) : ")
         elif truthval == "n" or truthval== "N" :
             pickle.dump(finalL,fbw)
             fbw.close()
             break
def CountRec() :
    global count
    count=0
    fb=open("student.dat","rb+")
    fbr=pickle.load(fb)
    for i in range(0,len(finalL)) :
        if fbr[i][2] > 75 :
            count+=1
            print("Admission Number : ",finalL[i][0]," | Name : ", finalL[i][1]," | Percentage : ",finalL[i][2])
        else:
            break
    print("Total number of students with percentage > 75 : ",count)
    fb.close()
    
                   
    
CreateFile()
CountRec()
