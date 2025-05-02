is_running = True

def main():
    global is_running
    while is_running:
        Choice_1 = input("Login - 1, Register - 2, Quit - 3 ")
        if Choice_1 == "1":
            Log_In()
        elif Choice_1 == "2":
            Register()
        elif Choice_1 == "3":
            is_running = False
        else:
            print("Invalid Choice")

def Register():
    NewUser = ""
    NewUser = input("Username? ")
    with open("test.txt") as file:
        for line in file:
            row = line.rstrip().split(",")  
            if NewUser == row[0]:
                print("Username Already Taken")
                Register()
    NewPass = input("Password? ")
    if len(NewPass) < 4:
        print("Password must be 4 or more characters")
    else:
        file = open("test.txt", "a")
        file.write(f"{NewUser},{NewPass}\n")

def Logged_In():
    Choice_2 = input("Change Password - 1, Logout - 2 ")
    if Choice_2 == "1":
        NewPassword = (input("New Password? "))
    elif Choice_2 == "2":
        main()
    else:
        Logged_In()

def Log_In():
    # Function for user to enter 
    Username = input("Username? ")
    Password = input("Password? ")
    data1 = 0
    with open("test.txt") as file:
        for line in file:
            row = line.rstrip().split(",")  
            if Username == row[0] and Password == row[1]:
                data1 = 1
                Logged_In()
        if data1 == 0:
            Log_In()

main()