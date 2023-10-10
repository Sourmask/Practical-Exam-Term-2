'''
Write a menu driven program to perform Employee related operations performed in a company
using a binary file " Employee.dat". 

(Details of employees are represented in a LIST which contains Empno, Empname, Department, Salary)

Write following functions
(i) Append Employee's details into the binary file (N Employees)
(ii) To search an employee for a given employee number
'''
import pickle

# To append N number of employees into the file
def append():
    N=int(input("Enter no. of employees to enter: ")) 
    with open("employee.dat","ab") as f:                  # easier to use 'with open' method as it eliminates need of try except statements
        for i in range(N):                                # loop repeats as many times as no of employees specified by user
            empno=int(input("Empno: ")) 
            empname=input("Empname: ")
            dept=input("Department: ")
            sal=int(input("Salary: "))
            data=[empno,empname,dept,sal]                 # data stored into an array first as it related to the same person
            pickle.dump(data,f)                           # dumps data into the binary file, file looks smght like [[data][data][data]]
    print("-- Success --")
    menu()                                                # goes back to main menu as its a menu driven program and software should no close until user asks to

# To search an employee from the file and display all data of that person.
def search():
    empno=int(input("Empno: "))                           # Search is based on empno, hence we ask user for it
    with open("employee.dat","rb") as f:                  # easier to use 'with open' method as it eliminates need of try except statements
        while True:                                       # keeps on checking data untill requirment is satisfised, here untill data of that perticular person is found
            data=pickle.load(f)                           # data is loaded one by one, instance if file is like [[data1][data2][data3]], only [data1] is loaded first attempt and then [data2] second attempt and so on
            if data[0]==empno:                            # we compare the value of empno in data to the entered emp, when satisfied, it proceeds or else continues with while loop as its not broken yet
                print(data)                               # if if statement satisfies, the entire list of data it was using to compare at that instant gets printed.
                break                                     # while loop is stopped if the condition as met, because was task is complete and we dont require to keep on checking data as logically only one employee will have that empno.
    menu()                                                # goes back to main menu as its a menu driven program and software should no close until user asks to

# Main
def menu():
    print("1 - Add Employee Data")
    print("2 - Search Employee Data")
    print("3 - Exit")
    task=int(input("Enter task no. to perform"))
    if task==1:
        append()
    elif task==2:
        search()
menu()