'''
2. Write a menu driven program to perform the operations of n customers in a Bank using binary
file "BANK.dat". 

Details of customers are to be stored in a list which contains
AccNo : Store account number of a customer
AccName: Store name of account holder
BalanceAmt : Balance amount in Bank

Write following functions
(i) StoreData(): To append a Customer's details into the binary file (N customers)
(ii) SearchName(): A function to search for a customer based on a given customer name
'''
import pickle

# To append N number of customers into the file
def StoreData():
    N=int(input("Enter no. of customers to enter: ")) 
    with open("bank.dat","ab") as f:                  # easier to use 'with open' method as it eliminates need of try except statements
        for i in range(N):                            # loop repeats as many times as no of customers specified by user
            AccNo=int(input("AccNo: ")) 
            AccName=input("AccName: ")
            BalanceAmt=int(input("BalanceAmt: "))
            data=[AccNo,AccName,BalanceAmt]           # data stored into an array first as it related to the same person
            pickle.dump(data,f)                       # dumps data into the binary file, file looks smght like [[data][data][data]]
    print("-- Success --")
    menu()                                            # goes back to main menu as its a menu driven program and software should no close until user asks to

# CODE EDITED HERE
# To search a customer from the file and display all data of that person.
def SearchName():
    AccName=int(input("AccName: "))      # CODE EDITED HERE                 # Search is based on AccNo, hence we ask user for it
    with open("bank.dat","rb") as f:                  # easier to use 'with open' method as it eliminates need of try except statements
        while True:                                   # keeps on checking data untill requirment is satisfised, here untill data of that perticular person is found
            data=pickle.load(f)                       # data is loaded one by one, instance if file is like [[data1][data2][data3]], only [data1] is loaded first attempt and then [data2] second attempt and so on
            if data[1]==AccName:          # CODE EDITED HERE                # we compare the value of AccNo in data to the entered accno, when satisfied, it proceeds or else continues with while loop as its not broken yet
                print(data)                           # if if statement satisfies, the entire list of data it was using to compare at that instant gets printed.
                break                                 # while loop is stopped if the condition as met, because was task is complete and we dont require to keep on checking data as logically only one customer will have that AccNo.
    menu()                                            # goes back to main menu as its a menu driven program and software should no close until user asks to

# Main
def menu():
    print("1 - Add Data")
    print("2 - Search Data")
    print("3 - Exit")
    task=int(input("Enter task no. to perform"))
    if task==1:
        StoreData()
    elif task==2:
        SearchName()
menu()
