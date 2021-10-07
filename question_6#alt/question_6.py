<<<<<<< HEAD
# Create random numbers between any two values and add them to a list of fixed size (say 5)
import random
#generate list of random numbers
def random_list(size, min, max):
    lst = []
    for i in range(size):
        lst.append(random.randint(min, max))
    return lst
x = random_list(5, 1, 100)
# the list of random numbers
print("The list of random numbers is:")
print(x)
l = int(input("Enter a number you would like to insert"))
# enter the index to be inserted in x
i = int(input("Enter the index to be inserted"))
# insert the number in the list
x.insert(i, l)
print("The list after insertion is:")
print(x)
# Would you like to delete a number from the list?
y = input("Would you like to delete a number from the list? (y/n)")
if y == "y":
    # enter the index to be deleted
    j = int(input("Enter the index to be deleted"))
    # delete the number from the list
    x.pop(j)
    print("The list after deletion is:")
    print(x)
else:
    print("Thank you for using the program")
=======
def generate(n=5):
    import random
    a=int(input("Enter base number : "))
    b=int(input("Enter ceiling number : "))
    for i in range(0,n) :
        x=round(a+(b-a)*random.random(),2)
        list1.append(x)
    print(list1)
    global val
   
    val=float(input("Enter value to be removed: "))
    temp(val)
       

def update(pos,num) :
    list1.insert(pos-1,num)
    print(list1)

def temp(val) :
    list1.remove(val)
    print(list1)
    global num
    global pos
    num=int(input("Enter value to be inserted : "))
    pos=int(input("Enter position from start of previous value (1 onward) : "))
    update(pos,num)


n=int(input("Enter length of list : "))
list1=[]
generate(n)
>>>>>>> 964a130e5215f229fac07a4e9133df869309fe82
