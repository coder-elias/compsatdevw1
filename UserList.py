#Read list of usernames and passwords from UserList.txt
users = []
userListFile = open("UserList.txt")

for line in userListFile:
    
    line = line.strip("\n")
    users.append(tuple(line.split(":")))