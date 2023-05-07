
username = "Praveen"
password = 1234

c_name = input("enter your name:")
c_password = int(input("enter your password:"))

if c_name == username and c_password == password:
    # print("successfully login")
    print("""
               1.Deposit
               2.withdraw
               3.mini_statement
               4.exit
                   """)
    amount  = 5000
    option = int(input("select your option:"))
if option == 1:
    dep = int(input("enter the amount"))
    amount+=dep
    print("Total amount:",amount)
elif option == 2:
    withd = int(input("enter the amount:"))
    amount-=withd
    print("Total amount:",amount)
elif option == 3:
    print("=====ATM=====")
    print("username:",username)
    print("Total amount:",amount)
    print("Thanks for visiting")
elif option == 4:
    exit()
else:
    print("please enter the correct credentials")
    
