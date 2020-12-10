#compares inputs to data found in the text file
while True:
    access = 0
    for user in users:

        if(user[0] == username and user[1] == password):
            access = 1
            break

    if(access == 1):
        print("Correct Username and Password")
        break

    else:
        print("\n\nINCORRECT USERNAME OR PASSWORD\nRetype Username and Password\n")

    username = input("Username: ")
    password = input("Password: ")
