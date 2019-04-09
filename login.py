def login():
    a = 1
    while a == 1:
        global user
        user = input("Username:")
        passw = input("Password:")
        with open('User.txt') as f:
         for line in f.readlines():
             us, pw = line.strip().split("|", 1)
             if (user == us) and (passw == pw):
                 print("login Successful!")
                 a = a+1
                 main()
                 return

        print("Incorrect detais, Try again!")



def register():
    print("You will recieve a generated Username from your Name and age")
    regName = input("First Name: ")
    regAge = input("Age: ")
    regPass = input("Password: ")
    regUser = (regName[0:3]+regAge)
    with open('User.txt', 'a') as file:

        file.writelines(regUser+"|"+regPass+"\n")
    print("You have Succesfully registered")
    print("Your Username is:"+regUser)
    print("Your Password is:"+regPass)
    print("!Please keep these credentials secure!")
