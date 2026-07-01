class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()



    def menu(self):
        user_input = input("""Welcome to chatbook !! Would you like to proceed?
                            1.Press 1 to signup
                            2. Press 2 to signin
                            3. Press 3 to write a post
                            4. Press 4 to message a friend
                            5. Press any other key to exit""")  
        if user_input == "1":
            self.signup()    # we remove pass from here and call the signup method to make thinks possible to implement
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()


# obj = chatbook() 

    def signup(self):
        email = input("Enter your email here ->")
        pwd = input("Enter your password here ->")
        self.usename = email
        self.password = pwd
        print("You have successfully signed up !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("Please signup first by pressing 1 in the main menu")
        else:
            uname = input("Enter your email/username here ->")
            pwd = input("Enter your password here ->")
            if self.username == uname and self.password == pwd:
                print("You have successfully signed in !!")
                self.loggedin = True
            else:
                print("Please input correct credentials !!")
        print("\n")
        self.menu(ss)                    

obj = chatbook()        