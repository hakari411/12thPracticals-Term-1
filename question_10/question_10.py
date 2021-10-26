# A binary file “Book.dat” has structure [bookno, bookname, author, price].
# Write a user defined function CreateFile() to input data for a record and add to Book.dat.
# Write a function CountRec(Author) which accepts Author name as parameter, count and return number ofbooks   by the given Author are stored in the binary file “Book.dat”

import os
import pickle
path = "question_10/Book.dat"

# Get the whole "Database"
def get_data():
    try:
        f = open(path, "rb")
        file = pickle.load(f)
        return file
    except Exception as e:
        print(e)

# get record from user as a dictionary


def get_record():  # using pickle
    bookno = int(input("Enter book no: "))
    bookname = input("Enter book name: ")
    author = input("Enter author name: ")
    price = float(input("Enter price: "))
    book = {'bookno': bookno, 'bookname': bookname,
            'author': author, 'price': price}
    return book

# add record to the database then save to the file


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


def search_record(author):
    try:
        data = get_data()
        count = 0
        for i in data:
            if i['author'] == author:
                count += 1
        return count
    except Exception as e:
        print(e)
# add_record()
# print(get_data())
# print(search_record("R.K. Narayan"))






#alternate
import pickle
finalL=[]
def CreateFile() :
     fbw=open("book.dat","ab+")
     truthval= input("Do you want to enter records ? (y/n) : ")
     while True :
         if truthval == "y" or truthval== "Y" :
             bookno = int(input("enter bookno : "))
             bookname = input("enter bookname : ")
             author = input("enter author : ")
             price = float(input("enter price : "))
             tempL = [bookno, bookname, author, price]
             fbw.seek(0)
             finalL.append(tempL)
             truthval= input("Do you want to enter records ? (y/n) : ")
         elif truthval == "n" or truthval== "N" :
             pickle.dump(finalL,fbw)
             fbw.close()
             print("file created")
             break
        
def CountRec(Author) :
     authsearch=Author
     fb = open("book.dat","rb+")
     fbr=pickle.load(fb)
     print(fbr)
     tval = input("Do you want to search records ? (y/n) : ")
     count=0
     if tval == "y" or tval== "Y" :
         for i in range(0,len(fbr)) :
             if fbr[i][2]==authsearch :
                      count+=1     
         print(authsearch," has published ",count," books")
         fb.close()
     elif tval == "n" or tval== "N" :
         fb.close()
         
              
CreateFile()
CountRec("whatever you want")
