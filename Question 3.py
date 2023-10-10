'''
3. A binary file "Employee.dat" maintains the details of employees in a company

which has structure [Empno, Empname, Department, Salary]

Write a menu driven program to perform the following
(i) Function AppendRecord() to append Employee's details into the binary file
(ii)Function AvgSalary() which accepts the department as parameter and find the average salary of all employees in that department
'''
import pickle

# To append N number of employees into the file
def AppendRecord():
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

# To search a deptartment and get average
def AvgSalary(dept):                                      # search is based on department, here is it passed as a parameter for the function
    with open("employee.dat","rb") as f:
        sum=0                                             # We predefine it to user in average equation later on
        length=0                                          # We predefine it to user in average equation later on
        while True:                                       # Will keep repeating untill all data checked
            try:                                     
                data=pickle.load(f)                       # data is loaded one by one, instance if file is like [[data1][data2][data3]], only [data1] is loaded first attempt and then [data2] second attempt and so on 
                if data[2]==dept:                         # we compare the value of dept in data to the entered dept, when satisfied, it proceeds or else continues with while loop as its not broken yet
                    sum+=data[3]
                    length+=1
            except:
                break 
        avg=sum/length                                    # sum is the sum of salaries and length is the number of employees in that branch, we derive length by taking advantage of the if statement written prior as it only gets satisfied if employee is from that department
        print(avg)
    menu()                                                # goes back to main menu as its a menu driven program and software should no close until user asks to

# Main
def menu():
    print("1 - Add Employee Data")
    print("2 - Get Average Salary")
    print("3 - Exit")
    task=int(input("Enter task no. to perform"))
    if task==1:
        AppendRecord()
    elif task==2:
        dept=input("Enter Department: ")
        AvgSalary(dept)
menu()
