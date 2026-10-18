#expense tracker
expense = []


#add expense
#----------------------------------------------------------------------------------------------------          
def add_expense():
    name = input("Name for your EXPENSE :")
    amount = int(input("Amount spent on it :"))
    new_expense = {"name":name,"amount":amount}
    expense.append(new_expense)
#----------------------------------------------------------------------------------------------------       
# view expense
def view_expense():
    print("Following are your expenses :- ")
    for y in expense:
        print(y["name"],"-",y["amount"])
#----------------------------------------------------------------------------------------------------   
# total expense    
def total_amount():
    t = 0
    for x in expense:
        t += x["amount"]
    print("Total amount spent is",t)
#----------------------------------------------------------------------------------------------------       





#stuff for while loop
#----------------------------------------------------------------------------------------------------       
n = int(input("HOW MANY EXPENSE YOU WANT TO ADD ?:"))
i = 0

while i < n :
    add_expense()
    i +=1
else:
    print("Expenses stored successfully............. ")
    print("")
#----------------------------------------------------------------------------------------------------       



#____________________________________________________________________________________________________
#viewing OR NOT
if input("To view the EXPENSES type y/n :").lower() == "y":
    add_expense()
else: 
    print("***********************")


#view the total 
if input("Do You want to know the total of your expense ? ").lower() == "yes":
    total_amount()
else: 
    print("***********************")
#____________________________________________________________________________________________________
    
    









